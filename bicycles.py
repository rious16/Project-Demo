#SR 6/17/19 - creating and modify lists
'''bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[-1].upper())


#append
bicycles.append('schwin')
print(bicycles)

message_bike = f"My first bicycle was a {bicycles[-1].title()}."
print(message_bike)'''

cars = []
cars.append('honda')
cars.append('toyota')
cars.append('geo')
cars.append('ford')
cars.insert(0,'GMC')



#popped
'''popped_cars = cars.pop()
print(cars)
print(popped_cars)

last_owned = cars.pop()
print(f'The last car I owned was a {last_owned.title()}.')

first_owned = cars.pop(0)
print(f'The first car I owned was a {first_owned.title()}.')
print(cars)'''

#sort
'''cars.remove('ford')
print(cars)

too_expensive = 'GMC'
cars.remove(too_expensive)
print(cars)
print(f'\nA {too_expensive.upper()} is too expensive.')'''
'''cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)'''

#sorted
'''print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
'''

#reverse
print(cars)

cars.reverse()
print(cars)

#Looping using for
for car in cars:
	print(f"The {car.title()} was very expensive,")
#^needs to be indented??
	print(f"because the {car} was so fast!\n")


