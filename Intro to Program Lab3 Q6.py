import math

def byte_converter(bytes):
    units = ("B", "KB", "MB", "GB")
    for i in range(len(units)):
        b = bytes / math.pow(1024,i)
        print(f"{b} {units[i]}")

user_input = int(input("Please enter the number of bytes: "))
byte_converter(user_input)