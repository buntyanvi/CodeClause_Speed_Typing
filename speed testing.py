import time

def calculate_typing_speed(start_time, end_time, text):
    total_time = end_time - start_time
    words = text.split()
    total_words = len(words)
    words_per_minute = total_words / (total_time / 60)
    return words_per_minute

def run_typing_test():
    text = "The quick brown fox jumps over the lazy dog."
    print("Welcome to the Speed Typing Test!")
    print("Type the following text:")
    print(text)
    input("Press Enter when you're ready to start.")
    print("Type now:")
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    speed = calculate_typing_speed(start_time, end_time, user_input)
    print("\nCalculating your results...")
    time.sleep(1)
    print(f"\nYour typing speed: {speed:.2f} words per minute.")
    accuracy = calculate_accuracy(text, user_input)
    print(f"Accuracy: {accuracy:.2f}%")

def calculate_accuracy(text, user_input):
    correct_chars = sum([1 for t, u in zip(text, user_input) if t == u])
    accuracy = (correct_chars / len(text)) * 100
    return accuracy

run_typing_test()
