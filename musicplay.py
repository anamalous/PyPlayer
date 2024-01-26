from tkinter import *
import tkinter.messagebox
from audmod import *
import os

al=["",0]
c=[]
currplay=[]

pc=[0,0]

alists=[0,0,0,0,0,0]

top=Tk()
top.title("MuSiC bOi")
top.geometry("200x240")
top.config(bg="black")

bf=Frame(top)
bf.pack()

listf=Frame(top)
listf.pack()

lf=Frame(top)
lf.pack()

l=Label(lf,bg="black",fg="white")
l.pack()

e=Entry(listf,width=30,text=" ")

f=Frame(top)
f.pack()

def bs():
    try:
        alists[1].pack_forget()
    except:
        pass
    try:
        alists[4].pack_forget()
    except:
        pass
    try:
        alists[5].pack_forget()
        pc[0].pack_forget()
        pc[1].pack_forget()
    except:
        pass
    try:
        alists[2].pack_forget()
        e.pack_forget()
    except:
        pass
    try:
        alists[3].pack_forget()
    except:
        pass
    if al[1]==1:
        return
    
    songs=list(filter(lambda x:x.split(".")[-1]=="mp3",os.listdir()))

    songlist=Listbox(listf,height=10,width=30,bg="#E0F6E3")
    alists[0]=songlist
    al[1]=1
    for i in songs:
        songlist.insert(songs.index(i),i)
    songlist.pack()
    songlist.bind("<<ListboxSelect>>",callback)

def callback2(evt):
    w=evt.widget
    index=int(w.curselection()[0])
    value=w.get(index)
    showplist(value[0])
    
def showplist(v):
    alists[1].pack_forget()
    allsongs=list(filter(lambda x:x.split(".")[-1]=="mp3",os.listdir()))

    fp=open(v+".txt","r")
    
    psongs=fp.readlines()
    psongs=list(map(lambda x:x.split("\n")[0],psongs))
    songs=list(filter(lambda x:x.split(".")[:-1][0] in psongs,allsongs))

    playsong=Listbox(listf,height=10,width=30,bg="#E0F6E3")

    alists[3]=playsong
    al[1]=0
    
    for i in songs:
        playsong.insert(songs.index(i),i)
    playsong.pack()
    playsong.bind("<<ListboxSelect>>",callback)

def newp():
    alists[1].pack_forget()
    songs=list(filter(lambda x:x.split(".")[-1]=="mp3",os.listdir()))

    songsel=Listbox(listf,height=10,width=30,bg="#E0F6E3",selectmode="multiple")

    pc[0]=Entry(listf,width=30)
    pc[0].pack()
    
    alists[5]=songsel
    al[1]=0

    for i in songs:
        songsel.insert(songs.index(i),i)
    songsel.pack()
    
    pc[1]=Button(listf,text="done",command=creator,bg="#E0F6E3")
    pc[1].pack(side=BOTTOM)

def creator():
    n=pc[0].get()
    if n=="":
        tkinter.messagebox.showinfo("OOPS!","name not provided")
        return
    f=open(n+".txt","w")
    c=list(alists[5].curselection())
    for i in c:
        f.write(alists[5].get(i).split(".")[:-1][0]+"\n")
    f.close()
    bp()
    
def options(evt):
    m=Menu(listf,tearoff=0)
    m.add_command(label="new playlist",command=newp)
    try:
        m.tk_popup(evt.x_root,evt.y_root)
    finally:
        m.grab_release
    
def bp():
    try:
        alists[0].pack_forget()
    except:
        pass
    try:
        alists[4].pack_forget()
    except:
        pass
    try:
        alists[5].pack_forget()
        pc[0].pack_forget()
        pc[1].pack_forget()
    except:
        pass
    try:
        alists[2].pack_forget()
        e.pack_forget()
    except:
        pass
    try:
        alists[3].pack_forget()
    except:
        pass
    if al[1]==2:
        return
    plays=list(filter(lambda x:x.split(".")[-1]=="txt",os.listdir()))
    playlist=Listbox(listf,height=10,width=30,bg="#E0F6E3")
    alists[1]=playlist
    al[1]=2
    if plays==[]:
        playlist.insert(0,"no playlists found")
    for i in plays:
        playlist.insert(plays.index(i),i.split(".")[:-1])
    playlist.pack()
    playlist.bind("<<ListboxSelect>>",callback2)
    playlist.bind("<Button-3>",options)

def searcher(evt):
    w=evt.widget
    s=w.get()
    alists[2].delete(0,END)
    show=list(filter(lambda x:x.split(".")[-1]=="mp3" and x.startswith(s),os.listdir()))
    for i in show:
        alists[2].insert(show.index(i),i)
        
def bse():
    try:
        alists[0].pack_forget()
    except:
        pass
    try:
        alists[5].pack_forget()
        pc[0].pack_forget()
        pc[1].pack_forget()
    except:
        pass
    try:
        alists[1].pack_forget()
    except:
        pass
    try:
        alists[3].pack_forget()
    except:
        pass
    try:
        alists[4].pack_forget()
    except:
        pass
    if al[1]==3:
        return
    al[1]=3
    e.pack()
    searched=Listbox(listf,height=9,width=30,bg="#E0F6E3")
    alists[2]=searched
    searched.pack()
    e.bind("<Key>",searcher)
    searched.bind("<<ListboxSelect>>",callback)

def labselect(evt):
    w=evt.widget
    wt=w.cget("text")
    for i in b:
        if i.cget("text")==wt:
            i.config(bg="#E0F6E3",fg="black")
            b[i]()
        else:
            i.config(bg="black",fg="white")
            
bsongs=Label(bf,text="all songs",bg="black",fg="#E0F6E3",padx=6)
bsongs.bind("<Button-1>",labselect)
bsongs.grid(row=1,column=1)
bplay=Label(bf,text="playlists",bg="black",fg="#E0F6E3",padx=6)
bplay.bind("<Button-1>",labselect)
bplay.grid(row=1,column=2)
bsear=Label(bf,text="search for",bg="black",fg="#E0F6E3",padx=6)
bsear.bind("<Button-1>",labselect)
bsear.grid(row=1,column=3)

b={bsongs:bs,bplay:bp,bsear:bse}

def playlayout(v,wid,ind):
    al[0]=(audiopiece(v))
    a=al[0]
    l.config(text=v)
    b1=Button(f,text="pause",fg="#E0F6E3",bg="black",command=a.pause,padx=5,bd=3)
    b1.grid(row=1,column=1)
    b2=Button(f,text="resume",fg="#E0F6E3",bg="black",command=a.resume,padx=5,bd=3)
    b2.grid(row=1,column=2)
    b3=Button(f,text="stop",fg="#E0F6E3",bg="black",command=a.stop,padx=5,bd=3)
    b3.grid(row=1,column=3)
    print(wid.get(ind+1))
    if a.done():
        playlayout(wid.get(ind+1),wid,ind+1)
    
def callback(evt):
    w=evt.widget
    index=int(w.curselection()[0])
    value=w.get(index)
    if value in al:
        return
    playlayout(value,w,index)

main=Label(listf,height=11,pady=2,width=25,bg="#E0F6E3",text="your groovy pocket pal")
main.pack()
alists[4]=main


top.mainloop()
