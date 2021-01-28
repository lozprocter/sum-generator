from random import randint

while True:
    first = randint(0,100)
    second = randint(0,100)
    user = input("Press the enter key", )
    if user == "":
        print(first, "+", second)
    answer = input("Answer:", )
    if first+second == int(answer):
        print("Good Job!")
    else:
        print("Bad Luck")

