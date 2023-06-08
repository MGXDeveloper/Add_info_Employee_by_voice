import tkinter
from tkinter import *
import pyttsx3
import speech_recognition as sr
from pydub.playback import play
from playsound import playsound
from gtts import gTTS
import qrcode
import time
import pyaudio
from tkinter import messagebox
from sqlite3 import *
import sqlite3
from tkinter import filedialog
screen=Tk()
db=sqlite3.connect('employs/EmployDate.db')
def employimage():
 global m

image=filedialog.askopenfilename(title='Employ_Image',filetypes=(('Image Files','*.png'),('All Files','*.png')))
mg=PhotoImage(image)
with open(image,"rb") as file:
  m=file.read()
  lm = Label(f1,text='✅',bg='white',fg='blue',font=('tagawal',14))
  lm.place(x=360, y=130, width=27, height=27)
def mysound():
  import speech_recognition as sr
  r = sr.Recognizer()
  with sr.Microphone() as src:
  print('Enter : ')
  r.adjust_for_ambient_noise(src, duration=1)
  myaudio = r.listen(src)
  mytext = r.recognize_google(myaudio,language=v.get())
  mytext = mytext.lower()
  print(mytext)
  return mytext
#CmmandsButton=================================
def B1():
  e1.delete(0, END)
  e1.insert(0,mysound())
def B2():
  e2.delete(0, END)
  e2.insert(0,mysound())
def B3():
  e3.delete(0, END)
  e3.insert(0, mysound())
def B4():
  e4.delete(0, END)
  e4.insert(0, mysound())
def Bs():
  db = sqlite3.connect('employs/EmployDate.db')
  name=e1.get()
  age=e2.get()
  job=e3.get()
  city=e4.get()
  db.execute("CREATE TABLE if not exists
  employs(Name,Age,Job,City,Image BLOB)")
  db.execute("insert into employs(Name,Age,Job,City,Image)
  Values(?,?,?,?,?)",(name,age,job,city,m))
  db.commit()
  db.close()
  messagebox.showinfo('Save','Save file')
  e1.delete(0, END)
  e2.delete(0, END)
  e3.delete(0, END)
  e4.delete(0, END)
 #stings========================================
  screen.title('تسجيل بيانات الموظفين')
  screen.geometry('400x500+800+200')
  screen.config(background='#2097DE')
  screen.resizable(0,0)
#Frames========================================
#\\\\\\\\\Frame1/////////
  f1=Frame(screen,background='silver',bg='#20AEDE')
  titleimage=PhotoImage(file='image/image4.png')
  res1=titleimage.subsample(4,6)
#(((((((((((Labels)))))))))))))
  ltm=Label(f1,image=res1,bg='#20AEDE')
  ltm.place(x=-5,y=1)
  l1=Label(f1,text='Employ_Image:',bg='#18E8B0',fg='black',font=('tagawa
  l',14,'bold'))
  l1.place(x=5,y=130)
  l2=Label(f1,text='Employ_Name
  :',bg='#18E8B0',fg='black',font=('tagawal',14,'bold'))
  l2.place(x=5,y=170)
  l3=Label(f1,text='Employ_Age
  :',bg='#18E8B0',fg='black',font=('tagawal',14,'bold'))
  l3.place(x=5,y=210)
  l4=Label(f1,text='Employ_Job
  :',bg='#18E8B0',fg='black',font=('tagawal',14,'bold'))
  l4.place(x=5,y=250)
  l5=Label(f1,text='Employ_City
  :',bg='#18E8B0',fg='black',font=('tagawal',14,'bold'))
  l5.place(x=5,y=290)
#(((((((((((Entry)))))))))))))
  e1=Entry(f1,font=('tagawal',14,'bold'))
  e1.place(x=170,y=170,width=182,height=27)
  e2=Entry(f1,font=('tagawal',14,'bold'))
  e2.place(x=170,y=210,width=182,height=27)
  e3=Entry(f1,font=('tagawal',14,'bold'))
  e3.place(x=170,y=250,width=182,height=27)
  e4=Entry(f1,font=('tagawal',14,'bold'))
  e4.place(x=170,y=290,width=182,height=27)
#(((((((((((Button)))))))))))))
  b1=Button(f1,text='🔊',bg='blue',fg='white',font=13,command=B1)
  b1.place(x=360,y=170,width=30,height=27)
  b2=Button(f1,text='🔊',bg='blue',fg='white',font=13,command=B2)
  b2.place(x=360,y=210,width=30,height=27)
  b3=Button(f1,text='🔊',bg='blue',fg='white',font=13,command=B3)
  b3.place(x=360,y=250,width=30,height=27)
  b4=Button(f1,text='🔊',bg='blue',fg='white',font=13,command=B4)
  b4.place(x=360,y=290,width=30,height=27)
  bm=Button(f1,text='📷',bg='blue',fg='white',font=13,command=employimage)
  bm.place(x=170,y=130,width=182,height=27)
  f1.place(x=5,y=7,width=390,height=350)
#\\\\\\\\\Frame2/////////
  f2=Frame(screen,background='#2B90C0')
  endimage=PhotoImage(file='image/image3.png')
  res2=endimage.subsample(1,2)
  ltm2=Label(f2,image=res2,bg='#2B90C0')
  ltm2.place(x=35,y=20)
  ls=Label(f2,text='File Save :',bg='silver',font=('tagawal',11,'bold'))
  ls.place(x=10,y=5)
#lan=Label(f2,text='Language : ',font=('tagawal',11,'bold'))
#lan.place(x=260,y=5)
  bs=Button(f2,text=' Save
  ✅',bg='blue',fg='white',font=('tagawal',11),command=Bs)
  bs.place(x=100,y=5,width=65,height=25)
#\\\\\\\\\\\\\\\\\\\\\\\\\\-LANGUAGE-///////////////////////////
  v=tkinter.StringVar()
  bl=Menubutton(f2,text='Language',bg='blue',fg='white',font=('tagawal',11))
  s=Menu(bl,tearoff=0)
  bl['menu']=s
  s.add_radiobutton(label=''العربية,variable=v,value='ar-AR')
  s.add_radiobutton(label='English',variable=v,value='en-EN')
  s.add_radiobutton(label='French',variable=v,value='fr-FR')
  bl.place(x=300,y=5,width=75,height=25)
  l_copy=Label(f2,text='Devloper_MGX',bg='#2B90C0',font=('tagawal',10))
  l_copy.place(x=150,y=110)
  f2.place(x=5,y=360,width=390,height=135)
  playsound('C:\\Users\\smart\\PycharmProjects\\employ\\sound\\wel.mp3')
  screen.mainloop()