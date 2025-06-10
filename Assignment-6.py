from tkinter import*
window = Tk()
window.title("CALCULATOR USING TKINTER")
window.geometry("300x550")
window.configure(background="black")

entry_display = Entry(window,font=('Arial', 32, 'bold'),borderwidth=10,relief ="sunken",justify ='right',bg="white",fg="black" )
entry_display.pack(pady=20, padx=20, fill='x')

def on_button_click(value):
    current = entry_display.get()
    entry_display.delete(0,END)
    entry_display.insert(0, current + value)

def on_clear_click():
    entry_display.delete(0,END)

def on_backspace_click():
    current = entry_display.get()
    entry_display.delete(0,END)
    entry_display.insert(0, current[:-1])

def on_equal_click():
    try:
        result = eval(entry_display.get())
        entry_display.delete(0,END)
        entry_display.insert(0, str(result))
    except Exception as e:
        entry_display.delete(0,END)
        entry_display.insert(0, "Error")


button_frame = Frame(window, bg="white")
button_frame.pack(padx=20, pady=10)

buttons = [('C', 0, 0, 2), ('←', 0, 2), ('/', 0, 3), ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),('0', 4, 0, 2), ('.', 4, 2), ('=', 4, 3)]

for (text, row, col, *spans) in buttons:
    columnspan = spans[0] if spans else 1

    if text.isdigit() or text == '.':
        action = lambda x=text: on_button_click(x)
        btn_bg = "black"
    elif text in ['/', '*', '-', '+']:
        action = lambda x=text: on_button_click(x)
        btn_bg = "blue"
    elif text == 'C':
        action = on_clear_click
        btn_bg = "red"
    elif text == '←':
        action = on_backspace_click
        btn_bg = "purple"
    elif text == '=':
        action = on_equal_click
        btn_bg = "green"

    button = Button(button_frame,text=text,font=('Arial', 18),command=action,bg=btn_bg,fg="white",relief=FLAT,borderwidth=0)

    button.grid(row=row, column=col, columnspan=columnspan, sticky="nsew", padx=5, pady=5, ipady=15)

window.mainloop()
