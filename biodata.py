class bio:
    def __init__(self,nama,umur,alamat):
        self.nama=nama
        self.umur=umur
        self.alamat=alamat

nama=input("Masukkan nama = ")
umur=input("Masukkan umur : ")
alamat=input("Masukkan alamat : ")

p1=bio(nama,umur,alamat)
#print(p1.nama,umur,alamat)
print("Namaku {}, umurku {} tahun, aku tinggal di {}.".format(p1.nama,umur,alamat))



