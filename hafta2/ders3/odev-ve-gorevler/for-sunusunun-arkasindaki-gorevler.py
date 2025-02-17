# 0'dan 10'a kadar saydır
for i in range(11):
    print(i)

print("\n")

# 1'den 10'a kadar saydır
for i in range(1, 11):
    print(i)

print("\n")

# Geri sayım sayacı
for i in range(10, -1, -1):
    print(i)

print("\n")

# 12'den 50'ye (50 dahil) kadar saydır
for i in range(12, 51):
    print(i)

print("\n")

# 30'dan 100'e (100 dahil) kadar 5'er saydır
for i in range(30, 101, 5):
    print(i)

print("\n")

# 100'den 40'a kadar (40 dahil) 5'er geri saydır
for i in range(100, 39, -5):
    print(i)

print("\n")

# Kaça kadar sayayım diye sor ve saydır
end = int(input("Kaça kadar sayayım? "))
for i in range(end + 1):
    print(i)

print("\n")

# Kaçtan kaça kadar sayacağını sor ve saydır
start = int(input("Kaçtan başlayayım? "))
end = int(input("Kaça kadar sayayım? "))
for i in range(start, end + 1):
    print(i)

print("\n")

# Kaçtan kaça kadar kaçar kaçar sayacağını sor ve saydır
start = int(input("Kaçtan başlayayım? "))
end = int(input("Kaça kadar sayayım? "))
step = int(input("Kaçar kaçar sayayım? "))
for i in range(start, end + 1, step):
    print(i)

print("\n")

# Programı kullanan kişinin adını, yaşı sayısınca yazdırın
name = input("Adınız nedir? ")
age = int(input("Kaç yaşındasınız? "))
for i in range(age):
    print(name)

print("\n")

# Çarpım tablosunu ekrana yazdırın
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("\n")

print("\n")

# Takdir, teşekkür hesaplayıcı
num_courses = int(input("Kaç dersiniz var? "))
total = 0
for i in range(num_courses):
    grade = float(input(f"{i + 1}. dersinizin ortalaması nedir? "))
    total += grade

average = total / num_courses

if average >= 85:
    print("Takdir belgesi aldınız.")
elif average >= 70:
    print("Teşekkür belgesi aldınız.")
else:
    print("Hiçbir belge alamadınız.")