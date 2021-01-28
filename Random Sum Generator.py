from random import randint

while True:
    try:
        first = randint(0,100)
        second = randint(0,100)
        #generates question and takes user input (answer)
        print(first, "+", second)
        answer = input("Answer:", )

        #checks that the user input matches the expected (correct) annswer and prints feedback
        if first+second == int(answer):
            print("Good Job!")
        else:
            print("Bad Luck")
        #protects the program from crashing from a non-numerical input
    except ValueError:
        print("Not a valid input")
