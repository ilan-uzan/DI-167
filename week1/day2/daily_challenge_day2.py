# Instructions:
# 1. Ask for User Input:

string = str(input('Enter a 10 character string: '))

# The string must be exactly 10 characters long.
# 2. Check the Length of the String:

# If the string is less than 10 characters, print: "String not long enough."

if len(string) < 10:
    print('string not long enough')
# If the string is more than 10 characters, print: "String too long."
elif len(string) > 10:
    print('string too long')
# If the string is exactly 10 characters, print: "Perfect string" and proceed to the next steps.
# 3. Print the First and Last Characters:
else:
    print('perfet string')
    print('first character' , string[0])
    print('last character', string[-1])
# Once the string is validated, print the first and last characters.
# 4. Build the String Character by Character:

    print('\nbulding the string step by step: ')
    for i in range (1, len(string) +1):
        print(string[:i])

# Using a for loop, construct and print the string character by character. Start with the first character, then the first two characters, and so on, until the entire string is printed.
# Hint: You can create a loop that goes through the string, adding one character at a time, and print it progressively.

# 5. Bonus: Jumble the String (Optional)

# As a bonus, try shuffling the characters in the string and print the newly jumbled string.
# Hint: You can use the random.shuffle function to shuffle a list of characters.