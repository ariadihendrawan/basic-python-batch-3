pilihan=0
daftar_nama=[]
daftar_nomor=[]

while pilihan!=3:
    print('================')
    print('SELAMAT DATANG !')
    print('================')
    print('''         --MENU--
    1. Daftar Kontak
    2. Tambah Kontak
    3. Keluar'''  )
    print()
    pilihan=int(input('Pilihan menu :'))

    if (pilihan==1):
        print('--------------------')
        print('Daftar kontak :')
        if(len(daftar_nama)>0):
            for x in range(len(daftar_nama)):
                print('Nama       :',daftar_nama[x])
                print('No telepon :',daftar_nomor[x])
                print()
           
        else :
            print('- kosong -')
            print()

    elif (pilihan==2):
        print('--------------------')
        namabaru=input('Nama :')
        nomorbaru=input('Nomor :')
        daftar_nama.append(namabaru)
        daftar_nomor.append(nomorbaru)
        print('Kontak berhasil ditambahkan')
        print()
        print()

    elif (pilihan==3):
        print('--------------------')
        print('Program selesai, sampai jumpa!')
        print()
        
    else : 
        print('--------------------')
        print('Menu tidak tersedia')
        print()