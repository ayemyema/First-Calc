import tkinter

button_values = [
    ["AC", "+/-", "%", "/"],
    ["7", "8", "9", "*"],   
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]
right_symbols = ["/", "*", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count =len(button_values) #5
column_count = len(button_values[0]) #4

color_pink = "#FF1B8D"
color_yellow = "#FFDA00"
color_blue = "#1BB3FF"
color_white = "#FFFFFF"
color_black = "#000000"

#window setup
window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 24), bg=color_black, fg=color_white, width=10, height=2, anchor="e")

label.grid(row=0, column=0, columnspan=4, sticky="we")

def button_clicked(value):
    print(value)

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(
            frame,
            text=value,
            font=("Arial", 20),
            width=5,
            height=2,
            command=lambda value=value: button_clicked(value)
        )
        if value in top_symbols:
            button.config(foreground="black", background=color_pink)
        elif value in right_symbols:
            button.config(foreground="white", background=color_yellow)
        else:
            button.config(foreground="white", background=color_blue)
        button.grid(row=row+1, column=column, padx=3, pady=3)
       
frame.pack()
#A+B, A*B, A/B, A-B, A=B, √A, AC, +/-, %
A = "0" 
operator = None
B = None

def clear_all():
    global A, B, operator
    A = "0"
    B = None
    operator = None
    label["text"] = A

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)


def button_clicked(value):
    global right_symbols, top_symbols, A, B, operator

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                num = float(A)
                num2 = float(B)
                try:
                    if operator == "+":
                        result = num + num2
                    elif operator == "-":
                        result = num - num2
                    elif operator == "*":
                        result = num * num2
                    elif operator == "/":
                        result = num / num2
                    else:
                        result = num2
                    label["text"] = remove_zero_decimal(result)
                    A = label["text"]
                    operator = None
                except Exception:
                    label["text"] = "Error"
        elif value in ["/", "*", "-", "+"]:
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"
                operator = value

    elif value == "AC":
        clear_all()

    elif value == "+/-":
        try:
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        except Exception:
            pass

    elif value == "%":
        try:
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
        except Exception:
            pass

    else:
        if value == ".":
            if "." not in label["text"]:
                label["text"] += value

        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()








