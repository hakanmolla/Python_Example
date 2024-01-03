kartSifresi="1923"
bakiye = 1000
denemeHakki=3
print("X Bankasına Hoşgeldinz...")
kart_islem_durumu=True
islemDurumu= True
while islemDurumu:
    girilenSifre = input("Kart Şifrenizi Giriniz...")
    if girilenSifre != kartSifresi:
        print("Yanlış Girdiniz Tekrar Giriniz...")
        denemeHakki -=1
        print(f"{denemeHakki},Deneme Hakkınız Kaldı")
        if denemeHakki == 0:
            print("Kartınız Blocklandı Bankda ile Görüşünüz ")
            islemDurumu =False
    else:
        print("------ Giriş Yapıldı.------")
        print("""
                  Yapılacak İşlemi Seçiniz
                  ------------------------
                  1-Para Çekme
                  2-Para Yatırma
                  3-Bakiye Sorgulama
                  4-Çıkış
                  """)
        while kart_islem_durumu :
            
            islemNo= input("işlem numarasını giriniz :")
            if islemNo == "4":
                print("Çıkış Yapıldı")
                islemDurumu=False
                kart_islem_durumu=False
            elif islemNo =="3":
                print(f"Toplam Bakiyeniz : {bakiye} ₺")
            elif islemNo =="2":
                yatirilacakMiktar = int(input("Yatırılacak Miktar\n"))
                bakiye += yatirilacakMiktar
                print(f"{yatirilacakMiktar} bakiyenize eklenmiştir Güncel bakiyeniz : {bakiye}")
            elif islemNo =="1":
                cekilecekMiktar = int(input("Çekilecek  Miktar\n"))
                if cekilecekMiktar > bakiye:
                    print("yetirli limitiniz Bulunmamaktadır. ")
                elif cekilecekMiktar <= bakiye:
                    bakiye -= cekilecekMiktar
                    print(f"{yatirilacakMiktar} bakiyenize eklenmiştir Güncel bakiyeniz : {bakiye}")
            
       
