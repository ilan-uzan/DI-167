# 🌟 Exercise 1 : Hello World
# Instructions
# Print the following output in one line of code:

# Hello world
# Hello world
# Hello world
# Hello world

print('hello world\nhello world\nhelloworld\nhello world')


# 🌟 Exercise 2 : Some Math
# Instructions
# Write code that calculates the result of:

# (99^3)*8 (meaning 99 to the power of 3, times 8).

answer = (99 ** 3) * 8
print(answer)



# 🌟 Exercise 3 : What is the output ?
# Instructions
# Predict the output of the following code snippets:

# >>> 5 < 3
# >>> 3 == 3
# >>> 3 == "3"
# >>> "3" > 3
# >>> "Hello" == "hello"

#########   false, true, false, error, false   ##########


# 🌟 Exercise 4 : Your computer brand
# Instructions
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable, print a sentence that states the following:
# "I have a <computer_brand> computer."

computer_brand = 'apple'
print(f'I have a {computer_brand} computer.')


# 🌟 Exercise 5 : Your information
# Instructions
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
# Have your code print the info message.
# Run your code.

name = 'ilan'
age = 22
shoe_size = 8.5
info = f'Hi my name is {name} i am {age} my shoe size is {shoe_size} and i love python'
print(info)

# 🌟 Exercise 6 : A & B
# Instructions
# Create two variables, a and b.
# Each variable’s value should be a number.
# If a is bigger than b, have your code print "Hello World".

a = 18
b = 4

if a > b:
    print('hello wolrrd')


# 🌟 Exercise 7 : Odd or Even
# Instructions
# Write code that asks the user for a number and determines whether this number is odd or even.

user_number = int(input('Enter a number: '))

if user_number % 2 == 0:
    print('Even')
else:
    print('Odd')



# 🌟 Exercise 8 : What’s your name ?
# Instructions
# Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.

user_name = str(input('Enter your name: '))
my_name = 'ilan'
if user_name == my_name:
    print('We have the same name')
else: 
    print('We do not have the same name')

# 🌟 Exercise 9 : Tall enough to ride a roller coaster
# Instructions
# Write code that will ask the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride.
# If they are not tall enough, print a message that says they need to grow some more to ride.

height = int(input('Enter your heigh in cm: '))

if height >= 145:
    print('you are tall enough to ride')
else:
    print('You are too short')

##############################################
#non mandatory exercises

# Exercise 1 : Hello World-I love Python
# Instructions
# Print the following output in one line of code:

# Hello world
# Hello world
# Hello world
# Hello world
# I love python
# I love python
# I love python
# I love python

print('hello world\nhello world\nhelloworld\nhello world\nI love python\nI love python\nI love python\nI love python')


# Exercise 2 : What is the Season ?
# Instructions
# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)

month = int(input('enter a month (1-12): '))

if month >= 3 and month <= 5:
    print('spring')
elif month >= 6 and month <= 8:
    print('summer')
elif month >= 9 and month <= 11:
    print('autumn')
else:
    print('winter')