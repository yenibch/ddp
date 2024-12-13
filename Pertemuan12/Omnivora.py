from Animal import Animal

class Omnivora(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_gigi, kebiasaan_sosial):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_gigi = jenis_gigi
        self.kebiasaan_sosial = kebiasaan_sosial
    def info_omnivora(self):
        super().info_animal()
        print(f"Jenis Gigi \t\t\t :", self.jenis_gigi,
              "\nKebiasaan Sosial \t\t :", self.kebiasaan_sosial)
        
print("Objek 1")        
omnivora = Omnivora("Beruang", "Daging & Tumbuhan", "Darat", "Melahirkan", "Kombinasi", "Berkelompok")
omnivora.info_omnivora()

print("Objek 2")        
omnivora = Omnivora("Ikan Lele", "Pemakan segala", "Air", "Bertelur", "Geraham Tajam", "Hidup sendiri")
omnivora.info_omnivora()

print("Objek 3")        
omnivora = Omnivora("Babi hutan", "Pemakan Segala", "Darat", "Melahirkan", "Kombinasi", "Berkelompok")
omnivora.info_omnivora()