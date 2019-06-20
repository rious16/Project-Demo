for value in range(1,6):
	print(value)

squares = []
for value in range(1,11):
	square = value ** 2
	squares.append(square)

print(squares)

twenty_list = [value+1 for value in range(0,20)]
print(twenty_list)

big_list = [value+1 for value in range(0,1_000_000)]
#print(big_list)

print(min(big_list))
print(max(big_list))
print(sum(big_list))

power_3=[value**3 for value in range(3,31)]
print(power_3)

my_foods = ['grilled cheese', 'chicken', 'brownies', 'ice cream']
friends_food = my_foods[:]

my_foods.append('cookies')
friends_food.append('sushi')

print("\nMy favorite foods are:")
for food in my_foods:
	print(food.title())

print("\nMy friends favorite foods are:")
for f_food in friends_food:
	print(f_food.title())

	
dimension = (200,50)
print("original dimension:")
for dimension in dimension:
		print(dimension)

dimension = (400,55)
print("\nmodified dimension:")
for dimension in dimension:
	print(dimension)

