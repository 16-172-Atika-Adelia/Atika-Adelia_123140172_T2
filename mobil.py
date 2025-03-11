from kendaraan import Kendaraan

# Kelas turunan 
class Mobil(Kendaraan) : 
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu) : 
        super().__init__(jenis, kecepatan_maksimum)
        self.merk = merk 
        self.jumlah_pintu = jumlah_pintu

    def info_mobil(self) : 
        return f"Merk Mobil : {self.merk}"

    def bunyikan_klakson(self) : 
        return "Tin! Tin!"
    
mobil2 = Mobil("Toyota", "140MPH", "GR 86", 2)

print(mobil2.info_mobil())
print(mobil2.bunyikan_klakson())