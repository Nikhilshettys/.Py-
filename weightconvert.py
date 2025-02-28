

weight = float(input("Enter your weight:"))
unit = input("Kilogram or pounds (K or L)")

if unit=="K":
    weight = weight * 2.205
    unit ="Lbs"
elif unit =="L":
    weight = weight / 2.205
    unit = "kgs"
else:
    print(f"Enter valid")

print(f"Your weight is :{weight:.2f} {unit}")