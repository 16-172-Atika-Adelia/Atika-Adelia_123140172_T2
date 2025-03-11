class Kendaraan : 
    def __init__(self, jenis, kecepatan_maksimum):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum

    def info_kendaraan(self) : 
            return f"Jenis Kendaraan : {self.jenis}, kecepatan maksimum : {self.kecepatan_maksimum} km/jam"
        
    def bergerak(self) : 
            return f"Kendaraan {self.jenis} sedang bergerak"

mobil = Kendaraan("Toyota", "140MPH")
print(mobil.info_kendaraan())
print(mobil.bergerak())
        

                
                
        