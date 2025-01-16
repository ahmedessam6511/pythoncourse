import tkinter as tk

def button_click():
    print("Button Clicked!!!!!")
    print('current value is %s' % name.get())
    name.delete(0,'end')          # delete between two indices, 0-based
    name.insert(0, 'your name')   # insert new text at a given index


root = tk.Tk()
root.title("TKinter Application")

button = tk.Button(root, text="Click Me", command=button_click)
button.pack()

# button.state(['disabled'])          # set the disabled flag
# button.state(['!disabled'])         # clear the disabled flag

label = tk.Label(root, text = "Your First Project").place(x = 12 , y = 50)

# resultsContents = tk.StringVar()
# # label['textvariable'] = resultsContents
# resultsContents.set('New value to display')

# image = PhotoImage(file='myimage.gif')
# label['image'] = image

name = tk.Entry(root, textvariable=tk.StringVar())
name.pack()

country = tk.OptionMenu(root, textvariable=tk.StringVar(), )


root.mainloop()