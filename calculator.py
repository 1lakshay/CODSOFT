import tkinter as tk

result = ""

def values(symbol):
    global result
    result += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, result)

def calculate():
    global result
    try:
        result = str(eval(result))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear()
        pass

def clear():
    global result
    result = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("290x220")
root.title("Calculator")
text_result = tk.Text(root, height = 2, width = 26, font =24, bg="light green")
text_result.grid(columnspan=5)
btn_1 = tk.Button(root, text="1", command = lambda : values(1), width=5, font=14)
btn_1.grid(row=2, column=1)      # tells location where this button location will be
btn_2 = tk.Button(root, text="2", command=lambda: values(2), width=5, font=14)
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: values(3), width=5, font=14)
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: values(4), width=5, font=14)
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: values(5), width=5, font=14)
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: values(6), width=5, font=14)
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: values(7), width=5, font=14)
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: values(8), width=5, font=14)
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: values(9), width=5, font=14)
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: values(0), width=5, font=14)
btn_0.grid(row=5, column=1)
btn_plus = tk.Button(root, text="+", command=lambda: values("+"), width=5, font=14)
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: values("-"), width=5, font=14)
btn_minus.grid(row=3, column=4)
btn_multi = tk.Button(root, text="x", command=lambda: values("*"), width=5, font=14)
btn_multi.grid(row=4, column=4)
btn_division = tk.Button(root, text="/", command=lambda: values("/"), width=5, font=14)
btn_division.grid(row=5, column=4)
btn_clear = tk.Button(root, text="C", command=clear, width=5, font=14)
btn_clear.grid(row=5, column=2)
btn_equal = tk.Button(root, text="=", command=calculate, width=5, font=14)
btn_equal.grid(row=5, column=3)
root.mainloop()