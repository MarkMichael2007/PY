from tkinter import *
from tkinter import messagebox
# First part
def calc():
    try:
        number = int(entry1.get())
    
        result = number * 5
        
        messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# secound part
root = Tk()
root.title("Mark")
root.geometry("600x400")

# Third part

entry1 = Entry(root)
entry1.insert(0, "Enter a Number")
entry1.pack()

# forth part
Bt1 = Button(root, width=10, text="Click", command=calc)
Bt1.pack()

root.mainloop()
