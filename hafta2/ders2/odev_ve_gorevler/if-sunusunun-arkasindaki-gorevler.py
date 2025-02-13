# Gorev olarak verilen "if sunusunun arkasındaki görevleri yapın" ödevi aşağıdadır.

    # 1. Girilen Sayının 100’den Büyük Olup Olmadığını Söyleyen Program:
sayi = int(input("Bir sayı girin: "))
if sayi > 100:
    print("Sayı 100'den büyüktür.")
else:
    print("Sayı 100'den küçük veya eşittir.")

    # 2. Nasılsın Diye Sorsun, Cevaba Göre Yorum Yapsın:
cevap = input("Nasılsın? ")

if cevap.lower() in ["iyi", "güzel", "harika"]:
    print("Buna sevindim!")
else:
    print("Üzgün olmana üzüldüm.")

    # 3. Notunu Sorup Kalıp Geçtiğini Söyleyen Program:
notu = int(input("Notunuzu girin: "))

if notu >= 50:
    print("Geçtin")
else:
    print("Kaldın")

    # 4. Şifre Ekranı Yapın, Bilemezse Yetki Yok Desin:
dogru_sifre = "12345"
sifre = input("Şifrenizi girin: ")

if sifre == dogru_sifre:
    print("Şifre doğru, programa hoş geldiniz!")
else:
    print("Yetki yok!")

    # 5. Girilen Yıla Göre Geçmiş, Gelmiş veya Şu Anki Yılı Söyleyen Program:
yil = int(input("Bir yıl girin: "))
current_year = 2025

if yil < current_year:
    print("Bu yıl geçmiş.")
elif yil == current_year:
    print("Bu yıl şu anda içindeyiz.")
else:
    print("Bu yıl henüz gelmemiş.")

    # 6. Yaş Kategorisi Tespiti Programı:
yas = int(input("Yaşınızı girin: "))

if yas <= 3:
    print("Bebek")
elif yas <= 14:
    print("Çocuk")
elif yas <= 35:
    print("Genç")
elif yas <= 65:
    print("Orta Yaşlı")
else:
    print("Yaşlı")

    # 7. Vücut Kitle Endeksi Hesaplayan ve Yorumlayan Program:
boy = float(input("Boyunuzu (metre cinsinden) girin: "))
kilo = float(input("Kiloyu girin: "))

vki = kilo / (boy ** 2)
print("Vücut Kitle Endeksiniz:", vki)

if vki < 18.5:
    print("Zayıf")
elif 18.5 <= vki < 24.9:
    print("Normal kilolu")
elif 25 <= vki < 29.9:
    print("Fazla kilolu")
else:
    print("Obez")

ideal_kilo_min = 18.5 * (boy ** 2)
ideal_kilo_max = 24.9 * (boy ** 2)
print(f"İdeal kilonuz: {ideal_kilo_min:.2f} kg - {ideal_kilo_max:.2f} kg arası.")

    # 8. Hava Sıcaklığını Sorsun ve Yorum Yapsın:
sicaklik = float(input("Hava sıcaklığını girin (°C): "))

if sicaklik < 10:
    print("Soğuk, kalın giyinin.")
elif 10 <= sicaklik < 25:
    print("Güzel bir hava, hafif giyinin.")
else:
    print("Sıcak, kendinizi serin tutun.")

    # 9. Doğum Tarihini Sorsun, Kardeş Sayısını Sorsun - (Not: Henüz derste işlenmediğinden "for" döngüsü ile her kardeş için ayrı ayrı işlem yaptırmadım):
dogum_tarihi = input("Doğum tarihinizi (YYYY) formatında girin: ")
kardes_sayisi = int(input("Kaç kardeşsiniz? "))

if kardes_sayisi == 1:
    print("Tek çocuksunuz.")
else:
    kardes_dogum = int(input("Bir kardeşinizin doğum yılını girin: "))
    if kardes_dogum > int(dogum_tarihi):
        print(f"Bu kardeşiniz sizden küçük.")
    elif kardes_dogum < int(dogum_tarihi):
        print(f"Bu kardeşiniz sizden büyük.")
    else:
        print(f"Bu kardeşiniz sizinle aynı yaştadır.")

    # 10. Hangi Ayda Olduğumuzu Soracak ve Mevsimi Söyleyecek Program - (Ay isimleri ile yapmaya üşendim :)):
ay = int(input("Hangi aydayız? (1-12 arası bir değer girin): "))

if 1 <= ay <= 3:
    print("Kış mevsimindeyiz.")
elif 4 <= ay <= 6:
    print("Bahar mevsimindeyiz.")
elif 7 <= ay <= 9:
    print("Yaz mevsimindeyiz.")
elif 10 <= ay <= 12:
    print("Sonbahar mevsimindeyiz.")
else:
    print("Geçersiz ay girdiniz.")

    # 11. Üç Sayıyı Alıp En Büyük ve En Küçüğünü Söyleyen Program - ("max" ve "min" e girmek zorunda kaldım):
sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
sayi3 = int(input("Üçüncü sayıyı girin: "))

en_buyuk = max(sayi1, sayi2, sayi3)
en_kucuk = min(sayi1, sayi2, sayi3)

print(f"En büyük sayı: {en_buyuk}")
print(f"En küçük sayı: {en_kucuk}")

    # 12. 16-30 Yaş Arası, 3 Yıl Tecrübeli, Günde 5 Saat Çalışacak Adayları Seçen Program:
yas = int(input("Yaşınızı girin: "))
tecrube = int(input("Programlama alanında kaç yıl tecrübeniz var? "))
calisma_suresi = int(input("Günde kaç saat çalışabilirsiniz? "))

if 16 <= yas <= 30 and tecrube >= 3 and calisma_suresi >= 5:
    print("Aday kabul edilmiştir.")
else:
    print("Aday şartları sağlamıyor.")

# 13. Voleybol Takımına 7-12 Yaş Arası Kızlar Seçiliyor, Başvuru Yapılacak mı?
yas = int(input("Yaşınızı girin: "))
cinsiyet = input("Cinsiyetinizi girin (Kadın/Erkek): ")

if 7 <= yas <= 12 and cinsiyet.lower() == "kadın":
    print("Başvurunuz kabul edilmiştir.")
else:
    print("Başvurunuz kabul edilmemiştir.")

    # 14. Madeni Para Miktarına Göre Hangi Itemleri Alabileceğini Söyleyen Program:
para_miktari = int(input("Topladığınız madeni para miktarını girin: "))

if para_miktari >= 100:
    print("Yeterli madeni paranız var, hızlandırıcı alabilirsiniz.")
else:
    print("Yeterli madeni paranız yok.")

    # 15. Bir Bilmece Sorup Cevaba Göre Puan Verme Programı:
cevap = input("Çarşıdan Aldım Bir Tane Eve Geldim 1000 Tane Bil Bakalım Ne? ")

if cevap.lower() == "nar":
    print("Cevap doğru! Tebrikler!")
else:
    print("Cevabınız yanlış. Doğru cevap: nar.")