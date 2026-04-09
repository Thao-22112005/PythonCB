# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:27:38 2026

@author: Danh Thao
"""

class HCN:
    def __init__(self, cd, cr):
        self.cd=cd
        self.cr = cr
    def Perimeter(self):
        return 2*(self.cd + self.cr)
    def Area(self):
        return self.cd*self.cr
    def display(self):
        print(f'Chieu dai {self.cd} va chieu rong {self.cr} co chu vi bang {self.Perimeter()} va dien tich bang {self.Area()}')


hcn1=HCN(3,4)
hcn1.display()