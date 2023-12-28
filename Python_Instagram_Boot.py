import instaloader
import tkinter as tk
from tkinter import messagebox

def download_post():
    username = entry_username.get()
    
    try:
        bot = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(bot.context,username)
        posts = profile.get_posts()
        for index,post in enumerate(posts,1):
            bot.download_post(post,target=f"{profile.username}_{index}")
            
        messagebox.showinfo("Başarılı","Gönderiler indirildi.")
    except Exception as e:
        messagebox.showerror("Hata",str(e))
        
root = tk.Tk()
root.title("Instagram Gönderi indirici ")
root.geometry("300x200")
label = tk.Label(root,text="Kullanıcı Adı:")
label.pack(pady=10)
entry_username = tk.Entry(root)
entry_username.pack()
download_button = tk.Button(root,text="Bilgileri indir", command=download_post)
download_button.pack()





root.mainloop()


        
