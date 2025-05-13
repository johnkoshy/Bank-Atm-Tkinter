# ---------------Program for ATM Machine-------------
from tkinter import *
import tkinter.messagebox as tkmessagebox
import mysql.connector
import random

window = Tk()
window.title("SBI - ATM")
window.geometry("800x750")
window.iconbitmap('sbi.ico')

# ---------------Variables-------------


USERNAME = StringVar()
PASSWORD = StringVar()
AADHAAR_NUMBER = StringVar()
FIRST_NAME = StringVar()
LAST_NAME = StringVar()
AGE = StringVar()
ADDRESS = StringVar()
BALANCE = StringVar()
DEPOSIT = StringVar()
WITHDRAWAL = StringVar()
NET_BALANCE = StringVar()
ACCOUNT_NUMBER = StringVar()
AC_NUMBER = StringVar()
CUSTOMER_NAME = StringVar()

# ---------------Methods-------------


def database():
    global mycursor, mydb
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bank"
    )
    mycursor = mydb.cursor()


def exit_window():
    result = tkmessagebox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        window.destroy()
        exit()


def login_form():
    global LoginFrame, lbl_login_result
    LoginFrame = Frame(window)
    LoginFrame.pack(side=TOP, pady=80)
    USERNAME.set("")
    PASSWORD.set("")
    lbl_username = Label(LoginFrame, text="Username:", font=('arial', 15), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(LoginFrame, text="Password:", font=('arial', 15), bd=18)
    lbl_password.grid(row=2)
    lbl_login_result = Label(LoginFrame, text="", font=('arial', 18))
    lbl_login_result.grid(row=3, columnspan=2)
    username = Entry(LoginFrame, font=('arial', 15), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    username.focus_set()
    password = Entry(LoginFrame, font=('arial', 15), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    btn_login = Button(LoginFrame, text="Login", font=('arial', 18), width=35, command=login)
    btn_login.grid(row=4, columnspan=2, pady=20)
    btn_login.bind('<Return>', login)
    lbl_register = Label(LoginFrame, text="Register", fg="Blue", font=('arial', 12))
    lbl_register.grid(row=0, sticky=W)
    lbl_register.bind('<Button-1>', toggle_to_register)


def register_form():
    global RegisterFrame, lbl_register_result
    RegisterFrame = Frame(window)
    RegisterFrame.pack(side=TOP, pady=20)
    USERNAME.set("")
    PASSWORD.set("")
    lbl_username = Label(RegisterFrame, text="Username:", font=('arial', 8), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(RegisterFrame, text="Password:", font=('arial', 8), bd=18)
    lbl_password.grid(row=2)
    lbl_aadhaar_number = Label(RegisterFrame, text="Aadhaar Number:", font=('arial', 8), bd=18)
    lbl_aadhaar_number.grid(row=4)
    lbl_first_name = Label(RegisterFrame, text="First Name:", font=('arial', 8), bd=18)
    lbl_first_name.grid(row=5)
    lbl_last_name = Label(RegisterFrame, text="Last Name:", font=('arial', 8), bd=18)
    lbl_last_name.grid(row=6)
    lbl_age = Label(RegisterFrame, text="Age:", font=('arial', 8), bd=18)
    lbl_age.grid(row=7)
    lbl_address = Label(RegisterFrame, text="Address:", font=('arial', 8), bd=18)
    lbl_address.grid(row=9)
    lbl_deposit_amount = Label(RegisterFrame, text="Deposit Amount:", font=('arial', 8), bd=18)
    lbl_deposit_amount.grid(row=10)
    lbl_register_result = Label(RegisterFrame, text="", font=('arial', 8))
    lbl_register_result.grid(row=11, columnspan=2)
    username = Entry(RegisterFrame, font=('arial', 8), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    username.focus_set()
    password = Entry(RegisterFrame, font=('arial', 8), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    aadhaar_number = Entry(RegisterFrame, font=('arial', 8), textvariable=AADHAAR_NUMBER,
                           validate='key', validatecommand=(window.register(validate_aadhaar), "%P"))
    aadhaar_number.grid(row=4, column=1)
    first_name = Entry(RegisterFrame, font=('arial', 8), textvariable=FIRST_NAME, width=15)
    first_name.grid(row=5, column=1)
    last_name = Entry(RegisterFrame, font=('arial', 8), textvariable=LAST_NAME, width=15)
    last_name.grid(row=6, column=1)
    age = Entry(RegisterFrame, font=('arial', 8), textvariable=AGE,
                validate='key', validatecommand=(window.register(validate_age), "%P"))
    age.grid(row=7, column=1)
    address = Entry(RegisterFrame, font=('arial', 8), textvariable=ADDRESS, width=15)
    address.grid(row=9, column=1)
    deposit_amt = Entry(RegisterFrame, font=('arial', 8), textvariable=DEPOSIT,
                        validate='key', validatecommand=(window.register(validate_deposit), "%P"))
    deposit_amt.grid(row=10, column=1)
    btn_register = Button(RegisterFrame, text="Register", font=('arial', 18), width=35, command=register)
    btn_register.grid(row=12, columnspan=2, pady=20)
    btn_register.bind('<Return>', register)
    lbl_login = Label(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
    lbl_login.grid(row=0, sticky=W)
    lbl_login.bind('<Button-1>', toggle_to_login)


def selection_form():
    global SelectionFrame
    SelectionFrame = Frame(window)
    SelectionFrame.pack(side=TOP, pady=40)
    lbl_select = Label(SelectionFrame, text="Please make a selection:", font=('arial', 15), bd=18)
    lbl_select.grid(row=1)
    btn_deposit = Button(SelectionFrame, text="Deposit", font=('arial', 15), bd=18, command=toggle_to_deposit)
    btn_deposit.grid(row=2)
    btn_withdraw = Button(SelectionFrame, text="Withdraw", font=('arial', 15), bd=18, command=toggle_to_withdrawal)
    btn_withdraw.grid(row=3)
    btn_balance = Button(SelectionFrame, text="Balance", font=('arial', 15), bd=18, command=s_toggle_to_balance)
    btn_balance.grid(row=4)
    btn_balance = Button(SelectionFrame, text="Exit", font=('arial', 15), bd=18, command=exit_to_login)
    btn_balance.grid(row=5)


def deposit_form():
    global DepositFrame, lbl_deposit_result, lbl_current_balance
    DepositFrame = Frame(window)
    DepositFrame.pack(side=TOP, pady=80)
    lbl_deposit_amount = Label(DepositFrame, text="Enter the deposit amount:", font=('arial', 15), bd=18)
    lbl_deposit_amount.grid(row=1)
    deposit_amt = Entry(DepositFrame, font=('arial', 18), textvariable=DEPOSIT, width=15)
    deposit_amt.grid(row=1, column=1)
    deposit_amt.focus_set()
    DEPOSIT.set("")
    lbl_deposit_result = Label(DepositFrame, text="", font=('arial', 18))
    lbl_deposit_result.grid(row=3, columnspan=2)
    btn_deposit = Button(DepositFrame, text="Deposit", font=('arial', 18), width=35, command=deposit)
    btn_deposit.grid(row=12, columnspan=2, pady=20)
    btn_balance = Button(DepositFrame, text="Balance", font=('arial', 18), width=35, command=d_toggle_to_balance)
    btn_balance.grid(row=14, columnspan=2, pady=20)
    btn_selection = Button(DepositFrame, text="Exit", font=('arial', 18), width=35, command=dep_exit_to_login)
    btn_selection.grid(row=16, columnspan=2, pady=20)
    lbl_deposit = Label(DepositFrame, text="Login", fg="Blue", font=('arial', 12))
    lbl_deposit.grid(row=0, sticky=W)
    lbl_deposit.bind('<Button-1>', dep_toggle_to_login)


def s_toggle_to_balance():
    SelectionFrame.destroy()
    net_balance()


def d_toggle_to_balance():
    DepositFrame.destroy()
    net_balance()


def w_toggle_to_balance():
    WithdrawalFrame.destroy()
    net_balance()


def net_balance():
    database()
    global BalanceFrame
    BalanceFrame = Frame(window)
    BalanceFrame.pack(side=TOP, pady=80)
    lbl_balance_result = Label(BalanceFrame, text="You have: Rs.", font=('arial', 15), bd=18)
    lbl_balance_result.grid(row=1)
    lbl_balance = Label(BalanceFrame, textvariable=NET_BALANCE, font=('arial', 18))
    lbl_balance.grid(row=1, column=1, sticky="W")
    lbl_balance_result = Label(BalanceFrame, text="Your account no:", font=('arial', 15), bd=18)
    lbl_balance_result.grid(row=2)
    lbl_balance = Label(BalanceFrame, textvariable=AC_NUMBER, font=('arial', 18))
    lbl_balance.grid(row=2, column=1, sticky="W")
    lbl_balance_result = Label(BalanceFrame, text="Your name:", font=('arial', 15), bd=18)
    lbl_balance_result.grid(row=3)
    lbl_balance = Label(BalanceFrame, textvariable=CUSTOMER_NAME, font=('arial', 18))
    lbl_balance.grid(row=3, column=1, sticky="W")
    CUSTOMER_NAME.set(customer_name())
    NET_BALANCE.set(net_bal())
    AC_NUMBER.set(get_ac_number())
    btn_balance = Button(BalanceFrame, text="Exit", font=('arial', 15), bd=18, command=bal_exit_to_login)
    btn_balance.grid(row=5)


def bal_exit_to_login():
    BalanceFrame.destroy()
    login_form()


def exit_to_login():
    SelectionFrame.destroy()
    login_form()


def dep_exit_to_login():
    DepositFrame.destroy()
    login_form()


def validate_aadhaar(value):
    if not value:
        return True
    if len(value) > 12:
        return False
    if not value.isdigit():
        return False
    return True


def validate_deposit(value):
    if not value:
        return True
    if not value.isdigit():
        return False
    return True


def validate_age(value):
    if not value:
        return True
    if len(value) > 3:
        return False
    if not value.isdigit():
        return False
    return True


def customer_name():
    database()
    global name
    mycursor.execute("SELECT CONCAT(first_name, ' ', last_name) AS fullname FROM customers WHERE username=%s", (USERNAME.get(),))
    res = mycursor.fetchone()
    if res is None:
        return "Unknown"
    name = res[0]
    print(name)
    return name


def account_number():
    global ac_number
    list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    ac_number = ""
    for i in range(10):
        ac_number = ac_number + random.choice(list)
    return ac_number


def get_ac_number():
    database()
    global ac_num
    mycursor.execute("SELECT account_number FROM customers WHERE username=%s", (USERNAME.get(),))
    res = mycursor.fetchone()
    if res is None:
        return "Unknown"
    ac_num = res[0]
    print(ac_num)
    return ac_num


def net_bal():
    database()
    global original_balance
    mycursor.execute("SELECT balance FROM customers WHERE username=%s", (USERNAME.get(),))
    res = mycursor.fetchone()
    if res is None:
        return None
    original_balance = res[0]
    print(original_balance)
    return original_balance


def deposit():
    database()
    global balance, deposit_amt
    previous_balance = net_bal()
    balance = previous_balance
    deposit_amt = int(DEPOSIT.get())
    # amt = deposit_amt + previous_balance
    # print(amt)
    balance += deposit_amt
    mycursor.execute("update customers set deposit=%s, balance=%s where username=%s",
                     (str(DEPOSIT.get()), balance, str(USERNAME.get())))
    mydb.commit()
    lbl_deposit_result.config(text="Successfully Deposited!", fg="black")
    mycursor.close()
    mydb.close()
    return balance


def withdrawal_form():
    global WithdrawalFrame, lbl_withdrawal_result
    WithdrawalFrame = Frame(window)
    WithdrawalFrame.pack(side=TOP, pady=80)
    lbl_withdrawal_amount = Label(WithdrawalFrame, text="Enter the withdrawal amount:", font=('arial', 15), bd=18)
    lbl_withdrawal_amount.grid(row=1)
    withdrawal_amt = Entry(WithdrawalFrame, font=('arial', 18), textvariable=WITHDRAWAL, width=15)
    withdrawal_amt.grid(row=1, column=1)
    withdrawal_amt.focus_set()
    WITHDRAWAL.set("")
    lbl_withdrawal_result = Label(WithdrawalFrame, text="", font=('arial', 18))
    lbl_withdrawal_result.grid(row=2, columnspan=2)
    btn_withdrawal = Button(WithdrawalFrame, text="Withdraw", font=('arial', 18), width=35, command=withdraw)
    btn_withdrawal.grid(row=12, columnspan=2, pady=20)
    btn_balance = Button(WithdrawalFrame, text="Balance", font=('arial', 18), width=35, command=w_toggle_to_balance)
    btn_balance.grid(row=14, columnspan=2, pady=20)
    btn_selection = Button(WithdrawalFrame, text="Exit", font=('arial', 18), width=35, command=wit_exit_to_login)
    btn_selection.grid(row=16, columnspan=2, pady=20)
    lbl_withdrawal = Label(WithdrawalFrame, text="Login", fg="Blue", font=('arial', 12))
    lbl_withdrawal.grid(row=0, sticky=W)
    lbl_withdrawal.bind('<Button-1>', wit_toggle_to_login)


def wit_exit_to_login():
    WithdrawalFrame.destroy()
    login_form()


def withdraw():
    try:
        database()
        global balance
        previous_balance = net_bal()
        if previous_balance is None:
            lbl_withdrawal_result.config(text="Error: Account not found!", fg="red")
            return
        balance = previous_balance
        withdrawal_amt = WITHDRAWAL.get()
        if not withdrawal_amt.isdigit():
            lbl_withdrawal_result.config(text="Please enter a valid number!", fg="red")
            return
        withdrawal_amt = int(withdrawal_amt)
        if withdrawal_amt <= 0:
            lbl_withdrawal_result.config(text="Withdrawal amount must be positive!", fg="red")
            return
        if withdrawal_amt < balance - 2000:
            balance -= withdrawal_amt
            mycursor.execute("UPDATE customers SET balance=%s WHERE username=%s",
                             (balance, str(USERNAME.get())))
            mydb.commit()
            lbl_withdrawal_result.config(text="Successfully Withdrawn!", fg="black")
        else:
            lbl_withdrawal_result.config(text="Insufficient Balance!", fg="black")
    except mysql.connector.Error as err:
        lbl_withdrawal_result.config(text=f"Database Error: {err}", fg="red")
    except ValueError:
        lbl_withdrawal_result.config(text="Invalid withdrawal amount!", fg="red")
    finally:
        mycursor.close()
        mydb.close()
    return balance


def toggle_to_deposit(event=None):
    SelectionFrame.destroy()
    deposit_form()


def toggle_to_withdrawal(event=None):
    SelectionFrame.destroy()
    withdrawal_form()


def toggle_to_login(event=None):
    RegisterFrame.destroy()
    login_form()


def toggle_to_register(event=None):
    LoginFrame.destroy()
    register_form()


def dep_toggle_to_login(event=None):
    DepositFrame.destroy()
    login_form()


def wit_toggle_to_login(event=None):
    WithdrawalFrame.destroy()
    login_form()


def toggle_to_selection(event=None):
    LoginFrame.destroy()
    selection_form()


def register(event=None):
    database()
    if USERNAME.get() == "" or PASSWORD.get() == "" or AADHAAR_NUMBER.get() == "" or FIRST_NAME.get() == "" or LAST_NAME.get() == "" or AGE.get() == "" or ADDRESS.get() == "" \
            or DEPOSIT.get() == "":
        lbl_register_result.config(text="Please complete the required field!", fg="orange")
    elif int(DEPOSIT.get()) < 2000:
        lbl_register_result.config(text="Minimum Rs. 2000 is required to start an account!", fg="orange")
    elif len(AADHAAR_NUMBER.get()) != 12:
        lbl_register_result.config(text="Aadhaar number must be 12 digits!", fg="orange")
    else:
        mycursor.execute("SELECT * from customers where username=%s", (USERNAME.get(),))
        if mycursor.fetchone() is not None:
            lbl_register_result.config(text="Username is already taken", fg="red")
        else:
            ac_no = account_number()
            print(ac_no)
            initial_bal = int(DEPOSIT.get())
            mycursor.execute("insert into customers (username, password, aadhaar_number, first_name, last_name, age, address, deposit, balance, account_number) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                             (str(USERNAME.get()), str(PASSWORD.get()), str(AADHAAR_NUMBER.get()), str(FIRST_NAME.get()), str(LAST_NAME.get()), int(AGE.get()), str(ADDRESS.get()), int(DEPOSIT.get()), initial_bal, ac_no))
            mydb.commit()
            USERNAME.set("")
            PASSWORD.set("")
            AADHAAR_NUMBER.set("")
            FIRST_NAME.set("")
            LAST_NAME.set("")
            AGE.set("")
            ADDRESS.set("")
            DEPOSIT.set("")
            lbl_register_result.config(text="Successfully Created!", fg="black")
            lbl_register_result.after(3000, lambda: lbl_register_result.config(text=''))
            mycursor.close()
            mydb.close()


def login(event=None):
    database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_login_result.config(text="Please complete the required field!", fg="orange")
    else:
        mycursor.execute("SELECT * from customers WHERE username=%s and password=%s", (USERNAME.get(), PASSWORD.get()))
        if mycursor.fetchone() is not None:
            toggle_to_selection()
        else:
            lbl_login_result.config(text="Invalid username or password", fg="red")


login_form()


# ---------------MENUBAR WIDGETS-------------

MenuBar = Menu(window)
FileMenu = Menu(MenuBar, tearoff=0)
FileMenu.add_command(label="Exit", command=exit_window)
MenuBar.add_cascade(label="File", menu=FileMenu)
window.config(menu=MenuBar)

# ---------------INITIALIZATION-------------

window.mainloop()

#By John Koshy
