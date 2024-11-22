#tugas1


print('## Nomor 1 ##')
def celcius_ke_fahrenheit(celcius):
    fahrenheit=(celcius*9/5)+32
    return fahrenheit

suhu_celcius1 = 0
suhu_celcius2= 100
suhu_fahrenheit1 = celcius_ke_fahrenheit (suhu_celcius1)
print('Suhu Celcius', suhu_celcius1, 'sama dengan', suhu_fahrenheit1)

suhu_fahrenheit2 = celcius_ke_fahrenheit (suhu_celcius2)
print('Suhu Celcius', suhu_celcius2, 'sama dengan', suhu_fahrenheit2)

#Tugas2

print()
print('## Nomor 2 ##')
def genap_ganjil(bilangan):
    hitung = bilangan % 2 == 0
    return hitung

angka = 4
hasil = genap_ganjil(angka)
print(f"Bilangan {angka} bernilai {hasil}")

angka2 = 7
hasil2 = genap_ganjil(angka2)
print(f"Bilangan {angka2} bernilai {hasil2}")

#tugas3

print()
print('## nomor 3 ##')
def cek_kelulusan(nilai):
    if nilai >= 65:
        return 'Lulus'
    else:
        return 'Gagal'
    
nilai_kamu = 80
status = cek_kelulusan(nilai_kamu)
print(f"Nilai: {nilai_kamu}, Status: {status}")

nilai_kamu2 = 60
status2 = cek_kelulusan(nilai_kamu2)
print(f"Nilai: {nilai_kamu2}, Status: {status2}")


#tugas4
print()
print('## Nomor 4 ##')
def bil_ganjil(ganjil):
    for i in range(1,ganjil+1, 2):
        print(i, end=" ")
bil_ganjil(20)           
