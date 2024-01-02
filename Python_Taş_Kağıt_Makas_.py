## Taş Kağıt Makas Oyunu : 
import random

def pc_secim(kullanici_secimi):
 bilgisayar_secimi = random.choice(["Taş", "Kağıt", "Makas"])
 if kullanici_secimi == bilgisayar_secimi:
    print(f"Berabere! // Bilgisayar secimi : {bilgisayar_secimi} // Kullanıcı Secimi : {kullanici_secimi}\n")
 elif (kullanici_secimi == "Taş" and bilgisayar_secimi == "Makas") :
    print(f"Kazandınız! // Bilgisayar secimi : {bilgisayar_secimi} // Kullanıcı Secimi : {kullanici_secimi}\n")
 elif (kullanici_secimi == "Kağıt" and bilgisayar_secimi == "Taş") :
    print(f"Kazandınız! // Bilgisayar secimi : {bilgisayar_secimi} // Kullanıcı Secimi : {kullanici_secimi}\n")
 elif (kullanici_secimi == "Makas" and bilgisayar_secimi == "Kağıt"):
    print(f"Kazandınız! // Bilgisayar secimi : {bilgisayar_secimi} // Kullanıcı Secimi : {kullanici_secimi}\n")
 else:
    print(f"Bilgisayar Kazandı! // Bilgisayar secimi : {bilgisayar_secimi} // Kullanıcı Secimi : {kullanici_secimi}\n")
   

while True:
    
    while True:
        print("******** Taş-Kağıt-Makas Oyununa HoşGeldiniz... ******")
        print("---------- Secim Yapınız --------------")
        try:
            secim = int(input("1-Taş\n2-Kağıt\n3-Makas\n4-oyunu bırak\n"))
            break
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı giriniz.")
        
    if secim == 1:
        kullanici_secimi = "Taş"
        pc_secim(kullanici_secimi)
    elif secim == 2:
        kullanici_secimi = "Kağıt"
        pc_secim(kullanici_secimi)
    elif secim == 3 :
        kullanici_secimi = "Makas"
        pc_secim(kullanici_secimi)
    elif secim == 4:
        print("Oyunu bıraktınız.")
        break
    else:
        print("Lütfen Gecerli bir sayısı giriniz. ")
    
