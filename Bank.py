import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random
import sys
from functools import partial
import speech_recognition as sr
cred = credentials.Certificate("ai-sdp1.json")
firebase_admin.initialize_app(cred,{
	    'databaseURL': 'https://ai-sdp1-default-rtdb.firebaseio.com/'
	})
FdbRefVap = db.reference('/')
from tkinter import *
import pyttsx3
root=Tk()
root.title("Bank")
root.geometry("400x400")

def num(num):
  rev=0
  number=int(num)
  while (number > 0):   
    remainder = number % 10  
    rev = (rev * 10) + remainder  
    number = number // 10  
  return rev

def speak(txt):
  engine=pyttsx3.init()
  engine.say(txt)
  engine.runAndWait()
  
def listen():
  r = sr.Recognizer()
  while(1):	
    try:
      with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2, duration=0.2)
        audio2 = r.listen(source2)
        MyText = r.recognize_google(audio2)
        name = MyText
        name=name.capitalize()
        return name
    except sr.RequestError as e:
      r1011=Tk()
      r1011.title("Error listen")
      r1011.geometry("400x400")
        
    except sr.UnknownValueError:
      r1011=Tk()
      r1011.title("Error listen")
      r1011.geometry("400x400")
      

def start():
  r1=Tk()
  r1.title("Banking")
  r1.geometry("400x400")
  label=Label(r1,text="You want to ")
  label.grid(row=1,column=0)
  s1=Button(r1,text="Type your name",command=typeit)
  s1.grid(row=2,column=2)
  s2=Button(r1,text="Say your name",command=sayit)
  s2.grid(row=3,column=2)
  r1.mainloop()
  
def end():
  speak("Thank you for using Smart ATM Machine")
  sys.exit()
