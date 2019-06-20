#SR 6/19/19 Dictionaries
alien_0 = {'color': 'green','points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}

alien_1['color'] = 'red'
alien_1['points'] = 15
print(alien_1)

alien_0['color'] = 'yellow'
print(alien_0)
print( f"The 1st alien color is now {alien_0['color']}.")

alien_0['speed'] = 'slow'
print(alien_0)


#Move alien_0 to the right 
#Use speed to determine how far alien is moved

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien['speed'] == 'medium':
	x_increment = 2
else:
	#Fast alien
	x_increment = 3

#New position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")
#change alien color back to green
alien_0['color'] = 'green'
print(f"The 1st alien color has been changed back to {alien_0['color']}.")
print()
#update 2nd alien
alien_1['speed'] = 'medium'
alien_1['x_position'] = 1
alien_1['y_position'] = 30

#create a new alien
alien_2 = {'color': 'red', 'points': 25, 'speed': 'fast', 'x_position': 2, 'y_position': 35 }

#add dictionaries to a list = 'nesting'

print("These are the different values for eash alien:")
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)

#alternate way
#Make an empty list for storing aliens.
aliens = []

#make 30 aliens
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

#show first 5 aliens
print()

for alien in aliens[:5]:
	print(alien)
print("...")
 
 #show how many aliens were created
print(f"\nTotal number of aliens created: {len(aliens)}")

#use slice to change first 3 aliens to different attributes
print()
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 15
		alien['speed'] = 'medium'
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['points'] = 25
		alien['speed'] = 'fast'

for alien in aliens[:5]:
	print(alien)
