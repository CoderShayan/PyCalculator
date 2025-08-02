import tkinter

import math

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]   #2D list for buttons in calculator

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]
sqrt_symbol = ["√"]

row_count = len(button_values) #5
column_count = len(button_values[0]) #4

#color used in app
color_gray = "#2F2F2C"
color_light_gray = "#636363"
color_dark_gray = "#141414"
color_black = "#1C1C1C"
color_orange = "#FF9500"
color_white = "white"

#windows setup
window = tkinter.Tk()   #create a window
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 40),background=color_black, 
                      foreground=color_white, anchor="e", width=column_count)   #anchor="e" means text will be aligned to the right 

label.grid(row=0, column=0, columnspan=column_count, sticky="we")   #sticky="we" means the label will expand to fill the width of the grid cell
for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                width=column_count-1, height=1, 
                                command=lambda value=value: button_clicked(value))  #lambda function is used to pass the value of button clicked
        
        if value in top_symbols:
            button.config(foreground=color_white, background=color_dark_gray)   #top symbols button background color
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)   #right symbols button background color
        else:
            button.config(foreground=color_white, background=color_gray)   #other buttons background color
                
        button.grid(row=row+1, column=column)   #+1 because first row is label

frame.pack()

#A+B, A-B,A*B, A/B
A = "0"
operator = None
B = None

#square root()
def sqrt(num):
    num = math.sqrt(num)
    return(num)

def clear_all():
    global A,B,operator
    A = "0"
    operator = None
    B = None
    
def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)

def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator
    
    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                
                elif operator == "×":
                    label["text"] = remove_zero_decimal(numA * numB)
                
                elif operator == "÷":
                    try:
                        label["text"] = remove_zero_decimal(numA / numB)
                    except ZeroDivisionError:
                        label["text"] = "Error"

                clear_all()

        elif value in "+-×÷":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"
                
                operator = value
    
    elif value in sqrt_symbol:
        try:
            num = float(label["text"])
            temp_result = sqrt(num)
            result = round(temp_result, 5)
            label["text"] = remove_zero_decimal(result)
            clear_all()
        except Exception:
            label["text"] = "Error"
    
    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
            
        elif value == "%":
            result = float(label["text"]) / 100 
            label["text"] = remove_zero_decimal(result)
        
    else:   #digits or . 
        if value == ".":
            if value not in label["text"]:
                label["text"] += value

        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value   #replace 0
            else:
                label["text"] += value    #append digit

#center the window
window.update()     #update the window the new size dimensions
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#fomat "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")    #set the position of the window

window.mainloop() #start the main loop of the app