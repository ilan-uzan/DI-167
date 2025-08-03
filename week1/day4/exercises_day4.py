# 🌟 Exercise 1: Favorite Numbers
# Key Python Topics:

# Sets
# Adding/removing items in a set
# Set concatenation (using union)


# Instructions:

# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

#create a set
my_fav_numbers = {1, 5, 9, 12}
#add2 numbers 
my_fav_numbers.update([2, 7])
#remove last number
my_fav_numbers.remove(12)
#create new set
friends_fav_number = {3, 6, 8, 10}
#populate it 
print(my_fav_numbers, friends_fav_number)
#concarenate
our_fav_numbers = my_fav_numbers.union(friends_fav_number)
print(our_fav_numbers)


# 🌟 Exercise 2: Tuple
# Key Python Topics:

# Tuples (immutability)


# Instructions:

# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.

# we cannot add more integeres to rhe tuple 


# 🌟 Exercise 3: List Manipulation
# Key Python Topics:

# Lists
# List methods: append, remove, insert, count, clear

# Instructions:

# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
basket.remove("Banana")
print('Banana removed', basket)
basket.remove("Blueberries")
print('blueberries removed', basket)
basket.append("Kiwi")
print('added kiwi at the end of the list', basket)
basket.insert( 0, 'Apples')
print('added apples at the begining of the list', basket)
apples_count = basket.count('Apples')
print('number of apples: ', apples_count)
basket.clear()
print('emptied the basket:', basket)

# 🌟 Exercise 4: Floats
# Key Python Topics:

# Lists
# Floats and integers
# Range generation


# Instructions:

# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

list = []
value = 1.5

while value <= 5:
    list.append(value)
    value += 0.5

print(list)

# 🌟 Exercise 5: For Loop
# Key Python Topics:

# Loops (for)
# Range and indexing


# Instructions:

# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

for i in range(1, 21):
    print(i)

for i in range(2, 21):
    if i % 2 == 0:
        print(i)


# 🌟 Exercise 6: While Loop
# Key Python Topics:

# Loops (while)
# Conditionals


# Instructions:

# Write a while loop that keeps asking the user to enter their name.
# Stop the loop if the user’s input is your name.

name = 'ilan'
user = str(input('Enter your first guess: '))
           
while user != name:
    user = str(input('Enter your guess: '))
else:
    print('We have the same name')



# 🌟 Exercise 7: Favorite Fruits
# Key Python Topics:

# Input/output
# Strings and lists
# Conditionals


# Instructions:

# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

favFruits = str(input('Enter your favourite fruits seperated by spaces: ')) #Banana Apple Pear
favFruits.split()

aFruit = str(input('Input the name of a fruit: '))

if aFruit in favFruits:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy it!')



# 🌟 Exercise 8: Pizza Toppings
# Key Python Topics:

# Loops
# Lists
# String formatting


# Instructions:

# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

################################################
toppings = []
basePrice = 10
toppingPrice = 2.5
numOfToppings = 0

print('Enter your toppings. Write quit to get out')
user_input = (input('Add Topping: '))

while (input != 'quit'):
    toppings.append(input)
    print(f'Adding {input} to your pizza')
    user_input = input('Add Topping: ')

output = 'Your toppings are: '
for topping in toppings:
    output.append(topping + ' ')
    numOfToppings += 1


totalCost = (basePrice + (toppingPrice * numOfToppings))
output.append(f'Your total cost is: {totalCost}')

print(output)

  ##############################################  



# 🌟 Exercise 9: Cinemax Tickets
# Key Python Topics:

# Conditionals
# Lists
# Loops


# Instructions:

# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

#first lets figure out how many people they have in their fam
num_people = int(input('how many people in your family? '))
#initial cost
total_cost = 0
#loop for the price per age of each person 
for i in range(num_people):
    age = int(input(f'Enter your age #{i+1}: '))

    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
    
    total_cost += ticket_price

    print('Total ticket cost: ', total_cost)


# Bonus:

# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.

#find out how many people
num_teenagers = int(input('How many of you are watching the movie? '))
#store the teenagers in a list
teenagers = []
#for loop to add eligible teenagers to the list
for i in range(num_teenagers):
    age = int(input(f'how old are you #{i+1}? '))

    if 16 <= age <= 21:
        teenagers.append(age) #add to the list
    else:
        print('sorry only people aged between 16 and 21 can watch')

print('\nfinal list of teens: ')
print(teenagers)
print(f'total teens who can watch: {len(teenagers)}')







# 🌟 Exercise 10: Sandwich Orders
# Key Python Topics:

# Lists
# Loops (while)


# Instructions:

# Using the list:
# sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
# The deli has run out of “Pastrami”, so use a loop to remove all instances of “Pastrami” from the list.
# Prepare each sandwich, one by one, and move them to a list called finished_sandwiches.
# Print a message for each sandwich made, such as: "I made your Tuna sandwich."
# Print the final list of all finished sandwiches.

sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]

#remove pastrami from the list
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

#create a new list
finished_sandwiches = []
#transfer sandwiches to the new list
while sandwich_orders:
    current_sandwiches = sandwich_orders.pop(0)
    print(f'I made your {current_sandwiches} sandwich')
    finished_sandwiches.append(current_sandwiches)

print('\nAll sandwiches made: ')
for sandwich in finished_sandwiches:
    print(f'- {sandwich}')