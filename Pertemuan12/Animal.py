class Animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    def info_animal(self):
        print(f"Nama Hewan \t\t\t :", self.nama,
              "\nMakanan \t\t\t :", self.makanan,
              "\nHidup \t\t\t\t :", self.hidup,
              "\nBerkembang Biak \t\t :", self.berkembang_biak)
        

# hewan = Animal("kucing", "cimol","udara","bertelur")
# hewan.info_animal()

# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)

# buat minimal 3 class child (Amphibi,  Mamalia, Carnivora, dll) setiap class child itu memiliki 2 properti dan method  
# buat 3 objek dari masing masing class child. 