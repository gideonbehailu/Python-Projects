import random

top_of_range = input("Please input you number here ")


if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please input a number greater than 0!")
        

else:
    print("Please input a number!")
    quit()

random_number = random.randint(0, top_of_range)

number_of_guesses = 0

while True:
    number_of_guesses += 1
    user_guess = input("Guess the numbere ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please input a number!")
        continue
    if user_guess == random_number:
        print("You gussed right!")
        break
    else:
        if user_guess > random_number:
            print("You guessed above the number")
        else:
            print("You guessed below the number")
        
print(f"You got the answer with {number_of_guesses} guesses")