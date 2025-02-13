# Görev olarak verilen "input" ödevi aşağıdaki gibidir
isim = input("Adınızı girin: ")
print("Merhaba,", isim)

sayi = int(input("Bir sayı girin: "))
print("Girilen sayının iki katı:", sayi * 2)

ad, soyad = input("Ad ve Soyadınızı girin: ").split()
print("Ad:", ad)
print("Soyad:", soyad)

deger = float(input("Bir ondalıklı sayı girin: "))
print("Girilen sayının karesi:", deger ** 2)

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
toplam = sayi1 + sayi2
print("Toplam:", toplam)

sayilar = input("Birkaç sayı girin (aralarına boşluk koyun): ").split()
sayilar = [int(sayi) for sayi in sayilar]
print("Sayılardan en büyüğü:", max(sayilar))

while True:
    try:
        yas = int(input("Yaşınızı girin: "))
        break
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
print("Yaşınız:", yas)

secim = input("Lütfen 'evet' veya 'hayır' yazın: ").lower()
if secim == "evet":
    print("Seçiminiz evet!")
else:
    print("Seçiminiz hayır!")

sifre = input("Şifrenizi girin: ")
if sifre == "12345":
    print("Şifre doğru!")
else:
    print("Yanlış şifre.")
