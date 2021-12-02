#Input

x = int(input("Masukan awal deret : "))
y = int(input("Masukan akhir deret : "))

if (x + 1) % 2 == 0 :
    for i in range (x + 1, y , 2) :
        if (i % 5 != 0) and (i % 9 != 0) :
            print(i ,"", end ="")
else :
    for i in range (x, y , 2) :
        if (i % 5 != 0) and (i % 9 != 0) :
            print(i,"", end ="")
