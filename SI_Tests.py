import random
#Git Test
def main():
    correct_letters = []
    incorrect_letters = []
    random_words = ['express','voice','adaptable','vacation','belong','swift','noisy','ghost','fury','dreary','squeeze']
    x = (len(random_words) - 1)
    word_index = random.randint(0,x)
    guess_word = random_words[word_index]
    print("Welcome to word guesser! You will have",len(guess_word) + 5,"guesses to figure out the letters to the word!")
    #print(guess_word)
    t = 0
    while t <= len(guess_word)+5:
        letter_guess = str(input("Please enter the letter you are guessing here in lower case: "))
        #for i in range(len(guess_word)):
        if letter_guess in guess_word:
            print("There was an:",letter_guess)
            if letter_guess not in correct_letters:
                correct_letters.append(letter_guess)
        else:
            print("There was not a:",letter_guess)
            if letter_guess not in incorrect_letters:
                incorrect_letters.append(letter_guess)
        t = t + 1
    print("Correct letters:",correct_letters)
    print("Incorrect letters",incorrect_letters)
    print("You have 3 tries to guess the word based on the above letters!")
    for final in range(3):
        final_guess = str(input("Enter your guess here: "))
        if final_guess == guess_word:
            print("Congrats you got it!")
            break
        elif final_guess != guess_word:
            print("Sorry thats not it!")

    if final_guess != guess_word:
        print("Better luck next time, the word was:",guess_word)
main()