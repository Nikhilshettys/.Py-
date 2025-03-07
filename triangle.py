import math

a = float(input("Enter side A:"))
b = float(input("Enter side B:"))

#c = (a**2) + (b**2)
c = math.sqrt(pow(a,2) + pow(b,2))
print(f"side c ={c}")