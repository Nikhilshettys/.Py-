#Ex 1 Rectangle area calc


length =float( input("Enter the lenght:"))
width = float(input("Enter the width:"))
area = length * width
print (f"The area is {area} cm")


# Ex 2 shopping cart program

item = input("What item would you like to busy ?:")
price = float(input("What is the price?"))
quantity = int(input("How many would u like?:"))

total = price * quantity
print(f"YOU have bought { quantity} X {item}/s")
print(f"your total is :${total}")