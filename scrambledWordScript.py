import random
import time

# List of words for each difficulty level
words = {
    "Beginner": ["apple", "banana", "cat", "dog", "elephant", "fish", "grape", "hat", "ice", "juice", "kite", "lion", "monkey", "nest", "orange"],
    "Intermediate": ["bicycle", "camera", "dolphin", "guitar", "jungle", "kangaroo", "laptop", "mountain", "ocean", "piano", "rabbit", "snake", "tiger", "umbrella", "violin"],
    "Advanced": ["astronomy", "biology", "chemistry", "dinosaur", "electricity", "geography", "history", "jupiter", "kaleidoscope", "lightning", "mathematics", "neptune", "oxygen", "planet", "quasar"],
    "Expert": ["algorithm", "biotechnology", "cryptography", "differential", "electromagnetic", "fluorescence", "gravitational", "holography", "isotope", "kinematics", "logarithm", "nanotechnology", "oscilloscope", "paleontology", "quantum"]
}

# Function to scramble a word
def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

# Function to generate the puzzle for a specific difficulty
def generate_puzzle(difficulty):
    scrambled_words = []
    for word in words[difficulty]:
        scrambled_word = scramble_word(word)
        scrambled_words.append((word, scrambled_word))
    return scrambled_words

# Function to display the puzzle
def display_puzzle(scrambled_words):
    print(f"\nHere are your scrambled words:")
    for i, (original, scrambled) in enumerate(scrambled_words, 1):
        print(f"{i}. {scrambled}")

# Function to check the user's answers
def check_answers(scrambled_words, time_limit):
    score = 0
    start_time = time.time()
    end_time = start_time + time_limit

    for i, (original, scrambled) in enumerate(scrambled_words, 1):
        if time.time() > end_time:
            print("\nTime's up!")
            return score
        user_guess = input(f"{i}. Unscramble '{scrambled}' (Time left: {int(end_time - time.time())}s): ")
        if user_guess.lower() == original.lower():
            print("Correct! +1 point")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{original}'.")
    return score

# Main function to run the game
def main():
    print("Welcome to the Scrambled Word Puzzle Game!")
    print("Choose a difficulty level:")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")
    print("4. Expert")

    # Get the player's choice
    choice = input("Enter the number of your choice (1-4): ")
    while choice not in ["1", "2", "3", "4"]:
        choice = input("Invalid choice. Please enter a number between 1 and 4: ")

    # Map choice to difficulty level
    difficulty_levels = {"1": "Beginner", "2": "Intermediate", "3": "Advanced", "4": "Expert"}
    difficulty = difficulty_levels[choice]

    print(f"\nYou have selected the {difficulty} level.")
    print("You have 120 seconds to unscramble as many words as you can. Let's begin!\n")

    # Generate and display the puzzle
    scrambled_words = generate_puzzle(difficulty)
    display_puzzle(scrambled_words)

    # Start the game with a 120-second timer
    time_limit = 120
    score = check_answers(scrambled_words, time_limit)

    # Display the final score
    total_words = len(scrambled_words)
    print(f"\nGame over! You scored {score}/{total_words}.")

if __name__ == "__main__":
    main()