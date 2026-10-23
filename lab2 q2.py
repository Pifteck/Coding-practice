x = 70
h = 25
y = input("Please enter three numbers separated by a space: ").split()
#print(y)
if len(y) != 3: #checking if the input is exactly three items
    print("Please enter three numbers")
if not all(num.isdigit() for num in y): #checking that the input is all numbers
    print("Please enter three INTEGERS")

#doing the calculation and rounding it so it is an integer
r = []
for num in y:
    r.append(round((3*x*int(num)/h)**0.5))

print(r)
