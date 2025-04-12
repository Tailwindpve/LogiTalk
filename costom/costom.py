#---------modules-----------
from customtkinter import *
from PIL import Image
#---------client------------
from socket import*
import threading
client=socket(AF_INET,SOCK_STREAM)
client.connect(("localhost",1337))
                                                                                #load_image=Image.open("assets/help.jpeg")
                                                                                #ready_image=CTkImage(light_image=load_image,size=(250,300),)
#-----create window----------------
win=CTk()
win.geometry("400x550")
win.title("LogiTalk")
win.configure(fg_color="grey")
                                                                                #label2=CTkLabel(win,image=ready_image,text="")
                                                                                #label2.place(x=300,y=100)
#---------create frame--------
frame=CTkFrame(win,width=350,height=400)
frame.pack_propagate(False)
frame.pack(pady=10)
#---------create frame2-------
frame2=CTkFrame(win,height=80,width=350)
frame2.pack_propagate(False)
frame2.pack(pady=10)
#---------chat----------
vvod=CTkEntry(frame2,placeholder_text="enter...",width=230,height=60)
vvod.pack(pady=20,side="left",padx=10)
message=CTkTextbox(frame,height=380,width=320)
message.configure(state="disable")
message.pack(pady=10)
#---------functions-----------

def click():
                                                                                #    label.configure(text=str(score),font=("Arial",30,"bold"))
    ssend=vvod.get()
    client.send(ssend.encode())
    vvod.delete(0,END)
    message.configure(state="normal")
    message.insert(END,ssend+"\n")
    message.configure(state="disable")
send_btn=CTkButton(frame2,text=">   SEND",compound="right",width=90,height=38,command=click,fg_color="black")
def receive():
    while 1:
        try:
            msg1=client.recv(1024).decode()
            message.configure(state="normal")
            message.insert(END,msg1+"\n")
            message.configure(state="disable")
            print(msg1)
        except:
            pass
threading.Thread(target=receive).start()
                                                                                #button=CTkButton(frame,text="Click",fg_color="black",width=250,height=150,corner_radius=20,command=click)#,image=ready_image)
                                                                                #button.place(x=530,y=100)
#-------pack--------                                                                                #label.pack()
                                                                                #label2.pack()
send_btn.pack(pady=20)
win.mainloop()
