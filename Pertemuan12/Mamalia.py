from Animal import Animal

class Mamalia(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, ukuran_tubuh, jenis_kulit):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.ukuran_tubuh = ukuran_tubuh
        self.jenis_kulit = jenis_kulit

    def info_mamalia(self):
        super().info_animal()
        print(f"Ukuran Tubuh \t\t\t :", self.ukuran_tubuh,
              "\nJenis Kulit \t\t\t :", self.jenis_kulit)
        
        
print("Objek 1")        
mamalia = Mamalia("Paus", "Ikan Kecil", "Air", "Melahirkan", "Sangat Besar", "Licin tidak Berbulu")
mamalia.info_mamalia()

print("Objek 2")        
mamalia = Mamalia("Kuda", "Tumbuhan", "Darat", "Melahirkan", "Sangat Besar", "Sedikit Berbulu")
mamalia.info_mamalia()

print("Objek 3")        
mamalia = Mamalia("Gajah", "Tumbuhan", "Darat", "Melahirkan", "Sangat Besar", "Berbulu")
mamalia.info_mamalia()