def loggedin(n):
  user="Welcome "+n
  speak(user)
  fbv = FdbRefVap.child(n).get()
  def withdraw():
    def otp():
      def submit():
        r222=Tk()
        r222.title(n+" Withdraw Amount")
        r222.geometry("400x400")
        l12=Label(r222,text="Enter Amount")
        l12.grid(row=2,column=0)
        nd = Entry(r222,width=30)
        nd.grid(row=2,column=1)
        def submit1():
          r2222=Tk()
          r2222.title(n+" Withdraw Amount PRocess Completed")
          r2222.geometry("400x400")
          de=int(nd.get())
          d=int(fbv["Deposited"])
          if(de<=d):
            money=d
            e=d-de
            FdbRefVap.child(n).update({"Deposited":e})
            eee=("Successfully withdrawn amount")
            e1=(e)
            e11=eee+" "+str(de)
            la12=Label(r2222,text=e11)
            la12.grid(row=1,column=0)
            eee1=("Available Balance is") 
            e12=eee1+" "+str(e)
            la12=Label(r2222,text=e12)
            la12.grid(row=3,column=0)
          else:
            eee=("Insufficient Balance")
            e1=str(fbv["Deposited"])
            e11=eee+"   "+e1
            l12=Label(r2222,text=e11)
            l12.grid(row=6,column=0)

        sxz=Button(r222,text="Submit",command=submit1)
        sxz.grid(row=4,column=2)
  
      fbv = FdbRefVap.child(n).get()
      p=key.get()
      if(p==str(fbv["OTP"])):
        r221=Tk()
        r221.title(n+" Withdraw")
        r221.geometry("400x400")
        sa=Button(r221,text="Savings Account",command=submit)
        sa.grid(row=1,column=2)
        sz=Button(r221,text="Current Account",command=submit)
        sz.grid(row=2,column=2)
      else:
        r001=Tk()
        r001.title(n+"Withdraw wrong OTP")
        r001.geometry("400x400")
        label001=Label(r001,text="Wrong OTP")
        label001.grid(row=2,column=0)

    l=0
    i=0
    r250=Tk()
    r250.title(n+" OTP")
    r250.geometry("400x400")
    while(l==0 and i<3):
      i+=1
      num = random.randint(500000,1000000)
      FdbRefVap.child(n).update({"OTP":num})
      label2=Label(r250,text="OTP")
      label2.grid(row=2,column=0)
      key=Entry(r250,width=30)
      key.grid(row=2,column=1)
      keys=key.get()
      s=Button(r250,text="Submit",command=otp)
      s.grid(row=3,column=2)
      
            
            
                
        
        
        
          
  def balance():
    r121=Tk()
    r121.title(n+" Balance")
    r121.geometry("400x400")
    fbv = FdbRefVap.child(n).get()
    balabel1=Label(r121,text="Balance")
    balabel1.grid(row=1,column=0)
    balabel1=Label(r121,text=fbv["Deposited"])
    balabel1.grid(row=1,column=1)
    
  def profile():
    r21=Tk()
    r21.title(n+"Profile")
    r21.geometry("400x400")
    fbv = FdbRefVap.child(n).get()
    z=0
    for x in fbv:
      label1=Label(r21,text=x)
      label1.grid(row=z,column=0)
      z+=1
    z=0
    for x in fbv:
      label1=Label(r21,text=fbv[x])
      label1.grid(row=z,column=1)
      z+=1
  def ec():
      def submit():
        def submit1():
          r23=Tk()
          r23.title(n+"Email Change")
          r23.geometry("400x400")
          neweid=key11.get()
          while((not '@' in neweid) or (neweid.isdigit())):
            label12=Label(r23,text="Email")
            label12.grid(row=2,column=0)
            neweid = Entry(r23,width=30)
            neweid.grid(row=2,column=1)
          ccc=("Email Id is accepted")
          label2=Label(r23,text=ccc)
          label2.grid(row=1,column=0)
          FdbRefVap.child(n).update({"Email_ID":neweid})
        r22=Tk()
        r22.title(n+"Email Change OTP 1")
        r22.geometry("400x400")
        fbv = FdbRefVap.child(n).get()
        p=key.get()
        
        if(p==str(fbv["OTP"])):
          label2=Label(r22,text="Email")
          label2.grid(row=2,column=0)
          key11=Entry(r22,width=30)
          key11.grid(row=2,column=1)
          xyz=key11.get()
          s=Button(r22,text="Submit",command=submit1)
          s.grid(row=3,column=2)
        else:
          r1001=Tk()
          r1001.title(n+"Email wrong OTP")
          r1001.geometry("400x400")
          label1001=Label(r1001,text="Wrong OTP")
          label1001.grid(row=2,column=0)

      l=0
      i=0
      r25=Tk()
      r25.title(n+" Email Change OTP")
      r25.geometry("400x400")
      while(l==0 and i<3):
        i+=1
        num = random.randint(500000,1000000)
        FdbRefVap.child(n).update({"OTP":num})
        label2=Label(r25,text="OTP")
        label2.grid(row=2,column=0)
        key=Entry(r25,width=30)
        key.grid(row=2,column=1)
        keys=key.get()
        s=Button(r25,text="Submit",command=submit)
        s.grid(row=3,column=2)
  def pc():
    def submit():
      def submit1():
        r23=Tk()
        r23.title(n+"Password Change")
        r23.geometry("400x400")
        newpass=str(key11.get())
        nnn=len(newpass)
        l=0
        i=0
        while((n ==4)):
            label12=Label(r23,text="Password")
            label12.grid(row=2,column=0)
            newpass = Entry(r23,width=30)
            newpass.grid(row=2,column=1)   
        ccc=("Password is accepted")
        label2=Label(r23,text=ccc)
        label2.grid(row=1,column=0)
        FdbRefVap.child(n).update({"Password":newpass})
        
      r22=Tk()
      r22.title(n+"Password Change OTP 1")
      r22.geometry("400x400")
      fbv = FdbRefVap.child(n).get()
      p=key.get()
      if(p==str(fbv["OTP"])):
        label2=Label(r22,text="Password")
        label2.grid(row=2,column=0)
        key11=Entry(r22,width=30)
        key11.grid(row=2,column=1)
        xyz=key11.get()
        s=Button(r22,text="Submit",command=submit1)
        s.grid(row=3,column=2)
      else:
        r2001=Tk()
        r2001.title(n+"Password wrong OTP")
        r2001.geometry("400x400")
        label1001=Label(r2001,text="Wrong OTP")
        label1001.grid(row=2,column=0)

    l=0
    i=0
    r25=Tk()
    r25.title(n+" Password Change OTP")
    r25.geometry("400x400")
    while(l==0 and i<3):
      i+=1
      num = random.randint(100000,500000)
      FdbRefVap.child(n).update({"OTP":num})
      label2=Label(r25,text="OTP")
      label2.grid(row=2,column=0)
      key=Entry(r25,width=30)
      key.grid(row=2,column=1)
      keys=key.get()
      s=Button(r25,text="Submit",command=submit)
      s.grid(row=3,column=2)

  def mnc():
    def submit():
      def submit1():
        r23=Tk()
        r23.title(n+"Mobile Number Change")
        r23.geometry("400x400")
        newpass=str(key11.get())
        nnn=len(newpass)
        l=0
        i=0
        while((n ==10)):
            label12=Label(r23,text="Mobile Number")
            label12.grid(row=2,column=0)
            newpass = Entry(r23,width=30)
            newpass.grid(row=2,column=1)   
        ccc=("Mobile Number is accepted")
        label2=Label(r23,text=ccc)
        label2.grid(row=1,column=0)
        FdbRefVap.child(n).update({"Mobile_No":newpass})
        
      r22=Tk()
      r22.title(n+"Mobile Number Change OTP 1")
      r22.geometry("400x400")
      fbv = FdbRefVap.child(n).get()
      p=key.get()
      if(p==str(fbv["OTP"])):
        label2=Label(r22,text="Mobile Number")
        label2.grid(row=2,column=0)
        key11=Entry(r22,width=30)
        key11.grid(row=2,column=1)
        xyz=key11.get()
        s=Button(r22,text="Submit",command=submit1)
        s.grid(row=3,column=2)
      else:
        r3001=Tk()
        r3001.title(n+"Number wrong OTP")
        r3001.geometry("400x400")
        label3001=Label(r3001,text="Wrong OTP")
        label3001.grid(row=2,column=0)

    l=0
    i=0
    r25=Tk()
    r25.title(n+" Mobile Number Change OTP")
    r25.geometry("400x400")
    while(l==0 and i<3):
      i+=1
      num = random.randint(100000,500000)
      FdbRefVap.child(n).update({"OTP":num})
      label2=Label(r25,text="OTP")
      label2.grid(row=2,column=0)
      key=Entry(r25,width=30)
      key.grid(row=2,column=1)
      keys=key.get()
      s=Button(r25,text="Submit",command=submit)
      s.grid(row=3,column=2)

    
  r11=Tk()
  r11.title(n+"Account")
  r11.geometry("400x400")
  s1=Button(r11,text="Profile",command=profile)
  s1.grid(row=1,column=2)
  s2=Button(r11,text="Email Change",command=ec)
  s2.grid(row=2,column=2)
  s3=Button(r11,text="Password Change",command=pc)
  s3.grid(row=3,column=2)
  s4=Button(r11,text="Mobile Number Change",command=mnc)
  s4.grid(row=4,column=2)
  s5=Button(r11,text="Balance",command=balance)
  s5.grid(row=5,column=2)
  s6=Button(r11,text="Withdraw",command=withdraw)
  s6.grid(row=6,column=2)
  s7=Button(r11,text="Exit",command=end)
  s7.grid(row=7,column=2)
