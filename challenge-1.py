import time

#Welcome the user
print("Hello everyone, this will be my first time using python to code a multiple choice quiz. Enjoy!")
time.sleep(1)

#Chances
chances = 1
print("You will have", chances, "chance to answer correctly. \nPlease put the alphabet of the answer\n")
time.sleep(2)

#Score
score = 0

#question number 1
question_1 = print("1) What is my nickname?\n(a) Juliana\n(b) Jenny\n(c) Jennifer\n(d) Jolie\n\n ")
answer_1 = "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_1, "\n\n")

time.sleep(2)

#question number 2
question_2 = print("2) What is my age? \n(a) 14\n(b) 15\n(c) 16\n(d) 17\n\n ")
answer_2 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_2):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_2, "\n\n")

time.sleep(2)

#question number 3
question_3 = print("3) What grade am I in? \n(a) 8\n(b) 9\n(c) 10\n(d) 11\n ")
answer_3 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_3, "\n\n")

time.sleep(2)

#question number 4
question_4 = print("4) What is my favorite color?\n(a) blue\n(b) yellow\n(c) green\n(d) red\n\n ")
answer_4 = "d"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_4, "\n\n")

time.sleep(2)

#question number 5
question_5 = print("5) How many years have I been studying here?\n(a) 5\n(b) 6\n(c) 7\n(d) 8\n\n ")
answer_5 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_5, "\n\n")

time.sleep(1)

#print the score
while score >= 4:
    print("Well done! Your score was", score)
    break

while score <= 3:
    print("Better luck next time! Your score was", score)
    break
#Goodbye message
print("Thank you for playing my game!")