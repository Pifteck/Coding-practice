numbers = input("Enter three numbers separated by spaces: ")

numbers = list(map(int, numbers.split()))

print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))
print("Sum of numbers:", sum(numbers))
print("Number of items:", len(numbers))