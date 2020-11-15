import smtplib  as s
from tkinter import*
import tkinter as tk
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import re
import pyttsx3
import speech_recognition as sr #for speech  recognize
import webbrowser

from collections import defaultdict

master=Tk()
master.geometry("850x700")
master.title('Email sender')

background_image= PhotoImage(file = "1.png")
background_label = Label(master, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1) 

var1=StringVar()
var2=StringVar()
var3=StringVar();
var4=StringVar();
l,doc=[],[]
message_send=[]
send_count=0
doc_count=0
mess_count=0
store_all_data=defaultdict(list)

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def send():
    print(l)
    e1=var1.get()
    if message_send!=[]:
        m1=message_send[0]
    else:
        m1=[]
    c=0
    Corect_email=Enter your email address (// "abc@gmail.com")
    pic,file1={},{}
    pic={'jpg':1,'png':1,'gif':1,'jpeg':1}
    file1={'pdf':1,'csv':1,'xps':1,'txt':1,'ppt':1,'docx':1,'py':1,'rar':1}
    for email1 in range(len(l)):
        text=""
        if re.search(regex,e1) and re.search(regex,l[email1]) and len(m1)>0 and len(doc)>0 and len(subj.get())>0:
            # Log in to server using secure context and send email
            obj1=s.SMTP('smtp.gmail.com',587)
            obj1.starttls();

            # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = e1
            message["To"] = l[email1]
            message["Subject"] =subj.get()

            # Add body to email
            message.attach(MIMEText(m1, "plain"))

            if  Corect_email==e1:
                for i in doc:
                    extension=i.split('.')
                    print(i,extension)
                    if extension[1]  in file1:
                        with open(i, "rb") as attachment:
                            # Add file as application/octet-stream
                            # Email client can usually download this automatically as attachment
                            part = MIMEBase("application", "octet-stream")
                            part.set_payload(attachment.read())
                        encoders.encode_base64(part)
                        part.add_header("Content-Disposition",f"attachment; filename= {i}",)
                        message.attach(part)
                        #convert message to string
                    elif extension[1] in pic:
                        img_data = open(i,'rb').read()
                        image = MIMEImage(img_data, name=os.path.basename(i))
                        message.attach(image)
                c=c+1
                text = message.as_string()
                obj1.login(Corect_email,Enter your password #example : "abh4555")
                obj1.sendmail(e1,l[email1],text)

                obj1.quit();

            else:
                global pop_up1
                pop_up1= Toplevel(master)
                pop_up1.title("Some error")
                pop_up1.configure(bg='black')
                pop_up1.geometry("250x200")
                Label(pop_up1, text="Something is wrong please Check :-(",fg='Blue').pack()
                Button( pop_up1, text="OK", command=error1,fg='blue',bg='Blue',background='Red').pack()
                break;

    if len(l)==c and len(l)!=0:
        global pop_up2
        pop_up2= Toplevel(master)
        pop_up2.title("Some error")
        pop_up2.geometry("250x200")
        pop_up2.configure(bg='black')
        Label(pop_up2, text="Send Successfully :-)",fg='Blue').pack()
        Button( pop_up2, text="OK", command=error2,fg='blue',bg='pink',background='Red').pack()
    else:
        global pop_up4
        pop_up4= Toplevel(master)
        pop_up4.title("Some error")
        pop_up4.geometry("250x200")
        pop_up4.configure(bg='Black')
        Label(pop_up4, text="Something is wrong please Check :-(",fg='Blue').pack()
        Button( pop_up4, text="OK", command=error4,fg='blue',bg='pink',background='Red').pack()

def error():
    pop_up.destroy()
    return
def error1():
    pop_up1.destroy()
    return

def error2():
    pop_up2.destroy()
    return

def error4():
    pop_up4.destroy()
    return

def cancel():
    master.destroy()

def add():
    e2=var2.get()
    store_all_data["receiver email address"].append(e2)
    l.append(e2)
    receiver.delete(0, END)
    receiver.insert(0, "")
    return

def Clear():
    l.clear()
    try:
        del store_all_data["receiver email address"]
    except:
        print("Please check all fields, Something is missing")
    global send_count;
    send_count=0
    receiver.delete(0, END)
    receiver.insert(0, "")
    send_count=0
    return
    
def Stop_Adding():
    global send_count
    e2=var2.get()
    if send_count==0:
        store_all_data["receiver email address"].append(e2)
        l.append(e2)
    send_count=1  
    return

def add1():
    e4=var4.get()
    doc.append(e4)
    store_all_data["document added is"].append(e4)
    docu.delete(0, END)
    docu.insert(0, "")
    return

def Clear1():
    doc.clear()
    try:
        del store_all_data["document added is"]
    except:
        print("Please check all fields, Something is missing")
    global doc_count;
    doc_count=0
    docu.delete(0, END)
    docu.insert(0, "")
    #print('doc_count',doc_count)
    return 
    

def Stop_Adding1():
    global doc_count
    e4=var4.get()
    if doc_count==0:
        store_all_data["document added is"].append(e4)
        doc.append(e4)
    doc_count=1
    return 
information=defaultdict(list)
information={"who made you":"I have made by Abhishek Jaiswal", "what is your name":"My name is , Voice control Email sender  5.0 version","tell about the library in you":"smtplib , email , pyttsx3 , speech_recognition, tkinter","what is special in you":"I m special because     i am controlable by  voice or   by  just  giving    command","how do you work": "There are some library present in me   by  which i am  able to hear and speak   for example  ,  pyttsx3 and speech recognition and    one more thing   ,  you have to install   PyAudio file also    as per the version and   how many bit  of python    you have installed  in  your  pc  "}  

def Read(text):
    read_doc=[]
    read1=[]
    for i in store_all_data:
        read1.append(i)
        for j in store_all_data[i] :
            read1.append(j)
        read_doc.append(read1)
        read1=[]
    print(read_doc)
    
    engine=pyttsx3.init()   # initialize
    engine.setProperty('rate',140) # for speed or  rate
    voices = engine.getProperty('voices')       #getting details of current voice
     #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[1].id)# for setting the rule
    print(store_all_data)
    print(information)
    if text==4:
        engine.say(read_doc) 

    elif text==1:
        engine.say("Speak anything") 

    elif text==2:
        engine.say("Sorry could not recognize what you said ") 
        #time.sleep(4)
    elif text in information:
        print("in")
        engine.say(information[text])
    else:
        print(text)
        print(text in store_all_data)
        if text in store_all_data:
            engine.say(store_all_data[text])  
        else:
            engine.say("Please say more clearly")  
        
    
                     # data fetch form entry  box
    engine.runAndWait()
    return 
    #print(store_all_data)
    
def Done_sender():
    #print(var1.get())
    store_all_data["sender email address"].append(var1.get())
Done_sub=0
def Done_subject():
    global Done_sub
    if Done_sub==0:
        store_all_data["subject"].append(var3.get())
        Done_sub+=1


def Done_mess():
    global mess_count
    if mess_count==0:
        s=""
        result=mess.get(1.0, tk.END+"-1c")
        for i in result:
            if i!='\n':
                s=s+i
            else:
                s=s+" "
        message_send.append(s)
        mess_count+=1
        store_all_data["message is"].append(s)

def callback(url):
    webbrowser.open_new(url)

def change_dropdown(*args):
    root = Toplevel(master)
    root.geometry('270x250')
    background_image2= PhotoImage(file = "b11.png")
    background_label1 = Label(root, image=background_image2)
    background_label1.place(x=0, y=0, relwidth=1, relheight=1) 
    l=Label(root,text="ALL LINKS ARE HERE",font=5,fg='blue',background="Yellow")
    l.pack()
    link1 = Label(root, text="Speech recognition ", fg="blue", cursor="hand2",font=4)
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://pypi.org/project/SpeechRecognition/"))

    link2 = Label(root, text="Simple Mail transfer protocol", fg="blue", cursor="hand2",font=4)
    link2.pack()
    link2.bind("<Button-1>", lambda e: callback("https://docs.python.org/3/library/smtplib.html"))

    link3 = Label(root, text="Email  ", fg="blue", cursor="hand2",font=4)
    link3.pack()
    link3.bind("<Button-1>", lambda e: callback("https://pypi.org/project/email-to/"))

    link4 = Label(root, text="Text-To-Speech conversion", fg="blue", cursor="hand2",font=4)
    link4.pack()
    link4.bind("<Button-1>", lambda e: callback("https://pypi.org/project/pyttsx3/"))

    link5 = Label(root, text="Tkinter ", fg="blue", cursor="hand2",font=4)
    link5.pack()
    link5.bind("<Button-1>", lambda e: callback("https://docs.python.org/3/library/tkinter.html"))

    link6= Label(root, text="PyAudio Hyperlink", fg="blue", cursor="hand2",font=4)
    link6.pack()
    link6.bind("<Button-1>", lambda e: callback("https://www.lfd.uci.edu/~gohlke/pythonlibs/"))

 
    root.mainloop()
    return 


def Ask():
    with sr.Microphone() as source:

        bool1=True
        while(bool1):
            Read(1)
            try:
                r = sr.Recognizer()
                audio = r.listen(source)
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
                print('check',text in information)
                if text=='break':
                    bool1=False
                elif text=='send':
                    send()
                    bool1=False
                elif text=='cancel':
                    cancel()
                    bool1=False
                elif text=='read':
                    Read(4);
                    bool1=False
                elif (text in information):
                    Read(text)
                elif text=="hyperlink":
                    print("yes come")
                    change_dropdown()
                    

                    
                else:
                    Read(text)
            except:
                Read(2)
canvas = Canvas(master, width = 117, height = 90,bg='blue')      
canvas.pack()  
canvas.place(x=360,y=30)    
img = PhotoImage(file= "C:\\Users\\aj556\\Downloads\\desktop\\pyhton notes and courses\\email_sender\\email_image.png")  
canvas.create_image(10,10, anchor=NW, image=img) 

s1=Label(master,text="Subject",fg='red')
s1.config(width=20,font=30)
s1.place(x=80,y=140)

subj1=Button(master, text ="Done", command = Done_subject,font=10,bg='blue',fg='pink')
subj1.place(x=590,y=135)

l1=Label(master, text="Sender's email", fg='red')
l1.config(width=20,font=30)
l1.place(x=80,y=190)

done1=Button(master, text ="Done", command = Done_sender,font=10,bg='blue',fg='pink')
done1.place(x=590,y=185)

l2=Label(master, text="Receiver's email",fg='red')
l2.config(width=20,font=30)
l2.place(x=80,y=240)

l3=Label(master, text='Message',fg='red')
l3.config(width=20,font=30)
l3.place(x=80,y=330)

done2=Button(master, text ="Done", command = Done_mess,font=10,bg='blue',fg='pink')
done2.place(x=590,y=325)

l4=Label(master, text='Document',fg='red')
l4.config(width=20,font=30)
l4.place(x=80,y=440)
#l4.grid(padx=10,pady=10)

subj=Entry(master,textvariable=var3,font=35)
subj.place(x=320,y=140)

sender= Entry(master,textvariable=var1,font=35)
sender.place(x=320,y=190)

receiver = Entry(master,textvariable=var2,font=35)
receiver.place(x=320,y=240)

Add1=Button(master, text ="Add", command = add,font=20,bg='blue',fg='pink')
Add1.place(x=590,y=240)

Clear11=Button(master, text ="Clear", command = Clear,font=20,bg='blue',fg='pink')
Clear11.place(x=647,y=240)

stop1=Button(master, text ="Stop Adding", command = Stop_Adding,font=20,bg='blue',fg='pink')
stop1.place(x=715,y=240)


mess=Text(master,font=35)
mess.place(x = 320, y = 283,width=220,height=140)

docu=Entry(master,textvariable=var4,font=35)
docu.place(x=320,y=440)

Add2=Button(master, text ="Add", command = add1,font=20,bg='blue',fg='pink')
Add2.place(x=590,y=430)

Clear21=Button(master, text ="Clear", command = Clear1,font=20,bg='blue',fg='pink')
Clear21.place(x=647,y=430)

stop2=Button(master, text ="Stop Adding", command = Stop_Adding1,font=20,bg='blue',fg='pink')
stop2.place(x=715,y=430)


OptionList = [
"Links"
]

variable = tk.StringVar(master)
variable.set("Hyperlink") 
opt = tk.OptionMenu(master, variable, *OptionList)
opt.config(width=6, font=('Comic Sans MS', 12),fg='blue')
opt.place(x=380,y=545)
variable.trace("w", change_dropdown)



photo1 = PhotoImage(file = "send3.png")
photo2 = PhotoImage(file = "close3.png")
photo3 = PhotoImage(file = "th1.png")
photo4 = PhotoImage(file = "ask.png")

#okk1=Button(master, command = send ,text="Send",image=photo)
okk1=Button(master, text ="Send", command = send,image=photo1)
cancel1=Button(master, text ="Cancel", command = cancel,image=photo2)
read=Button(master, text ="Read", command = lambda : Read(4),image=photo3)
ask=Button(master, text ="Ask", command = Ask,image=photo4)

okk1.config(width=47,height=33)
cancel1.config(width=47,height=33)
read.config(width=47,height=33)
ask.config(width=47,height=33)

okk1.place(x=330,y=500)
cancel1.place(x=404,y=591)
read.place(x=480,y=500)
ask.place(x=404, y=500)


mainloop()
