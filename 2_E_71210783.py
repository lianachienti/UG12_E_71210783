#data

senin = ['kelas ke-1 Algorima Graf', 'kelas ke-3 Sistem Operasi', 'kelas ke-4 PAK', 'kelas ke-5 Praktikum INLAN']
selasa = ['kelas ke-2 Matematika Teknik', 'kelas ke-4 Bhs Indonesia', 'kelas ke-6 PKN']
rabu = ['Hari rabu Anda tidak ada kelas']
kamis = ['kelas ke-1 IMK', 'kelas ke-3 LogMat', 'kelas ke-4 Praktekkom']
jumat = ['kelas ke-2 Sistem Basis Data', 'kelas ke-4 Praktikum Sistem Basis Data', 'kelas ke-6 INLAN']

#input

a = input("Hi Tutu, Silahkan masukan hari yang ingin Anda telusuri : ")

if a == 'senin' :
    for i in range (len(senin)) :
        print(senin[i])
elif a == 'selasa' :
    for i in range (len(selasa)) :
        print(selasa[i])
elif a == 'rabu' :
    for i in range (len(rabu)) :
        print(rabu[i])
elif a == 'kamis' :
    for i in range (len(kamis)) :
        print(kamis[i])
elif a == 'jumat' :
    for i in range (len(jumat)) :
        print(jumat[i])
    
