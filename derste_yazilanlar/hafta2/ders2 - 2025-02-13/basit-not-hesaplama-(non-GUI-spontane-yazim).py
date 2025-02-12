def sor(soru, tip=int):
    check = False
    while check == False:
        cevap = input(soru + "\n")
        try:
            if cevap != "":
                if tip == str:
                    check = True
                    return str(cevap)
                elif tip == float:
                    check = True
                    return float(cevap)
                elif tip == int:
                    check = True
                    return int(cevap)
                else:
                    raise ValueError("Tip Hatası")
            else:
                return cevap
        except:
            print("Hatalı Bir Giriş Yaptınız\n")
            sor(soru, tip)
                
    
def not_kontrol(not1="", not2=""):
    if not1 == "" or not2 == "":
        return False
    else:
        if not1 < 0.0 or not1 > 100.0:
            raise ValueError("Notlar 0 ile 100 arasında olmalıdır")
        if not2 < 0.0 or not2 > 100.0:
            raise ValueError("Notlar 0 ile 100 arasında olmalıdır")
        return True

def hesap(not1="", not2="",):
    kontrol = not_kontrol(not1, not2)
    if kontrol == False:
        return "Hatalı Not Girişi"
    if not1 == "" and not2 == "":
        print("Notlarınızı Girmediğiniz İçin Ortalama Hesaplanamadı")
    elif not1 == "" and not2 != "":
        print("1. Notunuzu Girmediğiniz İçin Ortalama Hesaplanamadı")
    elif not1 != "" and not2 == "":
        print("2. Notunuzu Girmediğiniz İçin Ortalama Hesaplanamadı")
    else:
        ortalama = (not1 + not2) / 2
        if ortalama >= 50.0:
            return "Ortalama Notunuz: " + str(ortalama) + ", Geçtiniz"
        else:
            return "Ortalama Notunuz: " + str(ortalama) + ", Kaldınız"
        
def not_hesapla():
    ad = sor("Adınızı Giriniz", str)
    not1 = sor(f"Sayın {ad}, 1. Notunuzu Giriniz", float)
    not2 = sor(f"Sayın {ad}, 2. Notunuzu Giriniz", float)
    print(hesap(not1, not2))

    
not_hesapla()