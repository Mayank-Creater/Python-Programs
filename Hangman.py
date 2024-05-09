word = input("Enter a word to be guessed: ")
letters_list = [x for x in word]
guess_list = ["_" for y in range(len(letters_list))]
guess_count = len(letters_list)

while guess_count > -1:
    guess = input("Enter a letter: ")
    if guess in letters_list:
        for i in range(len(letters_list)):
            if letters_list[i] == guess:
                guess_list[i] = guess
        print(guess_list)
        print()
    else:
        print("Wrong guess!")
        guess_count -= 1
        print(guess_list)
        print("You have " + str(guess_count) + " guesses left.")
        print()

    if guess_list == letters_list:
        print("You win!")
        break
    elif guess_count == 0:
        print("You lose!")
        print("The word was: " + word)