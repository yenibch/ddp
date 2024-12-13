from Animal import Animal

class Carnivora(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_gigi, jenis_memburu):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_gigi = jenis_gigi
        self.jenis_memburu = jenis_memburu
    def info_carnivora(self):
        super().info_animal()
        print(f"Jenis Gigi \t\t\t :", self.jenis_gigi,
              "\nJenis Memburu \t\t\t :", self.jenis_memburu)
        
print("Objek 1")        
carnivora = Carnivora("Singa", "Daging", "Darat", "Melahirkan", "Taring Tajam", "Menjebak Mangsa")
carnivora.info_carnivora()

print("Objek 2")        
carnivora = Carnivora("Serigala", "Daging", "Darat", "Melahirkan", "Taring Tajam", "Berkelompok")
carnivora.info_carnivora()

print("Objek 3")        
carnivora = Carnivora("Hiu", "Ikan-ikan", "Air/Laut", "Melahirkan", "Besar & Tajam", "Serangan Diam-diam")
carnivora.info_carnivora()
