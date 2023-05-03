import tkinter as tk

def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):
    return num1 / num2

def exponentiation_numbers(num1, num2):
    return num1 ** num2

def division_without_remainder_numbers(num1, num2):
    return num1 // num2

def division_by_modulus_numbers(num1, num2):
    return num1 % num2

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()

    if operation == '+':
        result = add_numbers(num1, num2)
    elif operation == '-':
        result = subtract_numbers(num1, num2)
    elif operation == '*':
        result = multiply_numbers(num1, num2)
    elif operation == '/':
        result = divide_numbers(num1, num2)
    elif operation == '**':
        result = exponentiation_numbers(num1, num2)
    elif operation == '//':
        result = division_without_remainder_numbers(num1, num2)
    elif operation == '%':
        result = division_by_modulus_numbers(num1, num2)
    else:
        result = 'Ошибка: неверная операция, попробуйте снова!'

    result_label.configure(text=result)

window = tk.Tk()
window.title('Калькулятор')

entry1 = tk.Entry(window, width=10)
entry1.pack(side='left')

operation_var = tk.StringVar()
operation_choices = ['+', '-', '*', '/', '**', '//', '%']
operation_var.set(operation_choices[0])

operation_menu = tk.OptionMenu(window, operation_var, *operation_choices)
operation_menu.pack(side='left')

entry2 = tk.Entry(window, width=10)
entry2.pack(side='left')

button = tk.Button(window, text='Вычислить', command=calculate)
button.pack(side='left')

result_label = tk.Label(window, width=10)
result_label.pack(side='left')

window.mainloop()
