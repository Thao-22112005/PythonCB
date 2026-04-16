# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:12:30 2026

@author: Danh Thao
"""
import string

chuoi = str(input("Nhap chuoi: "))

chuoi = chuoi.lower()

print(chuoi)

for p in string.punctuation:
    chuoi = chuoi.replace(p, "")

words = chuoi.split()

dic = {}

for word in words:
    if word in dic:
        dic[word] = dic[word] + 1
    else:
        dic[word] = 1

items = list(dic.items())

n = len(items)

for i in range(n):
    for j in range(0, n-i-1):
        if items[j][1] < items[j+1][1]:
            temp = items[j]
            items[j] = items[j+1]
            items[j+1]=temp


for k , v in items:
    print(k, ":",v)


