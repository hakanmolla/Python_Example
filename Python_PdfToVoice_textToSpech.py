import PyPDF2 
from gtts import gTTS
import os 
import tkinter as tk
from tkinter import filedialog

def pdf_metin_cikart(pdf_yolu):
    metin=""
    pdf_okuyucu = PyPDF2.PdfReader(open(pdf_yolu,"rb"))
    for sayfa_num in range(len(pdf_okuyucu.pages)):
        metin +=pdf_okuyucu.pages[sayfa_num].extract_text()
    return metin
## metini sesli hale getiren fonksiyon

def metni_sese_cevir(metin,cikti_dosyasi):
    sesli_cevirici = gTTS(text=metin,lang='tr')
    sesli_cevirici.save(cikti_dosyasi)
    
## dosya secme fonksiyonu
def dosya_sec():
    dosya_yolu= filedialog.askopenfilename(filetypes=[("Pdf Dosyaları","*.pdf Secebilir.")])
    if dosya_yolu:
        pdf_metin=pdf_metin_cikart(dosya_yolu)
        metni_sese_cevir(pdf_metin,"Kaydet.mp3")
        os.system("start Kaydet.mp3")
        
#tkinter arayüz
app=tk.Tk()
app.geometry("250x150")
app.title="Sesli Kitap Uygulaması"
secim_button = tk.Button(app,text="PDF seç",command=dosya_sec,padx=20,pady=20)
secim_button.pack(pady=20)


app.mainloop()
    
    
    
