# Rumus Persegi Panjang
from re import L
from tkinter import Variable
print("RPL Kelompok B Tugas Git 1")
print("____________________________________")
print("\nRumus Persegi Panjang")
P = int(input("\nInput Panjang : "))
L = int(input("\nInput Lebar : "))
Luas_Persegi_Panjang = P * L
Keliling_Persegi_Panjang = 2 * (P + L)
print("Luas Persegi Panjang\t : ",Luas_Persegi_Panjang)
print("Keliling Persegi Panjang\t : ",Keliling_Persegi_Panjang)

# Rumus Lingkaran
print("\nRumus Lingkaran")
R = int(input("\nInput Jari-jari :"))
Luas_Lingkaran = 3.14 * R * R
Keliling_Lingkaran = 2 * 3.14 * R
print("Luas Lingkaran\t :",Luas_Lingkaran)
print("Keliling Lingkaran\t :",Keliling_Lingkaran)

#Rumus Segitiga
print("\n Rumus Segitiga")
a = float(input("\nMasukkan panjang alas: "))
t = float(input("\nMasukkan tinggi segitiga: "))
luas = 0.5*a*t
print("Luas segitiga adalah :",luas)