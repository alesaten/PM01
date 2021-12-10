from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as mb


def monthly_charge_calculation():
    # очистка полей вывода суммы кредита с процентами и ежемесячного платежа для избежания слияния значений
    monthly_charge_entry.delete(0, END)
    amount_with_interest_entry.delete(0, END)

    try:
        # получение значений из полей
        amount_value = amount.get()
        credit_interest_rate_value = credit_interest_rate.get()
        loan_term_value = loan_term.get()

        # высчитывание ежемесячного платежа и суммы кредита с процентами и округление их значений
        monthly_charge_value = round((amount_value + amount_value / 100 * credit_interest_rate_value) / loan_term_value)
        amount_with_interest_value = round(monthly_charge_value * loan_term_value)

        # вывод значений в соотвествующие поля
        monthly_charge_entry.insert(0, monthly_charge_value)
        amount_with_interest_entry.insert(0, amount_with_interest_value)

        # создание или открытие файла для записи суммы кредита, количества месяцев, ставки, суммы кредита с процентами и
        # ежемесячного платежа
        accounting = open('monthly_charge_calculation_accounting.txt', 'a+')
        accounting.write(f"Сумма кредита: {amount_value}. Количество месяцев: {loan_term_value}. Ставка: "
                         f"{credit_interest_rate_value}.\nСумма кредита с процентами: {amount_with_interest_value}. "
                         f"Ежемесячный платёж: {monthly_charge_value}.\n")
        accounting.close()

    # отлов ошибок, которые могут возникнуть во время работы
    except TclError:
        mb.showerror("Ошибка", "Вводите только целочисленные значения!")
        clear_entries()

    except ZeroDivisionError:
        mb.showerror("Ошибка", "Данная программа не предусматривает деление на ноль.")
        clear_entries()


def clear_entries():
    # очистка используемых для расчёта полей
    amount_entry.delete(0, END)
    loan_term_entry.delete(0, END)
    credit_interest_rate_entry.delete(0, END)
    monthly_charge_entry.delete(0, END)
    amount_with_interest_entry.delete(0, END)


monthly_charge_app = Tk()
monthly_charge_app.title("Расчёт ежемесячного платежа")
monthly_charge_app.geometry("350x300")

# создание заголовка и поля ввода для указания суммы кредита
amount = IntVar()
amount.set("")
amount_label = Label(monthly_charge_app, text="Введите сумму кредита:")
amount_label.grid(row=0, column=0, padx=10, pady=15, sticky="w")
amount_entry = Entry(monthly_charge_app, textvariable=amount)
amount_entry.grid(row=0, column=1, sticky="w")

# создание заголовка и поля ввода для указания срока кредита в месяцах
loan_term = IntVar()
loan_term.set("")
loan_term_label = Label(monthly_charge_app, text="Введите количество месяцев:")
loan_term_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
loan_term_entry = Entry(monthly_charge_app, textvariable=loan_term)
loan_term_entry.grid(row=1, column=1, sticky="w")

# создание заголовка и поля ввода для кредитной ставки
credit_interest_rate = IntVar()
credit_interest_rate.set(18)
credit_interest_rate_label = Label(monthly_charge_app, text="Заданная ставка:")
credit_interest_rate_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
credit_interest_rate_entry = Entry(monthly_charge_app, textvariable=credit_interest_rate)
credit_interest_rate_entry.grid(row=2, column=1, sticky="w")

# заполнение третьей и шестой строки пустыми заголовками
# данная часть кода несёт в себе косметический характер
absent_label = Label(monthly_charge_app)
absent_label.grid(row=3)
another_absent_label = Label(monthly_charge_app)
another_absent_label.grid(row=6)

# создание заголовка и поля для вывода суммы кредита с процентами
amount_with_interest = IntVar()
amount_with_interest.set("")
amount_with_interest_label = Label(monthly_charge_app, text="Сумма кредита с процентами:")
amount_with_interest_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
amount_with_interest_entry = Entry(monthly_charge_app, textvariable=amount_with_interest)
amount_with_interest_entry.grid(row=4, column=1, sticky="w")

# создание заголовка и поля для вывода ежемесячного платежа
monthly_charge = IntVar()
monthly_charge.set("")
monthly_charge_label = Label(monthly_charge_app, text="Ежемесячный платёж:")
monthly_charge_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
monthly_charge_entry = Entry(monthly_charge_app, textvariable=monthly_charge)
monthly_charge_entry.grid(row=5, column=1, sticky="w")

# создание кнопки для запуска функции расчёта ежемесячного платежа
calculation_button = Button(monthly_charge_app, text="Рассчитать", command=monthly_charge_calculation)
calculation_button.grid(row=7, column=0)

# создание кнопки для очистки полей
clear_button = Button(monthly_charge_app, text="Очистить", command=clear_entries)
clear_button.grid(row=7, column=1)

monthly_charge_app.mainloop()
