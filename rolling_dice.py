import random
random_number = random.randrange(1 , 6)
while True:
    answer = input("Would you like to roll the dice?")
    if not answer:
        print("You didn't say anything!")
    if answer == "yes":
        print("Your number is...")
        print(random_number ,"!")
    if answer == "no":
        print("Okay, have a good day.")
        break