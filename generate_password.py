import random as rnd
import string as stg

def generate_password(): 
	# setup lists
	numbers = stg.digits
	upp_letters = stg.upper_letters
	low_letters = stg.low_letters

	# initialize password list
	password = []

	# Add a random number to the list
	password.append(rnd.choice(numbers))

	# Add a random upper letter to the list
	password.append(rnd.choice(upp_letters))

	# Add sixteen random lower letters to the list
	for _ in range(16): 
		password.append(rnd.choice(low_letters))

	# Shuffle the list to create password
	for _ in range(8): 
		rnd.shuffle(password)

	# Insert hyphens
	password.insert(6, "-")
	password.insert(13, "-")

	# Return password as a string
	return ''.join(password)