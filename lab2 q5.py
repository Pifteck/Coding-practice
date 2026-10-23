import math

user_string = input("Please enter a string: ")
half = math.floor(len(user_string)/2) #working out the mid point of the string
#print(half)
first_half = []
second_half = []
#then i split get the first half of the string and the second half without the midpoint
for i in range(0,len(user_string)):
    if i < half:
        first_half.append(user_string[i])
    elif i > half:    
        second_half.append(user_string[i])

second_half.reverse() #reverse the second half so i can compare
#compare the halfs, if equal then palindrome
if first_half == second_half:
    print("This string is a palindrome")
else:
    print("This string is not a palindrome")
