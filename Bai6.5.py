# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:03:48 2026

@author: Danh Thao
"""

class NCC:
    def __init__(self,maPhieu,ngayLap,MaNCC, TenNCC, DiaChi):
        self.maPhieu = maPhieu
        self.ngayLap=ngayLap
        self.MaNCC=MaNCC
        self.TenNCC=TenNCC
        self.DiaChi = DiaChi
        
class Hang():
    def __init__(self, tenHang, donGia, soLuong):
        self.tenHang=tenHang
        self.donGia=donGia
        self.soLuong=soLuong
    def ThanhTien(self):
        return self.donGia * self.soLuong*1.0

def Nhap():
    maPhieu = input('Nhap ma phieu: ')
    ngayLap = input('Nhap ngay lap: ')
    maNCC = input('Nhap ma ncc: ')
    tenNCC = input('Nhap ten ncc: ')
    diaChi = input('Nhap dia chi: ')
    ncc = NCC(maPhieu,ngayLap,maNCC,tenNCC,diaChi)
    hang = []
    n = int(input('Nhap so luong don hang: '))
    for i in range(n):
        print(f'Nhap hang thu {i+1}')
        tenHang = input('Ten hang: ')
        donGia = float(input('Don gia: '))
        soLuong = int(input('So luong: '))
        
        h = Hang(tenHang,donGia,soLuong)
        hang.append(h)
    return ncc, hang
def InThongTin():
    ncc, dsh = Nhap()
    print(f"{'PHIEU NHAP HANG':^50}")
    print("{:<40} {:<40}".format(f'Ma phieu: {ncc.maPhieu}',f'Ngay lap: {ncc.ngayLap}'))
    print("{:<40} {:<40}".format(f'Ma NCC: {ncc.MaNCC}',f'Ten NCC: {ncc.TenNCC}'))
    print("{:<70}".format(f'Dia chi: {ncc.DiaChi}'))
    print(f"{'Ten hang':^20} {'Don gia':^10} {'So luong':^10} {'Thanh tien':^15}")
    for h in dsh:
        print("{:^20} {:^10} {:^10} {:^15}".format(h.tenHang,h.donGia,h.soLuong,h.ThanhTien()))
    tong = sum(h.ThanhTien() for h in dsh)
    print(f"{'':^15} {'':^5} {'Cong thanh tien':^20} {tong:^20}")
InThongTin()
    
        