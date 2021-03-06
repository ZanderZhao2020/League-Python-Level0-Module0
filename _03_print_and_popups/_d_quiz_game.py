from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
	Window = Tk()
	Window.withdraw()
	Score = 0
	if simpledialog.askinteger("Question", "What is 2+2?") == 4:
		Score += 1
		messagebox.showinfo("Message", "Correct")
	else:
		messagebox.showerror("Error", "Wrong")
	if simpledialog.askinteger("Question", "What is 4/2?") == 2:
		Score += 1
		messagebox.showinfo("Message", "Correct")
	else:
		messagebox.showerror("Error", "Wrong")
	simpledialog.askinteger("Question", "What is the square root of \"a\"?")
	messagebox.showerror("Error", "Wrong")
	messagebox.showinfo("Message", "You got " + str(Score) + " points")
	Window.mainloop()
# Make a new window variable, window = Tk()

# Hide the window using the window's .withdraw() method

# 1. Create a variable to hold the user's score. Set it equal to zero.

# ASK A QUESTION AND CHECK THE ANSWER

#      // 2.  Ask the user a question

#      // 3.  Use an if statement to check if their answer is correct

#      // 4.  if the user's answer was correct, add one to their score

# MAKE MORE QUESTIONS. Ask more questions by repeating the above
#      // Option: Subtract a point from their score for a wrong answer

# After all the questions have been asked, tell the user their final score
# remember to convert your variable to a string using the str() function

# Run the window's .mainloop() method
