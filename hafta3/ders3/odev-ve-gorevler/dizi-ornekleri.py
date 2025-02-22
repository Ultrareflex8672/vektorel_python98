dizi = [1, 2, 3, 4, 5]
print("Dizi elemanları:", dizi)

dizi = [5, 3, 1, 4, 2]
dizi.sort()
print("Sıralanmış dizi:", dizi)

dizi = [1, 2, 3]
dizi.append(4)
print("Eleman eklenmiş dizi:", dizi)

dizi = [1, 2, 3, 4, 5]
dizi.reverse()
print("Ters çevrilmiş dizi:", dizi)

dizi = [1, 2, 3, 4, 5]
toplam = sum(dizi)
print("Dizideki elemanların toplamı:", toplam)

dizi = [1, 2, 3, 4, 5]
ters_dizi = dizi[::-1]
print("Ters çevrilmiş dizi:", ters_dizi)

dizi = [10, 20, 30, 40, 50]
en_buyuk = max(dizi)
en_kucuk = min(dizi)
print("En büyük eleman:", en_buyuk)
print("En küçük eleman:", en_kucuk)

dizi = [5, 10, 15, 20, 25]
toplam = sum(dizi)
print("Dizideki elemanların toplamı:", toplam)

dizi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cift_sayilar = [x for x in dizi if x % 2 == 0]
print("Çift sayılar:", cift_sayilar)

dizi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tek_sayilar = [x for x in dizi if x % 2 != 0]
print("Tek sayılar:", tek_sayilar)