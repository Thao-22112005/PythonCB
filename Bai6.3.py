# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:37:27 2026

@author: Danh Thao
"""

class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance
    def Deposit(self):
        a = float(input("So tien nap vao tai khoan: "))
        self.balance+=a
    def Withdrawal(self):
        b = float(input('So tien ban muon rut: '))
        self.balance-=b
    def bankFees(self):
        self.balance-=0.05*self.balance
    def display(self):
        print("So tai khoan:",self.accountNumber)
        print("Ten:",self.name)
        print("So du:",self.balance)
    
def main():
    bc1= BankAccount(2005,"Danh Thao",20000000)
    luaChon =0
    while True:
        print('===================MENU===================')
        print('1. Nap tien')
        print('2. Rut tien')
        print('3. Tra phi')
        print('4. Hien Thi')
        print('5. Thoat')
        luaChon=int(input('Moi ban lua chon: '))
        while luaChon < 1 or luaChon > 5:
            print('Chi duoc lua chon tu 1->5. Nhap lai')
            luaChon=int(input('Moi ban lua chon: '))
        if luaChon == 1:
            bc1.Deposit()
            print('Thong tin tai khoan sau khi nap tien la: ')
            bc1.display()
        elif luaChon == 2:
            bc1.Withdrawal()
            print('Thong tin tai khoan sau khi rut tien la: ')
            bc1.display()
        elif luaChon == 3:
            bc1.bankFees()
            print('Thong tin tai khoan sau khi tra phi')
            bc1.display()
        elif luaChon == 4:
            print('Thong tin tai khoan')
            bc1.display()
        elif luaChon == 5:
            print('Bye!!!')
            break
main()