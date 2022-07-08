import random


def get_integer(prompt):
    """
    Get's an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The string that user will see, when
        they're prompted to enter the value.
    :return: Integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("Enter an integer!")


# help(get_integer)   # Can be used while working in python interactive shell.
highest = 100
answer = random.randint(1, highest)
# print(answer)   # TODO: remove after testing

guess = 0
print("Guess a number between 1 and {}".format(highest))

while guess != answer:
    guess = get_integer("guess : ")
    while guess not in range(0, highest+1):
        print("Please enter a value between 1 to {}".format(highest))
        guess = int(input("guess : "))
    if guess == 0:
        print("See you next time")
        break
    if guess == answer:
        print("You guessed it in the right!!")
        break
    else:
        if guess < answer:
            print("Guess higher..")
        elif guess > answer:
            print("Guess lower..")
