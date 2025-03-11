from kendaraan import Kendaraan

from mobil import Mobil 

class MobilSport(Mobil) : 
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu, tenaga_kuda, harga):
        super().__init__(jenis, kecepatan_maksimum, merk, jumlah_pintu)
        self.__tenaga_kuda = tenaga_kuda 
        self.__harga = harga
    
    def get_tenaga_kuda(self) : 
        return sel.__tenaga_kuda 
    
    def set_tenaga_kuda(self, value) :
        if value > 0 : 
            self.__tenaga_kuda = value 
        else : 
            print("Tenaga Kuda harus lebih dari 0!")

    def get_harga(self) : 
        return self.__harga 
    
    def set_harga(self, value) : 
        if value > 0 : 
            self.__harga = value 
        else : 
            print("Harga harus lebih dari 0!")

    def info_mobil_sport(self) : 
        return f"{self.info_kendaraan()}, {self.info_mobil()}, Tenaga Kuda : {self.__tenaga_kuda}, Harga : {self.__harga}"
    
    def mode_balap(self) : 
        return "Mobil Sport masuk ke mode balap!"

mobil3 = MobilSport("Toyota", "140MPH", "GR 86", 2, 228 , "1.1M" )
print(mobil3.info_mobil_sport() )
print(mobil3.mode_balap())
