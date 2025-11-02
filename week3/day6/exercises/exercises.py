# 🌟 Exercise 1: Random Sentence Generator
# Goal: Create a program that generates a random sentence of a specified length from a word list.



# Key Python Topics:

# File handling (open(), read())
# Lists
# Random number generation (random.choice())
# String manipulation (split(), join(), lower())
# Error handling (try, except)
# Input validation


# Instructions:

# Download the provided word list and save it in your development directory.
# Create a function to read the words from the file.
# Create a function to generate a random sentence of a given length.
# Create a main function to handle user input and program flow.


# Step 1: Create the get_words_from_file function

# Create a function named get_words_from_file that takes the file path as an argument.
# Open the file in read mode ("r").
# Read the file content.
# Split the content into a list of words.
# Return the list of words.


# Step 2: Create the get_random_sentence function

# Create a function named get_random_sentence that takes the sentence length as an argument.
# Call get_words_from_file to get the list of words.
# Select a random word from the list length times.
# Create a sentence with the selected words.
# Convert the sentence to lowercase.
# Return the sentence.


# Step 3: Create the main function

# Create a function named main.
# Print a message explaining the program’s purpose.
# Ask the user for the desired sentence length.
# Validate the user input:
# Check if it is an integer.
# Check if it is between 2 and 20 (inclusive).
# If the input is invalid, print an error message and exit.
# If the input is valid, call get_random_sentence with the length and print the generated sentence.

import os
import sys
import random

words_file = os.path.join(os.path.dirname(__file__), 'words.txt')

def get_words_from_file(file_path):
    '''Read words from fgile and return a list of words.'''
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f'Error: words file not found at: {file_path}')
        return []
    except Exception as e:
        print(f'Error reading words file: {e}')
        return []
    
    words = content.split()
    return words

def get_random_sentence(length):
    '''Generate a random sentence of given length using words from the words file.'''
    words = get_words_from_file(words_file)
    if not words:
        print('No words available to generate a sentence')
        return ''
    
    chosen = [random.choice(words) for _ in range(length)]
    sentence = ' '.join(chosen).lower()
    return sentence

def main():
    print("Random Sentence Generator — creates a sentence from a word list.")
    user_input = input("Enter desired sentence length (integer between 2 and 20): ").strip()

    try:
        n = int(user_input)
    except ValueError:
        print("Invalid input: please enter an integer.")
        sys.exit(1)

    if not (2 <= n <= 20):
        print("Invalid input: number must be between 2 and 20 (inclusive).")
        sys.exit(1)

    sentence = get_random_sentence(n)
    if sentence:
        print("\nGenerated sentence:")
        print(sentence)


if __name__ == "__main__":
    main()
    
    
# 🌟 Exercise 2: Working with JSON
# Goal: Access a nested key in a JSON string, add a new key, and save the modified JSON to a file.



# Key Python Topics:

# JSON parsing (json.loads())
# JSON serialization (json.dump())
# Dictionaries
# File handling (open())


# Instructions:

# Using the follow code:
# Access the nested “salary” key.
# Add a new key “birth_date” wich value is of format “YYYY-MM-DD”, to the “employee” dictionary: "birth_date": "YYYY-MM-DD".
# Save the modified JSON to a file.


# Step 1: Load the JSON string

# Import the json module.
# Use json.loads() to parse the JSON string into a Python dictionary.


# Step 2: Access the nested “salary” key

# Access the “salary” key using nested dictionary access (e.g., data["company"]["employee"]["payable"]["salary"]).
# Print the value of the “salary” key.


# Step 3: Add the “birth_date” key

# Add a new key-value pair to the “employee” dictionary: "birth_date": "YYYY-MM-DD".
# Replace "YYYY-MM-DD" with an actual date.


# Step 4: Save the JSON to a file

# Open a file in write mode ("w").
# Use json.dump() to write the modified dictionary to the file in JSON format.
# Use the indent parameter to make the JSON file more readable.


import json

def run_exercise_2():
    """Solve Exercise 2: parse JSON, print salary, add birth_date, save to file."""
    sampleJson = """{ 
       "company":{ 
          "employee":{ 
             "name":"emma",
             "payable":{ 
                "salary":7000,
                "bonus":800
             }
          }
       }
    }"""

    # Load JSON string into Python dict
    data = json.loads(sampleJson)

    # Access nested salary
    salary = data["company"]["employee"]["payable"]["salary"]
    print(f"Salary found: {salary}")

    # Add birth_date to employee
    data["company"]["employee"]["birth_date"] = "1990-01-01"

    # Save modified JSON to a file next to this script
    out_path = os.path.join(os.path.dirname(__file__), "modified_employee.json")
    try:
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"Modified JSON saved to: {out_path}")
    except Exception as e:
        print(f"Error saving JSON file: {e}")
# ...existing code...
{ changed code }
if __name__ == "__main__":
    # run exercise 2 if script called with 'ex2' argument: `python exercises.py ex2`
    if len(sys.argv) > 1 and sys.argv[1] == "ex2":
        run_exercise_2()
    else:
        main()