#question 1 
num_list = []
num_list2 = []
#this for loop gives me the list of numbers that are divisible by 9 that are between 2000 and 4000
for x in range(2000,4001):
    if x % 9 == 0:
        num_list.append(x)
#this for loops gives me the list of numbers that are divisible by 9 AND divisible by 2 (if n is divisible by 2, it is also a multiple of 2)
#i want divisible by 9 but not multiple of 2, so will use set() and compare difference
for num in num_list:
    if num % 2 == 0:
        num_list2.append(num)

num_list3 = set(num_list).difference(set(num_list2))
print(num_list3)