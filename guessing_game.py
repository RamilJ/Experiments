import random

secret_number = random.randint(1, 100)

remaining_guesses = 10

num_guesses = 0

for i in range(remaining_guesses):
    guess = int(input("Guess a number between 1 and 100: "))
    num_guesses = num_guesses + 1
    remaining_guesses = remaining_guesses - 1

    if guess == secret_number:
        print("Correct, %d is the number. You guessed %d times" %(secret_number, num_guesses))
        break
    else:
        if guess < secret_number:
            print("Too low! You have %d guess remaining" %remaining_guesses)
        else:
            print("Too high! You have %d guess remaining" %remaining_guesses)
            
else:
    print("Sorry, you ran out of guesses. The secret number was", secret_number)
