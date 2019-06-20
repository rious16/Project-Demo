#Name input
name = input("Please enter your first name (lowercase):")

#name doesn't equal nick ends program
if name != 'nick':
	print("Wrong person, try again")
	exit()
else:
	print(F"Welcome {name.title()}, please choose an option below:")
	print(F"\n\tpython \n\tgo \n\tchef")

#returned typed text
python = ("Python is a basic coding language used in web development and data analytics.  The code is easy to read and is a favorite among new programmers.  Python uses an interpreter, which excutes code one line at a time, causing it to take longer to handle large scale programs.")	
go = ("Go or Golang was developed by Google and is used for system programming, web development and cloud computing.  Go's code is also easy to read and is easier to work with when there are a lot of programmers involved.  Unlike Python, which has several different commands for certain actions, Go uses one command for every action.  A benefit of Go is the fact that it uses a compiler and reads code as a whole which allows it to work much faster.")
chef = ("Chef is an automation platform.  Chef allows the user to maintain and update a vast array of servers from any workstation using code instead of writing and uploading scripts.  Chef is written in Ruby.  From the workstations the user can test new code, launch applications or start and stop services.  This setup also allows the users to easily monitor servers and fix problems quickly.")

#user choice - create a loop within an if statement
print()
print("(At anytime type exit to leave)")
answer = input(f"\nYour choice:")


codes = ['python', 'go', 'chef']

for code in codes:
	if answer == 'python':
		print()
		print(python)
		answer = input(f"\nYour choice:")

	if answer == 'go':
		print()
		print(go)
		answer = input(f"\nYour choice:")

	if answer == 'chef':
		print()	
		print(chef)
		answer = input(f"\nYour choice:")

	if answer == 'exit':
		print(f"\nThank you, Goodbye.")



