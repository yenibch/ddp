import math

def kubus(sisi):
    volume = 6 * sisi **2
    print(f"luas kubus adalah = {volume}")

def balok(panjang, lebar, tinggi):
    volume= 2* panjang * lebar * tinggi
    print(f"luas balok adalah = {volume}")

def tabung(jari2, tinggi):
    volume = 2* 22/7 * jari2 * tinggi
    print(f"luas tabung adalah = {volume}")

def prisma(l_alas, kel_alas, tinggi):
    volume = 2 * l_alas * kel_alas * tinggi
    print(f"luas prisma adalah = {volume}")

def limas(l_alas, tinggi):
    volume = l_alas * tinggi
    print(f"luas limas adalah = {volume}")