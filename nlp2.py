
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import wordninja
import uvicorn
import re
from functools import lru_cache

app = FastAPI(title="Joined Words Splitter")

class TextInput(BaseModel):
    text: str

# Small compound word dictionary for tricky edge cases
COMPOUND_WORDS = {
    "everyone": ["every", "one"],
    "everybody": ["every", "body"],
    "everything": ["every", "thing"],
    "anyone": ["any", "one"],
    "anything": ["any", "thing"],
    "nothing": ["no", "thing"],
    "somebody": ["some", "body"],
    "something": ["some", "thing"],
    "somewhere": ["some", "where"],
    "nowhere": ["no", "where"],
    "anywhere": ["any", "where"],
    "hereafter": ["here", "after"],
    "forevermore": ["forever", "more"],
    "overseas": ["over", "seas"],
    "underneath": ["under", "neath"],
    "without": ["with", "out"],
    "within": ["with", "in"],
    "notwithstanding": ["not", "withstanding"],
}

def clean_text(text: str) -> str:
    # Replace underscores, dots, commas, @, and other punctuations with space
    text = re.sub(r'[_@.,!?:;]+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def is_valid_word(word: str) -> bool:
    """Check if wordninja recognizes this word as valid (single token) and length>=2."""
    return len(word) >= 2 and wordninja.split(word) == [word]

@lru_cache(maxsize=None)
@lru_cache(maxsize=None)
def split_subwords_greedy(word: str):
    """
    Greedy longest-prefix matching for compound words.
    Always chooses the first valid prefix and continues.
    """
    n = len(word)
    result = []
    i = 0

    while i < n:
        found = False
        # Try to match the longest prefix starting at i
        for j in range(n, i, -1):
            candidate = word[i:j]

            # Check compound dictionary first
            if candidate in COMPOUND_WORDS:
                result.extend(COMPOUND_WORDS[candidate])
                i = j
                found = True
                break
            # Then check if wordninja recognizes it
            elif is_valid_word(candidate):
                result.append(candidate)
                i = j
                found = True
                break

        if not found:
            # If nothing matches, skip one char to avoid infinite loop
            i += 1

    return result

def manual_split(text: str):
    """Longest valid word first split (similar to previous)."""
    words = []
    i = 0
    n = len(text)
    while i < n:
        found_word = None
        for j in range(n, i, -1):
            candidate = text[i:j]
            if is_valid_word(candidate):
                found_word = candidate
                break
        if found_word:
            words.append(found_word)
            i += len(found_word)
        else:
            i += 1
    return words

@app.post("/split")
async def split_words(input: TextInput):
    # Clean unwanted characters and normalize spaces
    cleaned_text = clean_text(input.text).replace(" ", "").lower()

    if not cleaned_text.isalpha():
        raise HTTPException(status_code=400, detail="Input must contain only letters after cleaning")

    # Initial split using manual longest-word-first
    initial_words = manual_split(cleaned_text)
    final_words = []

    # Check compound words and apply greedy subword splitting
    for w in initial_words:
        subwords = split_subwords_greedy(w)
        final_words.extend(subwords)

    return {"words": final_words}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
