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

# Set application color
root.configure(bg = '#abc4ff')

# Set fixed application window size
root.geometry("250x325")
root.resizable(False, False)

# Create function to get a new password
def get_password(widget):
	# Insert new password on a new line
    widget.config(state = 'normal')
    widget.insert(tk.END, generate_password() + "\n")
    widget.config(state = 'disabled')

    # if the new password goes beyond the text box, scroll down 
    widget.see(tk.END)

# Create widget to insert passwords
text_widget = tk.Text(root, height = 15, width = 20, padx = 10)
text_widget.config(bg = '#f5eadd')
text_widget.pack(pady = 5)

# Create a password that call a function to insert a newly generated password to the text widget
button = tk.Button(root, pady = 10, text = "New Password", command = lambda:get_password(text_widget))
button.config(width = root.winfo_screenwidth(), bg = '#809bce')
button.pack(pady = 15, side = tk.BOTTOM)

# Tkinter event loop
root.mainloop()
