import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board']

word = random.choice(words)

print("Doan ca ky tu: ")

guesses = ''
turns = 12

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end=" ")

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You Win")
        print("Tu do la: ", word)
        break

    print()
    guess = input("Doan 1 ky tu:")

    guesses += guess

    if guess not in word:

        turns -= 1
        print("SAI")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")