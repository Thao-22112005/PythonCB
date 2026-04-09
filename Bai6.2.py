# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:32:47 2026

@author: Danh Thao
"""

class Person:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi
    def display(self):
        print("Ten:",self.ten)
        print("Tuoi:",self.tuoi)
    
class Student(Person):
    def __init__(self, ten, tuoi, session):
        super().__init__(ten, tuoi)
        self.session=session
    def displayStudent(self):
        super().display()
        print(self.session)


sv1 = Student('Thao',20,'KTPM02')
sv1.displayStudent()