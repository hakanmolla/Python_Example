import time
import subprocess as sp

Db_Kul_Adı = "hakan"
Db_Kul_Sif = "molla"
print("*********** Kullanıcı Login Safyasına Hoş Geldiniz... ***********")
kul_adi = input("Lütfen Kullanıcı Adınızı Giriniz !!!\n")
kul_sif = input("Lütfen Kullanıcı Şifrenizi Giriniz !!!\n")

def Sifre_kontrol(new_sifre):
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*']
    karater_buyuk_harf_status =""
    karater_kucuk_harf_status =""
    karater_rakam =""
    special_characters_status =""
    karater_uzun =""
    for karakter in new_sif:
        if karakter in special_characters:
            special_characters_status = "yes"
            break
    for karater in new_sif:
        if karater.isupper():
            karater_buyuk_harf_status = "yes"
        elif karater.islower():
            karater_kucuk_harf_status = "yes"
        elif any(char.isdigit() for char in new_sif):
            karater_rakam= "yes"                  
    if len(new_sif) >= 8 :
         karater_uzun = "yes"
               
    if karater_buyuk_harf_status== "yes" and karater_kucuk_harf_status == "yes" and karater_rakam == "yes" and special_characters_status == "yes" and karater_uzun == "yes":
        Db_Kul_Sif = new_sif
        print (f"Şifreniz {new_sif} olarak Güncellenmiştir..." )
        yanıt=True
        return yanıt
    else:
        print("Girdiğiniz Şifre Şifre Politikasına uymadığından dolayı İşleminiz yapılmamıştır.\n ")
        print(f"Şifreni en az 8 karakter / Büyük ve Küçük Harf / Rakam ve Özel Karater olmalıdır. {special_characters} \n ")
        yanıt=False
        return yanıt

def User_login(kul_adi,kul_sif):
    if Db_Kul_Adı == kul_adi and Db_Kul_Sif == kul_sif:
        print ("Şifre kontrolu yapılıyor.....")
        time.sleep(1)
        print("Tebrik ederiz Kullanıcı Adı ve Şifresniz Doğrudur.")
        return True
    elif Db_Kul_Adı != kul_adi and Db_Kul_Sif == kul_sif:
        print("Üzgünüz Kullanıcı Adınız Yanlıştır...")
        return False
    elif Db_Kul_Sif != kul_sif and Db_Kul_Adı == kul_adi :
        print ("Üzgünüz Kullanıcı Şifreniz Yanlıştır.....")
        return False
    else:
        print("Girmiş olduğunuz Kullanıc Adı ve Kullanıcı Şifresi Yanlıştır.")
        return False
          
if User_login(kul_adi,kul_sif) :
    print ( "Giriş sayfasına hoşgeldiniz.")
    secim_yap= input("1-Kullanıcı Şifrenizi Değiştirin\n2-Not Defterini Çalıştırın\n3-Çıkış Yap\n")
    while True:
        if secim_yap == "1":
                print ("#"*45)
                print("Kullanıcı Şifrenizi Değiştirmek için Lütfen Şifre Giriniz.\n")
                print("Kullanıcı Şifrenizde Mim 8 Karakter,Özel Karakter,Sayılardan, Büyük ve Küçük Harfler Oluştuğuna Dikkat Ediniz. ")
                print ("#"*45)
                new_sif = input("Lütfen yeni Şifrenizi Giriniz.")
                if Sifre_kontrol(new_sif):
                    print("Şifre uygun.")
                    break
        elif secim_yap == "2":
            sp.call("notepad.exe")
            input("devam Edilsin mi ?")
        elif secim_yap == "3":
            print("Cıkış İşlemi Yapılıyor Görüşmek Üzere ")
            time.sleep(1)
            print("!!!!! BYE BYE !!!!! ")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")
            input()
            continue
