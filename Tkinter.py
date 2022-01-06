from tkinter import *
klik=0
def klikker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)
    aken.geometry(str(aken.winfo_width()+10)+"x"+str(aken.winfo_height()+10))
    if klik==100:
        klik=0

def klikker1(event):
    global klik
    klik-=1
    lbl.configure(text=klik)
    if klik==-100:
        klik=0
        
def text_lbl(event):
    text=txt.get()#From Entry to text
    lbl.configure(text=text)
    txt.delete(0,END)

def valik():
    valik_=var.get()
    lbl.configure(text=valik_)
    txt.insert(0,valik_)

def obnul(event):
    klik="нажми на ЛКМ или ПКМ"
    lbl.configure(text=klik)

def vihod(event):
    aken.destroy()#Уничтожает любой виджет
aken=Tk()
aken.title("Akna nimetus")
aken.geometry("600x400")
nupp=Button(aken,text="Mina olen nupp\nValjuta mind!",font="Arial 20",fg="red",bg="lightblue",height=4,width=20,relief=GROOVE)
nupp.bind("<Button-1>",klikker)#LKM
nupp.bind("<Button-3>",klikker1)#PKM
nupp.bind("<Button-2>",obnul)#SKM
lbl=Label(aken,text="...",height=4,width=20,font="Arial 20",fg="green",bg="red")
txt=Entry(aken,font="Arial 20",fg="white",bg="black",justify=CENTER)
txt.bind("<Return>",text_lbl)#Enter
i1=PhotoImage(file="Boy_eats.gif")
i2=PhotoImage(file="1.gif")
i3=PhotoImage(file="2.gif")
var=StringVar()
var.set("Üks")
r1=Radiobutton(aken,image=i1,variable=var,value="Üks",command=valik)
r2=Radiobutton(aken,image=i2,variable=var,value="Kaks",command=valik)
r3=Radiobutton(aken,image=i3,variable=var,value="Kolm",command=valik)
nupp1=Button(aken,text="Exit",font="Arial 20",fg="red",bg="lightblue",height=4,width=20,relief=GROOVE)
nupp1.bind("<Button-1>",vihod)
lbl.pack()
nupp.pack()
txt.pack()
r1.pack()
r2.pack()
r3.pack()
nupp1.pack()
aken.mainloop()