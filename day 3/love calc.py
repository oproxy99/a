from re import U


print("Welcome to the Love Calculator!")
name1=input("Enter your name: \n")
name2=input("Enter their name: \n")

name=name1+name2
name=name.lower()

t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")
true = t+r+u+e

l=name.count("l")
o=name.count("o")
v=name.count("v")
e=name.count("e")
love = l+o+v+e

score= int(str(true) + str(love))

if score<10 or score>90:
    print(f"Your score is {score}, you mix together like coke and mentos.")

elif 40<= score <=50:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}, not a good match.")

