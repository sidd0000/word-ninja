from app import clean_text, manual_split, split_subwords_greedy

# List of tricky test cases
test_cases = [
    {"input": "everyone", "expected": ["every", "one"]},
    {"input": "everyones", "expected": ["every", "one", "some"]},
    {"input": "everybody", "expected": ["every", "body"]},
    {"input": "everything", "expected": ["every", "thing"]},
    {"input": "anyone", "expected": ["any", "one"]},
    {"input": "anyones", "expected": ["any", "one", "some"]},
    {"input": "anything", "expected": ["any", "thing"]},
    {"input": "nothing", "expected": ["no", "thing"]},
    {"input": "somethings", "expected": ["some", "thing", "some"]},
    {"input": "somewhere", "expected": ["some", "where"]},
    {"input": "somebody", "expected": ["some", "body"]},
    {"input": "nowhere", "expected": ["no", "where"]},
    {"input": "anywhere", "expected": ["any", "where"]},
    {"input": "hereafter", "expected": ["here", "after"]},
    {"input": "forevermore", "expected": ["forever", "more"]},
    {"input": "overseas", "expected": ["over", "seas"]},
    {"input": "underneath", "expected": ["under", "neath"]},
    {"input": "without", "expected": ["with", "out"]},
    {"input": "within", "expected": ["with", "in"]},
    {"input": "notwithstanding", "expected": ["not", "withstanding"]},
    {"input": "good.morning_everyone", "expected": ["good", "morning", "every", "one"]},
    {"input": "how.are.you.doing", "expected": ["how", "are", "you", "doing"]},
    {"input": "something_special_here", "expected": ["some", "thing", "special", "here"]},
    {"input": "nothingness", "expected": ["no", "thing", "ness"]},
    {"input": "anyone_else", "expected": ["any", "one", "else"]},
    {"input": "somewhere_over_the_rainbow", "expected": ["some", "where", "over", "the", "rainbow"]},
    {"input": "everything_is_possible", "expected": ["every", "thing", "is", "possible"]},
    {"input": "everybody_here", "expected": ["every", "body", "here"]},
    {"input": "good_evening_everyone", "expected": ["good", "evening", "every", "one"]},
    {"input": "over_and_under", "expected": ["over", "and", "under"]},
    {"input": "not_withstanding_all", "expected": ["not", "withstanding", "all"]},
    {"input": "hello_world", "expected": ["hello", "world"]},
    {"input": "anywhere_else", "expected": ["any", "where", "else"]},
    {"input": "without_a_doubt", "expected": ["with", "out", "a", "doubt"]},
    {"input": "forevermore_and_ever", "expected": ["forever", "more", "and", "ever"]},
    {"input": "hereafter_today", "expected": ["here", "after", "today"]},
    {"input": "underneath_the_stars", "expected": ["under", "neath", "the", "stars"]},
    {"input": "somethings_special", "expected": ["some", "thing", "some", "special"]},
    {"input": "everyones_here", "expected": ["every", "one", "some", "here"]},
    {"input": "anything_can_happen", "expected": ["any", "thing", "can", "happen"]},
    {"input": "nothing_but_the_best", "expected": ["no", "thing", "but", "the", "best"]},
    {"input": "good_morning_everybody", "expected": ["good", "morning", "every", "body"]},
    {"input": "somewhere_over", "expected": ["some", "where", "over"]},
    {"input": "nowhere_to_run", "expected": ["no", "where", "to", "run"]},
    {"input": "everything_and_everyone", "expected": ["every", "thing", "and", "every", "one"]},
    {"input": "anyone_at_home", "expected": ["any", "one", "at", "home"]},
    {"input": "hereafter_never", "expected": ["here", "after", "never"]},
    {"input": "notwithstanding_the_law", "expected": ["not", "withstanding", "the", "law"]},
    {"input": "without_end", "expected": ["with", "out", "end"]},
    {"input": "within_limits", "expected": ["with", "in", "limits"]},
    {"input": "overseas_travel", "expected": ["over", "seas", "travel"]},
]

def run_tests():
    for idx, case in enumerate(test_cases, 1):
        cleaned = clean_text(case["input"]).replace(" ", "").lower()
        initial_words = manual_split(cleaned)
        final_words = []
        for w in initial_words:
            final_words.extend(split_subwords_greedy(w))

        if final_words == case["expected"]:
            print(f"Test {idx} PASSED: {case['input']} → {final_words}")
        else:
            print(f"Test {idx} FAILED: {case['input']}")
            print(f"  Expected: {case['expected']}")
            print(f"  Got     : {final_words}")

if __name__ == "__main__":
    run_tests()
