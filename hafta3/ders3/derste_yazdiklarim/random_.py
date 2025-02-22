import random

def rasgele_sec(liste):
    secim = random.choice(liste)
    return secim   # Değeri döndür

liste = ["taş", "kağıt", "makas"]

secim = rasgele_sec(liste)
print(secim)
