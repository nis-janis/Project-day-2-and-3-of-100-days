print("Welcome to the Roller coaster!")
height = int(input("what is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the Roller coaster")
    age = int(input("what is your age? "))
    if age <= 12:
        print("Ticket price is: $5")
        bill = 5
    elif age <= 18:
        print("Ticket price is: $7")
        bill = 7
    elif age>=45 and  age<=55:
        print("Your ride will be free")
    else:
        print("the ticket price is: $12")
        bill = 12
    photo = input("Do you want a photo? type Y or N")
    if photo == "Y":
        bill = bill + 3
    print(f"Your bill is ${bill}")

else:
    print("Sorry! You can't ride")
