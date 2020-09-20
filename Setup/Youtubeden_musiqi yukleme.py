import youtube_dl
import tkinter as tk
from tkinter import *
from tkinter import messagebox,filedialog

def CreatWidgets():
    linkLabel=Label(root,text="Youtube Linki   : ",bg="turquoise4")
    linkLabel.grid(row=1,column=0,pady=5,padx=5)

    root.linkText=Entry(root,width=55,textvariable=videoLink)
    root.linkText.grid(row=1,column=1,pady=5,padx=5,columnspan=2)

    destinationLabel=Label(root,text="Yuklenecek Yer  : ",bg="turquoise4")
    destinationLabel.grid(row=2,column=0,pady=5,padx=5)

    root.destinationText=Entry(root,width=38,textvariable=downloadPath)
    root.destinationText.grid(row=2,column=1,pady=5,padx=5)

    browseButton=Button(root,text="Daxil et",command=Browse,width=20)
    browseButton.grid(row=2,column=2,pady=5,padx=5)

    dwldButton=Button(root,text="Musiqini Yukle",command=Download,width=30)
    dwldButton.grid(row=3,column=1,pady=5,padx=5)

def Browse():
    dwldDirectory=filedialog.askdirectory(initialdir="/Users/abhijithwarrier/Downloads/Music")
    downloadPath.set(dwldDirectory)

def Download():
    yt_link=videoLink.get()
    dwldFolder=downloadPath.get()

    audDWLDopt={
        'format':'bestaudio/best',
        'outtmpl':dwldFolder+"/%(title)s.%(ext)s",
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality':'320'
            }],
        }
    with youtube_dl.YoutubeDL(audDWLDopt)as aud_dwld:
        aud_dwld.download([yt_link])
        
    messagebox.showinfo("Tebrikler",  "Musiqi yuklenildi")

root=tk.Tk()
root.geometry("650x120")
root.resizable(False,False)
root.title("Youtubeden Musiqi yukleme")
root.config(background="turquoise4")

videoLink=StringVar()
downloadPath=StringVar()
CreatWidgets()

root.mainloop()









