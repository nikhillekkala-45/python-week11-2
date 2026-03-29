from tkinter import *
root = Tk()
def show():
    user_text = Name.get()  
    if user_text.strip() == "":
        output_label.config(text="Please Enter Some Text", fg="pink")
    else:
        output_label.config(text=f"You Entered: {user_text}", fg="green")
root.title('Hello World')
root.geometry('300x250')
label = Label(root, text='Name', bg='black', fg='white')
label.grid(row=0, column=0, padx=10, pady=10)
Name = Entry(root)
Name.grid(row=0, column=1, padx=10, pady=10)
submit_btn = Button(root, text='Submit', bg='blue', fg='white', command=show)
submit_btn.grid(row=1, column=1, pady=10)
output_label = Label(root, text="", font=("Arial", 12))
output_label.grid(row=2, column=0, columnspan=2, pady=20)
root.mainloop()

