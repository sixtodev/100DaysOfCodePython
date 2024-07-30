import random
import hangman_art
import hangman_words
#step 1


end_of_game = False
display = []
lives = 6
# Randomly choose a word form the word_list and assign it to a variable called
# chosen_word

chosen_word = random.choice(hangman_words.word_list)

print(f"Pssss, The solution is {chosen_word}.")


#Ask the user to guess a letter and assign 
#their answer to a variable called guess, make guess lowercase.


word_length = len(chosen_word)
for _ in range(word_length):
    display += ("_")


while not end_of_game :

    guess = input("Guess a letter: ").lower()
# check if the letter the user guessed  is one of the letters in the chosen_word
    for n in range(word_length):
        letter = chosen_word[n]
        if letter == guess:
            display[n] = letter

    if guess not in chosen_word:
        lives -= 1  
        if lives == 0:
            end_of_game = True
            print("---------")
            print("YOU LOSE!")
            print("---------")

    print("")
    print(f"{' '.join(display)}")
        
              


    if "_" not in display:
        end_of_game = True
        print("---------")
        print("YOU WIN!")
        print("---------")


    print(hangman_art.stages[lives])
       
    

    
    
