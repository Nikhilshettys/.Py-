#python calculator



a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
print("\n1.Addition."
               "\n2.Subtraction\n3.multiplication\n4.division\n")
choice = input("Enter your choice:")

if choice == "1":
    print(a + b)
elif choice == "2":
    print(a - b)
elif choice == "3":
    print(a * b)
elif choice == "4":
    print(a / b)
else:
    print("Pls enter valid choice")
