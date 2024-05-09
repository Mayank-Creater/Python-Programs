number = int(input("Enter number to be guessed: "))
original_list = []
temp_num = number
history_list = []

for i in range(100):
    print()

while temp_num != 0:
    temp = temp_num % 10
    temp_num = temp_num // 10
    original_list.append(temp)

original_list = original_list[::-1]

guess_count = 12

while guess_count != 0:
    guess = input("Enter guess: ")
    if guess.isnumeric() == False:
        print("Invalid input. Try again.")
        continue
    else:
        guess_num = int(guess)
    temp_guess = guess_num
    guess_list = []

    while temp_guess != 0:
        temp = temp_guess % 10
        temp_guess = temp_guess // 10
        guess_list.append(temp)

    guess_list = guess_list[::-1]

    if len(guess_list) != 4:
        print("Guess must be of 4 digits!")
        continue

    count = 0

    for z in guess_list:
        count_num = guess_list.count(z)
        if count_num > count:
            count = count_num

    if count > 1:
        print("Guess must not have duplicate digits!")
        continue

    exist = 0
    position = 0

    for i in range(0,4):
        if guess_list[i] == original_list[i]:
            position += 1
        elif guess_list[i] in original_list:
            exist += 1

    history = "{}: exist: {}, position: {}".format(guess_num, exist, position)

    if len(history_list) != 0:
        for j in history_list:
            print(j)

    history_list.append(history)
    print(history)

    if guess_num == number:
        print("You guessed it right!!!")
        print("You did it in {} guesses".format(12-guess_count))
        break
    else:
        guess_count -= 1
        print("{} guesses left!".format(guess_count))
        print()

else:
    print("You can't guess it!")
    print("It was {}".format(number))
