#Arithmetic
x = 2 + 3
print(x)
print(17 // 5)
print(10 % 4)

#Comparison
print(2 == 2)
print(3 == 2)
print(2 != 2)
print(3 != 2)

#Assignment
x = 2
x += 2

print(x)

y = 5
y -= 2
print(y)

z = 5
z *= 2
print(z)

#Logical
x = 2
y = 2
print(x > 0 and y > 0)

#Membership
x = [1, 2, 3, 4]
print(2 in x)
print(5 in x)

#Identity
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
z = x
print(x is not y)
print (x is not z)

#Kondisi If
x = 10
if (x > 0 and x < 100):
    print("Nilai x lebih besar dari 0 dan lebih kecil dari 100")

#Kondisi Else
nilai = 80
absen = 80
if (nilai > 75 and absen > 85):
    print("slmt y km lulus")
else:
    print("bljr lg jgn mls")

#Kondisi Elif
a = 2
b = 2
if (a > b):
    print("Nilai a lebih besar dr b")
elif (a < b):
    print("Nilai a lebih kecil dari b")
else:
    print("Nilai a sama dengan b")

#Kondisi Shorthand
a = 5
b = 3

print("a") if a . b else print("a == b") if a == b else print("b")

#If and Operators
nilai = 80
absen = 70

if (nilai > 75 and absen > 80):
    print("Selamat Anda lulus karena nilai dan absen anda memenuhi")
elif (nilai > 75 and absen < 80):
    print("Anda belum lulus ujian karena absen Anda belum memenuhi")
elif (nilai < 75 and absen > 80):
    print("Anda belum lulus ujian karena nilai Anda belum memenuhi")
else:
    print("Anda belum lulus ujian karena nilai dan absen anda belum memenuhi")

#Nested If
a = 9

if (a > 0):
    print("Nilai a lebih besar dari 0")
    if (a > 5):
        print("Nilai a lebih besar dari 5")
        if (a > 10):
            print("Nilai a lebih besar dari 10")
        else:
            print("Tapi, nilai a lebih kecil dari 10")
    else:
        print("Tapi, nilai a lebih kecil dari 5")
else:
    print("Nilai a lebih kecil dari 0")