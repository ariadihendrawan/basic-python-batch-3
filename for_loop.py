# fruit=['apple','banana','cherry']
# banyak_data=3
# for x in range(banyak_data):
#     fruit.append(input("Masukkan data "))

# print(fruit)

n=int(input("Masukkan jumlah data :"))
print('------------------------------')
list_nama=[]
list_umur=[]
for i in range(n):
    nama=input("Masukkan nama : ")
    umur=input("Masukkan umur : ")
    print('=======================')
    list_nama.append(nama)
    list_umur.append(umur)

for x in range(n):
    print(list_nama[x-1], list_umur[x-1])
