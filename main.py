# Importing the random module to randomly select characters for the password
import random

# Lists of characters that can be used in the password
# These lists contain lowercase and uppercase letters, numbers, and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message
print("Welcome to the PyPassword Generator!\n")

# Taking user input for the number of letters, symbols, and numbers
# The user specifies how many characters of each type they want in the password
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Initialize an empty list to store the password characters
password = []

# Add the specified number of random letters to the password
for i in range(0, nr_letters):
  password.append(random.choice(letters))

# Add the specified number of random symbols to the password
for i in range(0, nr_symbols):
  password += random.choice(symbols)

# Add the specified number of random numbers to the password
for i in range(0, nr_numbers):
  password += random.choice(numbers)

# Shuffle the characters in the password list to ensure randomness
random.shuffle(password)

# Convert the list of characters into a single string
password_final = ""
for i in password:
  password_final += i

# Display the final password
print(f"Your password is: {password_final}")
