import random
def hangman():
    word_list=["interest", "coding", "github", "open", "source"]
    word=random.choice(word_list)
    guesses=6
    spaces = ""
    for characters in word:
        spaces = spaces + "_"
    while guesses>-1:
        print(f"You have {guesses} guesses left.")
        print(spaces)
        term=input("Please enter a letter you think is in this word, or type the whole word: ")
        if term==word:
            print("Congrats! You guesses the word!")
            break
        elif term in word:
            x = word.rfind(term)
            spaces = list(spaces)
            spaces[x] = term
            spaces = "".join(spaces)
            print("In the word!")
            if "_" not in spaces:
                print("Congrats! You won")
                break
        else:
            guesses-=1
            print("Not in the word!")
            if guesses == 0:
                print("Oops! You are out of guesses!")
                print(f"The word was: {word}")
                break

hangman()