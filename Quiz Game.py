# Building a game project

print("Hello there welcome to my game!")

# asking if the user is willing to play the game
playing = input("Are you willing to play?(Yes / No) ")

if playing == "Yes":
    print("Let's play the game!")
else:
    print("Okay, maybe next time!")
    quit()
score = 0
# starting the game after the Yes response 
# first question
answerQuestion1 = input("Question 1 : How many days in a week? ")

if answerQuestion1 == "7":
    print("Correct!")
    score += 1
else:
    print("That is incorrect!")
    answerQuestionRetry1 = input("Do you want to try one more time? (Yes / No) ")
    if answerQuestionRetry1 == "Yes":
        answerQuestionRetry1 = input("How many days in a week? ")
        if answerQuestionRetry1 == "7":
            print("Correct!")
            score += 0.5
        else:
            print("That is incorrect!")
    else:
         print("The correct answer is 7.")
    print("Let's continue the second question")
# second question

answerQuestion2 = input("Question 2 : How many months in a year? ")
if answerQuestion2 == "12":
    print("Correct!")
    score += 1
else:
    print("That is incorrect!")
    answerQuestionRetry2 = input("Do you want to try one more time? (Yes / No) ")
    if answerQuestionRetry2 == "Yes":
        answerQuestionRetry2 = input("How many months in a year? ")
        if answerQuestionRetry2 == "12":
            print("Correct!")
            score += 0.5
        else:
            print("Incorrect!")
    else:
        print("The correct answer is 12.")

print(f"Your point is {(score)}.")
print(f"Your point is {(score/4) * 100}%.\nThank you for playing!")