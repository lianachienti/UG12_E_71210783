def nilai_x(deret_bilangan) :
    nilai_kecil = deret_bilangan[0]
    for nilai in deret_bilangan :
        if nilai < nilai_kecil :
            nilai_kecil = nilai
    return nilai_kecil

def nilai_y(deret_bilangan) :
    nilai_besar = deret_bilangan[0]
    for nilai in deret_bilangan :
        if nilai > nilai_besar :
            nilai_besar = nilai
    return nilai_besar

a = [3, 20, 100, -35, 50]

print(a)
print("Nilai terbesar : ", nilai_y(a))
print("Nilai terkecil : ", nilai_x(a))
