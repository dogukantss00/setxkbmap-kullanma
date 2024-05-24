from tkinter import *
from tkinter import messagebox,ttk
import subprocess


def degistir():
    try:
        dil=vombo.get()
        subprocess.run(["setxkbmap",dil], capture_output=True, text=True, check=True, bufsize=0)
        messagebox.showinfo("","başarılı")
        pencere1.destroy()
    except:
        messagebox.showerror("başarısız tekrar deneyin")
pencere1=Tk()
pencere1.geometry("400x300")
pencere1.title("KLAVYE DEĞİŞTİRME")

label1=Label(pencere1,text="LÜTFEN İTEDİĞİNİZ KLAVYE DİLİNİ SEÇİNİZ")
label1.place(x=50,y=100)
languages="tr","us","ar","zh","fr","en"
vombo=ttk.Combobox(pencere1,values=languages)
vombo.place(x=100,y=120)

buton=Button(pencere1,text="ONAYLA",command=degistir)
buton.place(x=150,y=150)

pencere1.mainloop()