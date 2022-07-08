from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
	Window = Tk()
	Window.withdraw()
	Number = random.randint(0, 3)
	print(Number)
	simpledialog.askstring("Question", "Enter something you think is awesome")
	if Number == 0:
		messagebox.showinfo("Message", "That is awesome")
	elif Number == 1:
		messagebox.showinfo("Message", "That is okay")
	elif Number == 2:
		messagebox.showinfo("Message", "That is boring")
	else:
		messagebox.showinfo("Message", "Shut up")
# Make a new window variable, window = Tk()

# Hide the window using the window's .withdraw() method

# 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)

# 2. Print your variable to the console

# 3. Get the user to enter something that they think is awesome

# 4. If your variable is  0
# -- tell the user whatever they entered is awesome!

# 5. If your variable is  1
# -- tell the user whatever they entered is ok.

# 6. If your variable is  2
# -- tell the user whatever they entered is boring.

# 7. If your variable is  3
# -- invent your own message to give to the user (be nice).

# Run the window's .mainloop() method
