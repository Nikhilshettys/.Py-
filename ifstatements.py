#if Do some code only IF some condition is true
#Else do something else

age = int(input("Enter your age:"))

if age>=18:
    print("YOU are signed up!")
elif age<0:
    print("YOU noy yet born")
elif age>=100:
    print("You are  TOO old to sign up")
else:
    print("You are not signed up!!!")

#boolean if


online  = True

if online:
    print("user is online")
else:
    print("user is offline")


#if 2

name = input ("Enter ur name:")

if name=="":
    print("you did not type in your name")
else:
    print(f"Hello {name}")