r=float(input('Masukkan jari-jari lingkaran : '))  #r tipe float bisa flexible menerima angka pecahan
luas=(22/7)*r*r
print('Luas lingkaran dengan jari-jari',r,'cm adalah',luas,'cm\u00b2')

#BONUS : format 2 angka di belakang koma
print('Luas lingkaran dengan jari-jari',r,'cm adalah','{:.2f}'.format(luas),'cm\u00b2')