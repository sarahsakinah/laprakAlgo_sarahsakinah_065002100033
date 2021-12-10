# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 17:11:41 2021

nama:sarah sakinah
prodi:sistem infomasi
nim:065002100033
"""

def menghitung_range():
    print("PROGRAM MENGHITUNG JUMLAH RANGE")
    sarah = input("masukan angka pertama: ")
    sarah = int (sarah)
    input2=int(input('masukkan angka kedua: '))
    sum = 0
    for i in range(sarah, input2+1, 1):
        sum = sum+i
    print("Jumlah range adalah: ", sum )
menghitung_range()