def typeit():
  def submit():
    def balance():
      r11121=Tk()
      r11121.title(key.get()+" Balance")
      r11121.geometry("400x400")
      fbv = FdbRefVap.child(key.get()).get()
      balabel1=Label(r11121,text="Balance")
      balabel1.grid(row=1,column=0)
      balabel1=Label(r11121,text=fbv["Deposited"])
      balabel1.grid(row=1,column=1)
    fbv = FdbRefVap.child(key.get()).get()
    revn=str(num(int(key1.get())))
    if(key.get()==fbv["Username"] and key1.get()==fbv["Password"]):
      loggedin(key.get())
    
    elif(key.get()==fbv["Username"] and revn == fbv["Password"]):
      balance()
  r=Tk()
  r.title("Login")
  r.geometry("400x400")
  label=Label(r,text="Username")
  label.grid(row=1,column=0)
  key=Entry(r,width=30)
  key.grid(row=1,column=1)
  label1=Label(r,text="Password")
  label1.grid(row=2,column=0)
  key1=Entry(r,width=30, show = '*')
  key1.grid(row=2,column=1)
  s3=Button(r,text="Submit",command=submit)
  s3.grid(row=3,column=2)
  r.mainloop()
def password(n):
  
  def submit():
    
    def balance():
      
      r11121=Tk()
      r11121.title(n+" Balance")
      r11121.geometry("400x400")
      fbv = FdbRefVap.child(n).get()
      balabel1=Label(r11121,text="Balance")
      balabel1.grid(row=1,column=0)
      balabel1=Label(r11121,text=fbv["Deposited"])
      balabel1.grid(row=1,column=1)
    fbv = FdbRefVap.child(n).get()
    revn=str(num(int(key1.get())))
    if(n==fbv["Username"] and key1.get()==fbv["Password"]):
      loggedin(n)
    elif(key.get()==fbv["Username"] and revn == fbv["Password"]):
      balance()
  r3=Tk()
  r3.title(n+" Login")
  r3.geometry("400x400")
  label1=Label(r3,text="Password")
  label1.grid(row=2,column=0)
  key1=Entry(r3,width=30, show = '*')
  key1.grid(row=2,column=1)
  s3=Button(r3,text="Submit",command=submit)
  s3.grid(row=3,column=2)
    
def sayit():
  r2=Tk()
  r2.title("Login")
  r2.geometry("400x400")
  label1=Label(r2,text="Please say your name")
  label1.grid(row=1,column=0)
  speak("Please Say Your User Name")
  n=listen()
  label2=Label(r2,text="Is your name"+n)
  label2.grid(row=2,column=0)
  s4=Button(r2,text="YES",command=password(n))
  s4.grid(row=3,column=1)
  s5=Button(r2,text="NO",command=typeit)
  s5.grid(row=3,column=2)
  r2.mainloop()
speak("Welcome TO ATM Machine")
s=Button(root,text="Start",command=start)
s.grid(row=3,column=2)
root.mainloop()


