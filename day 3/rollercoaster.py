print("Welcome to the Roller Coaster Ride!!")
height=int(input("What is your height in cm?\n"))

if height < 120:
    print("You are too short to take the ride.")

else:
    print("You can take the ride.")
    age=int(input("What is your age?\n"))

    if age < 12:
        bill=5
    elif age <= 18:
        bill=7
    else:
        bill=10

    photo=input("Do you want pictures taken? Yes or No \n")
    if photo=="Yes":
        bill=bill+3
        print(f"Your total cost is ${bill}.")
    else:
        print(f"The total cost is ${bill}.")

