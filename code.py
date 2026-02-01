# worlde game
import random

def load_files(path):
    with open(path) as f:
        word = [one_word.strip() for one_word in f]
        
    return word


def is_word_valid(user_guessed, guesses):
    return len(user_guessed) ==5 and user_guessed in guesses
   
def guess_word_checking(user_guessed, word):
    
    result = ""
    
    for i in range(5):
        if user_guessed[i] == word[i]:   # if any charactor is present and at the correct position
            result += "\033[32m" + user_guessed[i].upper() + " "  # make that charactor Green
            
        elif user_guessed[i] in word:   # if any charactor is present in the answer "Word"
            result += "\033[33m" + user_guessed[i].upper()  + " "  # make it Yellow
            
        else:
            # letter not present at all → RED
            result += "\033[31m" + user_guessed[i].upper() + " "    # make it Red ( means the word is not Correct)
    
    return result + "\033[0m"


def print_guesses(all_guesses):
    print("┌──────────────────┐")

    for word in all_guesses:
        
        print("│ "+ word + ("       │"))
        
    empty_row = 6 - len(all_guesses)
    for _ in range(empty_row):
        print("│  ━ ━ ━ ━         │")
    print("└──────────────────┘") 
        
    return


    
def wordle(guesses, answers):
    
    answer_word = random.choice(answers).lower()
    
    
    print("🎮 Welcome to WORDLE -----the game of guessing a Word-----")
    print("Guess the 5-letter word (6 attempts)\n")
    
    first_attempt = 1
    max_attempts = 6
    all_guesses = []
    
    while first_attempt <= max_attempts:
        user_guessed = input("Enter Guess #" + str(first_attempt) + ": ").lower()
        
        if not is_word_valid(user_guessed, guesses):
            if not len(user_guessed) == 5:
                print("Please enter an English word with 5 letters.")
            else:
                print("Incorrect Word! It don't make sense!")
            continue
            
        if answer_word == user_guessed:
            # print("Congratulation! You guessed the correct word: " + user_guessed + "\033[32m")
            print("Congratulation! You guessed the correct word:\033[32m", user_guessed + "\033[0m")
            break
            
        
        first_attempt += 1
        feedback = guess_word_checking(user_guessed, answer_word)
        all_guesses.append(feedback)
        print_guesses(all_guesses)
        
        
        if first_attempt > max_attempts:
            print("😢 Game Over!")
            print("Game over. The secret word was: \033[32m", answer_word.upper() + "\033[0m")
            




guesses_file = "guesses.txt"
answers_file = "answers.txt"

guesses = load_files(guesses_file)
answers = load_files(answers_file)

wordle(guesses, answers)