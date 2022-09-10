from tkinter import *       # pip install SpeechRecognition 
from pytube import YouTube    # pip install SpeechRecognition

root=Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"200x200+{(1120//2)-100}+{(580//2)-100}")
root.resizable(600,600)
root.title("Youtube Video İndir")

link=StringVar()
Label(root,text="Linki Yapıştır",font="arial 15 bold").place(x=160,y=60)
link_enter=Entry(root,width=70,textvariable=link).place(x=32,y=90)

def Downloader():
    url=YouTube(str(link.get()))
    video=url.streams.get_highest_resolution()
    video.download("G:\YAZILIM\Video İndir Pyhton")
    Label(root,text="İndirildi!",font="arial 15").place(x=200,y=120)
Button(root,text="İndir",font="arial 15 bold",bg="pale violet red",padx=2,command=Downloader).place(x=350,y=120)
root.mainloop
