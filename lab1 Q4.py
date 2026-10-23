#Question 4
print("tis but our fantasy, and will not let belief take hold of him\n\ttouching this dreaded sight, twice seen of us.\n\t\tTherefore, I have entreated him along,\n\twith us to watch the minutes of this night, that, if again\nthis apparition come,\n\nHe may approve our eyes and speak to it")

#Question 6
#part A
x, y, z = input("Please enter three integers: ").split()
ordernumber = []
if x == y or x == z or y == z:
    print("Please enter three unique integers")
if x > y and x > z:
    ordernumber.append(x)
    if y > z:
        ordernumber.append(y)
        ordernumber.append(z)
    else:
        ordernumber.append(z)
        ordernumber.append(y)
elif y > x and y > z:
    ordernumber.append(y)
    if x > z:
        ordernumber.append(x)
        ordernumber.append(z)
    else:
        ordernumber.append(z)
        ordernumber.append(x)
elif z > x and z > y:
    ordernumber.append(z)
    if y > x:
        ordernumber.append(y)
        ordernumber.append(x)
    else:
        ordernumber.append(x)
        ordernumber.append(y)
print(ordernumber)

#part B
password = "Password!"
userpassword = input("Please enter your password: ")
if userpassword == password:
    print("Password Accepted!")
else:
    print("Wrong Password")

#part C
grade = input("Please enter your grade: ")
if int(grade) < 49:
    print("Fail")
elif 50 <= int(grade) <=69:
    print("Pass")
elif 70 <= int(grade) <= 100:
    print("Distinction")
else:
    print("Please enter a grade between 0-100!")