# Import the Tkinter module, a GUI
import tkinter as tk

import random
import string

# Create strong randomly generated password
def generate_password(): 
	# setup lists
	numbers = string.digits
	upp_letters = string.ascii_uppercase
	low_letters = string.ascii_lowercase

	# initialize password list
	password = []

	# Add a random number to the list
	password.append(random.choice(numbers))

	# Add a random upper letter to the list
	password.append(random.choice(upp_letters))

	# Add sixteen random lower letters to the list
	for _ in range(16): 
		password.append(random.choice(low_letters))

	# Shuffle the list to create password
	for _ in range(8): 
		random.shuffle(password)

	# Insert hyphens
	password.insert(6, "-")
	password.insert(13, "-")

	# Return password as a string
	return ''.join(password)


# Initialize Tkinter using a Tk root widget
root = tk.Tk()

# Set application title
root.title("Password Generator")

# Set fixed application window size
root.geometry("500x500")								### CHANGE LATER
root.resizable(False, False)

# Create function to get a new password
def get_password(widget):
	# Insert new password on a new line
    widget.config(state='normal')
    widget.insert(tk.END, "\n" + generate_password())
    widget.config(state='disabled')
    widget.see(tk.END)


text_widget = tk.Text(root, height=10, width=50)
text_widget.pack()

text_widget.insert(tk.END, generate_password())
text_widget.config(state='disabled')


button = tk.Button(root, text = "New Password", command = lambda:get_password(text_widget))
button.pack()


# Tkinter event loop
root.mainloop()
