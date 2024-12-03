import math

def l_persegi(sisi):
    hitung = sisi * sisi
    print(f"luas persegi adalah {sisi} * {sisi} = {hitung}")

def l_persegipanjang(panjang, lebar):
    hitung = panjang * lebar
    print(f"luas persegi panjang adalah {panjang} * {lebar} = {hitung}")

def l_jajargenjang(alas, tinggi):
    hitung = alas * tinggi
    print(f"luas dari jajargenjang adalah {alas} * {tinggi} = {hitung}")

def l_segitiga(alas, tinggi):
    hitung = 1/2 * alas * tinggi
    print(f"luas dari segitiga adalah 1/2 * {alas} * {tinggi} = {hitung}")  

def l_lingkaran(jari2):
    hitung = 22/7 * jari2 **2
    print(f"lias lingkaran adalah 22/7 * {jari2} **2 = {hitung}")
