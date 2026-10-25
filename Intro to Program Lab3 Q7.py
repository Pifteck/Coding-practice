#part a
numbers = [1,2,3,4,5,6,7,8,9,10]
square = list(map(lambda x: x ** 2, numbers))
even = list(filter(lambda y: y % 2 == 0, square))
print(square)
print(even)

#part b
temperature = [(0, 32), (10, 50), (20, 68), (30, 86)]
even_temp = list(filter(lambda z: z[0] % 2 == 0 and z[1] % 2 == 0, temperature))
sort_temp = list(sorted(even_temp, key=lambda t: t[1], reverse=True))
print(even_temp)
print(sort_temp)