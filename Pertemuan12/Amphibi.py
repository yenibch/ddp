from Animal import Animal

class Amphibi(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_air, bernapas):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas
    def info_amphibi(self):
        super().info_animal()
        print(f"Jenis Air \t\t\t :", self.jenis_air,
              "\nBernapas \t\t\t :", self.bernapas)
        
        
print("Objek 1")      
amphibi = Amphibi("Katak", "serangga", "Dua Alam", "Bertelur","Air Tawar", "Paru-paru" )
amphibi.info_amphibi()

print("Objek 2")
amphibi = Amphibi("Buaya", "Daging", "Dua Alam", "Bertelur", "Air Tawar", "Paru-paru")
amphibi.info_amphibi()

print("Objek 3")
amphibi = Amphibi("Cacing", "Tanah", "Dua Alam", "Bertelur", "Tanah", "Kulit")
amphibi.info_amphibi()
