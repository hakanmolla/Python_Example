from tkinter import Label
from tkinter import Tk
import time

def digital_clock():
    #saat alanı
    time_live= time.strftime("%H:%M:%S")
    label.config(text=time_live)
    #tarih alanı
    date_info=time.strftime("%d %B %Y")
    date_label.config(text=date_info)
    label.after(200,digital_clock)

app_windows = Tk()
app_windows.title("Dijital Saat")
app_windows.geometry("500x200")
app_windows.resizable(0,0)
app_windows.configure(bg="black")

text_font = ("Boulder",36,'bold')
background = "black"
foreground = "white"
border_widht = 20

# saat Etiketi

label = Label(app_windows,font=text_font,bg=background,fg=foreground)
label.grid(row=0,column=1,padx=border_widht,pady=10)

# Tarih Etiketi
date_label= Label(app_windows,font=text_font,bg=background,fg=foreground)
date_label.grid(row=1,column=1,padx=border_widht,pady=10)



digital_clock()
app_windows.mainloop()
