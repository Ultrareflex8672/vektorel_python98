# Görev olarak verilen "if" ödevi aşağıdaki gibidir

sayi = 10
if sayi > 5:
    print("Sayı 5'ten büyüktür.")


sayi = 3
if sayi > 5:
    print("Sayı 5'ten büyüktür.")
else:
    print("Sayı 5'ten küçük ya da eşittir.")


sayi = 7
if sayi > 10:
    print("Sayı 10'dan büyüktür.")
elif sayi == 7:
    print("Sayı 7'dir.")
else:
    print("Sayı 10'dan küçük ve 7 değil.")


yas = 25
sehir = "İstanbul"
if yas > 18 and sehir == "İstanbul":
    print("Yasınız 18'den büyük ve İstanbul'dasınız.")


yas = 16
sehir = "Ankara"
if yas < 18 or sehir == "İstanbul":
    print("Yaşınız 18'den küçük ya da İstanbul'dasınız.")


ad = "Ali"
if ad == "Ali":
    print("Merhaba Ali!")


mevsimler = ["kış", "ilkbahar", "yaz", "sonbahar"]
if "yaz" in mevsimler:
    print("Yaz mevsimi mevcut.")


yas = int(input("Yaşınızı girin: "))
if yas >= 18:
    print("Reşitsiniz.")
else:
    print("Reşit değilsiniz.")


ad = input("Adınızı girin: ")
if not ad:
    print("Ad girilmedi!")
else:
    print("Adınız:", ad)


a = 10
b = 20
c = 15

if a > b and a > c:
    print("En büyük sayı a'dır:", a)
elif b > a and b > c:
    print("En büyük sayı b'dir:", b)
else:
    print("En büyük sayı c'dir:", c)


def is_teenager(age):
    if age >= 13 and age <= 19:
        return True
    else:
        return False

yas = 16
if is_teenager(yas):
    print("Bu kişi bir gençtir.")
else:
    print("Bu kişi genç değil.")
