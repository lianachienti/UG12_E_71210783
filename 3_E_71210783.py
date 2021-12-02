x = int(input("Masukkan Angka : "))

for i in range(x // 2 + 1) :
    print(' ' * (x // 2 - i) + '* ' * (i + 1))
for i in reversed(range(x // 2 + 1)) :
    print(' ' * (x // 2 - i) + '* ' * (i + 1))
