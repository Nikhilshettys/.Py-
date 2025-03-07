#print(help(str))
#valid user inout exercise
#1.Username is no more than 12 characters
#2.Username must not contain spaces
#3.Username must not contain digits

username= input ("Enter a username:")


username.find(" ")
if len(username) >12:
    print("your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contains digits")
else:
    print(f"welcome {username}")