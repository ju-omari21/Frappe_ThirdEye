import random
rand = random.randrange(1,5)

user_input = int(input("Hey there, please enter your gussed number between 1 and 20: "))
if user_input == rand:
    print(f"Your gusse is true")

else:
    print("Your gusse is wrong")
