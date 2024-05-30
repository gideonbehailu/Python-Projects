import random 

firstName = input("What should be your nickname: ")

print(f"Welcome {firstName}! Let's play Rock/Paper/Scissors")
print("Type in Q to quit the game")

user_score = 0
computer_score = 0
draw_count = 0

options = ["rock", "paper", "scissors"] 

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_computer = random.randint(0, 2)
    # rock:0, paper:1, scissors:2
    computer_pick = options[random_computer]
    print(f"Computer picked {computer_pick}.")
          
    if user_input == "rock" and computer_pick == "scissors":
        print (f"{firstName} you win hehe!")
        user_score += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print (f"{firstName} you win hehe!")
        user_score += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print (f"{firstName} you win hehe!")
        user_score += 1
        continue

    elif user_input == computer_pick:
        print ("Oww that was a draw!")
        draw_count += 1 
        continue
    else:
        print (f"{firstName} you lose Boooo!")
        computer_score += 1

print(f"There were {draw_count}")
print(f"{firstName} you won {user_score} times.")
print(f"{firstName} you lost the game {computer_score} times")