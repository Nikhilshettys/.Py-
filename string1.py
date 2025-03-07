#indexing = accessing elements of a sequence using [] (indexing operator
#  [start : end : step]

credit_number = "1234-4556-78790-1234"

#print(credit_number[2])
#print(credit_number[0:4])
#print(credit_number[5:10])
#print(credit_number[5:])

#print(credit_number[-4])
#print(credit_number[::3])
last_digits = credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}")

