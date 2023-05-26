import tkinter as tk

window = tk.Tk()
window.title('calc')
window.geometry('547x629')
window.resizable(False, False)
window.configure(bg = 'light blue')

def calc(op):
    global formula
    if op == 'C':
        formula = ''
    elif op == ';-)':
        pass
    elif op == 'D':
        formula = formula[0:-1]
    elif op == '=':
        formula = str(eval(formula))
    else:
        if len(formula) < 19:
            formula += op
    result_lable.configure(text = formula)

formula = ''
result_lable = tk.Label(text = formula, font = ('Arial', 35), bg = 'light blue')
result_lable.place(x=25, y=60)

button_list = [';-)', 'C', 'D', '/', '7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+', '+/-', '0', '.', '=']
x = 10
y = 175

for button in button_list:
    get_op = lambda x = button: calc(x)
    tk.Button(text = button, bg = 'light cyan', font = ('Arial', 20), command = get_op).place(x=x, y=y, width = 128, height = 85)
    x += 133
    if x > 500:
       x = 10
       y += 90   

window.mainloop()
