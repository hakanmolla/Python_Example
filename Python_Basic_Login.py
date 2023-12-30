import tkinter as tk
arayuz = tk.Tk()
arayuz.title("Şifre")
arayuz.geometry("300x200")
KuAd ="Hakan"
KuSi = "123456"

kullanıcı = tk.Label(text="Kullanıcı Adı:")
kullanıcı.place(x=10,y=10)

y=tk.StringVar()
Kullanıcı_girisi = tk.Entry(textvariable=y)
Kullanıcı_girisi.place(x=100,y=10)

kullanıcı_sifre = tk.Label(text="Kullanıcı Şifresi:")
kullanıcı_sifre.place(x=10,y=35)

x=tk.StringVar()
Kullanıcı_girisi = tk.Entry(textvariable=x)
Kullanıcı_girisi.place(x=100,y=35)

dogru_yanlıs = tk.Label(text ="000",font="Verdana 30 bold")
dogru_yanlıs.place(x=100 ,y=95)

def giris_komut():
    KA=y.get()
    KS=x.get()
    print(KA,"----",KS)
    if KA == KuAd and KS== KuSi:
        print("Doğru")
        dogru_yanlıs.config(text="Dogru",fg="green")
    else:
        print("Yanlış")
        dogru_yanlıs.config(text="Yanlış",fg="red")

giris = tk.Button(text="Giriş ",command=giris_komut)
giris.place(x=135,y=70)

arayuz.mainloop()
