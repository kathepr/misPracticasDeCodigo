
print("\nWelcome to the rollercoaster")
height= float(input("What's your height in cm? "))
bill = 0

if height >= 120:
    print("Amazing! You can ride the rollercoaster!")
    age = int(input("What's your age? "))
    if age < 12:
        bill = 5
        print("You have to pay $5")
    elif age >=12 and age <=18:
        bill = 7
        print("You have to pay $7")
    else:
        bill = 12
        print("You have to pay $12")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
        print(f"Your final bill is {bill}")
else:
    print("Sorry, you can't ride. You are not tall enough for this rollercoaster. Try again in a few years :) ")