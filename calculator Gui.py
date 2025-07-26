from tkinter import *
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.set(result)
        except Exception as e:
            entry.set("Error")
    elif text == "C":
        entry.set("")
    else:
        entry.set(entry.get() + text)

# Create main window
root = Tk()
root.geometry("300x400")
root.title("Simple Calculator")

entry = StringVar()
entry.set("")

# Entry display
entry_field = Entry(root, textvar=entry, font="Arial 20 bold")
entry_field.pack(fill=X, ipadx=8, pady=10, padx=10)

# Button layout
btns = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

for row in btns:
    frame = Frame(root)
    for btn_text in row:
        btn = Button(frame, text=btn_text, font="Arial 18", width=5, height=2)
        btn.pack(side=LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", click)
    frame.pack()

root.mainloop()
