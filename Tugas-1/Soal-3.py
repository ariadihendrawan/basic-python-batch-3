n_teori=float(input("Masukkan nilai ujian teori   :"))
n_praktek=float(input("Masukkan nilai ujian praktek :"))

if (n_teori >=70 and n_praktek >=70):
    print('Selamat, anda lulus')
elif (n_teori>=70 and n_praktek<70):
    print('Anda harus mengulang ujian praktek')
elif (n_teori<70 and n_praktek>=70):
    print('Anda harus mengulang ujian teori')
elif(n_teori <70 and n_praktek <70):
    print('Anda harus mengulang ujian teori dan praktek')