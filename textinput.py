nama=input("Masukkan nama : ")
nomor=input("Masukkan no telp : ")

f = open("nama.txt", "w")
f.write(nama+"\n")
f.write(nomor+"\n")
f.close()

f = open("nama.txt", "r")
print(f.read())
