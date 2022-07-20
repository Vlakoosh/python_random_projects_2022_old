import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word

def hangman():
    print("")
    word = get_valid_word(words).upper()
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #keeps track of letters that the user already guessed
    lives = 3
    
    while len(word_letters) > 0 and lives != 0:

        # ' '.join([a, b, c, d]) --> 'a b c d'
        if used_letters:
            print("You have already used these letters: ", ', '.join(used_letters))

        #what's the current word status (W _ R D)
        word_list = [letter if letter in used_letters else '_' for letter in word]

        
        print("Current word: ", " ".join(word_list))
        print(f"Lives left: {lives}")

        print("")
        
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
        elif user_letter in used_letters:
            print("You have used that letter already")
        else:
            print("Invalid character")
    # gets here when len(word_letters) == 0
    print("")
    if lives == 0:
        print("You are out of lives")
    print(f'Correct word was: {word}')


hangman()