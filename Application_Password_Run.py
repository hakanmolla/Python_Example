import subprocess as sp
import time

psw="123456"
Kullanici_şifresi=input("Lütfen Şifre giriniz. ")

while True:
    print ("****Uygulama Çalıştırmaya Hoşgeldiniz*****")
    print ("Şifre kontrolu yapılıyor")
    time.sleep(2)
    if psw == Kullanici_şifresi:
        secim_yap= input("11-Notepad\n2-comandline\n3-hesap makinesi\n4-system kontrol\n")
        
        if secim_yap == "1":
            sp.call("notepad.exe")
            input("devam Edilsin mi ?")
        elif secim_yap =="2":
            sp.call("cmd.exe")
            input("devam Edilsin mi ?")
        elif secim_yap =="3":
            sp.call("calc.exe")
            input("devam Edilsin mi ?")
        elif secim_yap =="4":
            sp.call("msconfig.exe")
            input("devam Edilsin mi ?")
    else:
        print("Hatalı şifre girdiniz...")
        for i in range(3):
            Kullanici_şifresi=input("Lütfen Şifre giriniz. ")
            if psw == Kullanici_şifresi:
                break
            else:
                print(i)
                if i == 2 :
                    break
                continue
        if psw != Kullanici_şifresi:
            print("Çok fazla hatalı giriş yaptınız")
            break
            
         
            
    
