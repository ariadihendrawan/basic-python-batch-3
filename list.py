angka="Ini adalah angka 10"
angka_list=["ini","adalah","angka",10]

#print(angka[0])
#print(angka_list[0])

for x in angka_list :
    print(x)

hasil=" "
for x in range(0,len(angka_list)) :
    hasil=hasil+angka_list[x]+" "
    print(hasil)

print(hasil)
