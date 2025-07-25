# Working with the following string:

# description = "strings are..."

# make it all uper case
# replace the word "are" to "is"
# print just the word "strings"

description = "strings are..."
description_upper = description.upper()
description_replaced = description_upper.replace("ARE", "IS")
word = description_replaced.split()[0]

print(word)

# Check what is the type of each value, then change it: if it is a string, make it an integer and vice-versa:

bank_balance = '33000'
phone_number = 532287514

print(type(bank_balance))
print(type(phone_number))

print(int(bank_balance))
print(str(phone_number))

# Given the following values:

# x = 5
# y = 10
# z = 0
# word1 = "hello"
# word2 = "world"

# 1. Check if x is less than y and y is greater than z.

# 2. Verify if word1 is not equal to word2.

# 3. Use the bool() function to check the boolean value of z and word1.

x = 5
y = 10
z = 0
word1 = 'hello'
word2 = 'world'

cond1 = x < y and y > z
print(cond1)

cond2 = 'word1' != 'word2'
print(cond2)

bool_z = bool(z)
bool_word1 = bool(word1)
print(bool_z)
print(bool_word1)

# You have a friend named Alice, and you want to send her a message with the following details:

# Name: Alice

# Age: 30

# City: New York

# Tasks:

# Use f-strings to print a message saying:

# "Hello, Alice! You are 30 years old and live in New York."

# Use str.format() to print the same message.

name = 'Alice'
age = 30
city = 'New York'

print(f"Hello, {name}! You are {age} years old and live in {city}.")

# Ask the user for their age using the input() function and store it in a variable age.

# Convert the inputted age into an integer and calculate the number of years until they turn 100.

# Display a message: "You will turn 100 in X years", where X is the number of years calculated.

 