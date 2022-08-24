from tkinter import *
import json

try:
    file = open('users.json', 'r')
    users = json.load(file)
    print(users)
except Exception as e:
    print(e)


class Account:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('User Login')
        # root.geometry('500x500')
        self.root.resizable(False, False)

        self.username = StringVar()
        self.password = StringVar()

        self.label_un = Label(self.root, text='Username', padx=20, pady=20)
        self.label_un.grid(row=0, column=0)

        self.entry_un = Entry(self.root, textvariable=self.username)
        self.entry_un.grid(row=0, column=1, padx=20, pady=20)

        self.label_pw = Label(self.root, text='Password')
        self.label_pw.grid(row=1, column=0)

        self.entry_pw = Entry(self.root, show='*', textvariable=self.password)
        self.entry_pw.grid(row=1, column=1)

        self.btn_login = Button(self.root, text='Login', command=self.login)
        self.btn_login.grid(row=6, column=0, columnspan=2, padx=20, pady=20)

        self.label_msg = Label(self.root, text='')
        self.label_msg.grid(row=7, column=0, columnspan=2, pady=10)

        self.root.mainloop()

    def login(self):
        # un = entry_un.get()
        # pw = entry_pw.get()
        un = self.username.get()
        pw = self.password.get()
        
        for user in users:
            if un==user['username'] and pw==user['password']:
                self.root.destroy()
                user_index = users.index(user)
                Transaction(user_index)
                break
        else:
            self.label_msg.config(text='Wrong credentials', foreground='red')


class Transaction:
    def __init__(self, u) -> None:
        self.root1 = Tk()
        self.root1.title('Dashboard')
        self.root1.geometry('300x300')

        self.user_index = u
        self.amount = IntVar()

        self.label_msg = Label(self.root1, text=f'Welcome { users[self.user_index]["name"] }', font=('Arial', 18))
        self.label_msg.grid(row=0, column=0, padx=20)

        self.label_bal = Label(self.root1, text=f'Your balance is: { users[self.user_index]["balance"] }', font=('Arial', 18))
        self.label_bal.grid(row=1, column=0, padx=20)

        self.entry_amt = Entry(self.root1, textvariable=self.amount)
        self.entry_amt.grid(row=2, column=0, padx=20)

        self.btn_w = Button(self.root1, text="Withdraw", command=lambda: self.transaction('w'))
        self.btn_w.grid(row=3, column=0, padx=20, pady=10)

        self.btn_d = Button(self.root1, text="Deposite", command=lambda: self.transaction('d'))
        self.btn_d.grid(row=4, column=0, padx=20, pady=10)

        self.root1.mainloop()

    def transaction(self, type):
        amt = self.amount.get()
        if type == 'w':
            users[self.user_index]['balance'] = users[self.user_index]['balance'] - amt
        elif type == 'd':    
            users[self.user_index]['balance'] = users[self.user_index]['balance'] + amt
        self.label_bal.config(text=f'Your balance is: { users[self.user_index]["balance"] }')

        try:
            file = open('users.json', 'w')
            json.dump(users, file)
            print(users)
        except Exception as e:
            print(e)

Account()
