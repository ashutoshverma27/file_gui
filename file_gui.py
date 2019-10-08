import os,shutil
from os import path
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar
import threading
choose=[]
folder={".jpg":"Images",".jpeg":"Images",".png":"Images",".mkv":"Videos",".mp4":"Videos",".pdf":"Documents",".exe":"Software",".c":"C files",".py":"Python Files"}

source=""
dst=""
src=""
def seldir(value):
    global source,src,dst
    if value=="a":
        source=str(filedialog.askdirectory())
        if source:
            selected=source+" Selected"
            direct.set(selected)
            showdir(source)
    if value=="b":
        src=str(filedialog.askdirectory())
        if src:
            selected=src+" Selected"
            src_hostel.set(selected)
            showdir(src)
    if value=="c":
        dst=str(filedialog.askdirectory())
        if dst:
            selected=dst+" Selected"
            dst_hostel.set(selected)
            showdir(dst)
    

def showdir(value):
    image_dir=os.path.join(value,"images")
    video_dir=os.path.join(value,"Videos")
    docs_dir=os.path.join(value,"Documents")
    soft_dir=os.path.join(value,"Software")
    py_dir=os.path.join(value,"Python Files")
    c_dir=os.path.join(value,"C Files")
    var1="("
    var2="("
    var3="("
    var4="("
    var5="("
    var6="("
    """for i in [".jpg",".png",".jpeg"]:
        
        if i in choose:
            var1=var1+i+","
    var1=var1+") "+"will be saved to "+image_dir
    image_var.set(var1)"""
    for i in choose:
        if i==".jpg" or i==".jpeg" or i==".png":
            var1=var1+i+","
        if i==".mkv" or i==".mp4":
            var2=var2+i+","
        if i==".pdf" or i==".txt" or i==".docs":
            var3=var3+i+","
        if i==".exe":
            var4=var4+i+","
        if i==".py":
            var5=var5+i+","
        if i==".c":
            var6=var6+i+","
    if ".jpg" in choose or ".jpeg" in choose or ".png" in choose:
        var1=var1+") "+"will be saved to "+image_dir
        image_var.set(var1)
    if ".mkv" in choose or ".mp4" in choose:
        var2=var2+") "+"will be saved to "+video_dir
        vid_var.set(var2)
    if ".pdf" in choose or ".txt" in choose or ".docs" in choose:
        var3=var3+") "+"will be saved to "+docs_dir
        doc_var.set(var3)
    if ".exe" in choose:
        var4=var4+") "+"will be saved to "+soft_dir
        soft_var.set(var4)
    if ".py" in choose:
        var5=var5+") "+"will be saved to "+py_dir
        py_var.set(var5)
    if ".c" in choose:
        var6=var6+") "+"will be saved to "+c_dir
        c_var.set(var6)
        
        
            
            

def chose(value):
    global choose
    if value not in choose:
        choose.append(value)
        print(choose)
    if source:
        showdir(source)
    if src and dst:
        print(dst)
        showdir(dst)
        

def sort_docs(value):
    global source,dst
    print(source)
    try:
        if value=="a":
           sort_files(source,source)
        if value=="c":
            sort_files(src,dst)
    except FileNotFoundError:
        msg['fg']='red'
        msg['font']=('Helvetica bolder', '12')
        show.set("Select a directory first!!!!")
    
def copy_callback(from_, to, lock,i,dest_file):
    th = threading.Thread(target=copy_thread, args=(from_, to, lock,i,dest_file))
    th.start()


def copy_thread(from_, to, lockobj,i,dest_file):
    with lockobj:
        msg="Moving "+i+" files....."
        show.set(msg)
        if os.path.exists(dest_file):
            shutil.move(from_,dest_file)
            show.set("File already exists and replaced")
        else:
            shutil.move(from_, to)
            show.set("file moved")
        check_thread()  
            

lock = threading.Lock() # this one monitores finish of copy operation

def sort_files(source_value,dest_value):
    print(source_value)
    print(source_value)
    files=os.listdir(source_value)
    for i in choose:
        for file in files:
            if file.endswith(i):
                try:
                    dest=os.path.join(dest_value,folder[i])
                    dest_file=os.path.join(dest,file)
                    os.mkdir(dest)
                    send=os.path.join(source_value,file)
                    shutil.move(send,dest)
                    
                except:
                    dest_file=os.path.join(dest,file)
                    print(dest_file)
                    send=os.path.join(source_value,file)
                    copy_callback(send,dest,lock,i,dest_file)
                    #shutil.move(send,dest)
def check_thread():
    if lock.acquire(blocking=False):
            show.set("All files moved successfully!")
            lock.release()
                 

window=Tk()
window.title("File Organiser")
window.configure(background='#acdcdc')
frame=Frame(window,height=150,width=300)##frame for options
root=Frame(frame,height=450,width=500) ##frame for sorting within folders
hostel=Frame(frame,height=450,width=600)###for moving one folder to another
show=StringVar()
direct=StringVar()
src_hostel=StringVar()
dst_hostel=StringVar()
image_var=StringVar()
vid_var=StringVar()
doc_var=StringVar()
soft_var=StringVar()
py_var=StringVar()
c_var=StringVar()


#################frame for moving from one directory to another##################
def raisehostel(): 
    hostel.tkraise()
    hostel.configure(background='#acdcdc')
    label22=Label(hostel,text="Move from(Source):")
    label22.place(x=20,y=5)
    b1=Button(hostel,text="Browse ",command=lambda:seldir("b"))
    b1.place(x=150,y=5)

    label23=Label(hostel,text="Move to(Destination):")
    label23.place(x=300,y=5)
    b2=Button(hostel,text="Browse ",command=lambda:seldir("c"))
    b2.place(x=430,y=5)

    
    label5=Label(hostel,textvariable=src_hostel,bg='#acdcdc')#label for source
    label5.place(x=20,y=33)

    label4=Label(hostel,textvariable=dst_hostel,bg='#acdcdc')#label for destination
    label4.place(x=300,y=33)
    


    #image format option
    image=Label(hostel,text="Images:")
    image.place(x=20,y=60)

    jpg=Checkbutton(hostel,text=".jpg",bg='#acdcdc',command=lambda:chose(".jpg"))
    jpg.place(x=100,y=60)
    jpeg=Checkbutton(hostel,text=".jpeg",command=lambda:chose(".jpeg"),bg='#acdcdc')
    jpeg.place(x=150,y=60)
    png=Checkbutton(hostel,text=".png",command=lambda:chose(".png"),bg='#acdcdc')
    png.place(x=200,y=60)

    label7=Label(hostel,textvariable=image_var,bg='#acdcdc',font=('Helvetica', '8'))
    label7.place(x=20,y=85)

    #video format option
    video=Label(hostel,text="Videos:")
    video.place(x=20,y=115)

    mkv=Checkbutton(hostel,text=".mkv",command=lambda:chose(".mkv"),bg='#acdcdc')
    mkv.place(x=100,y=115)
    mp4=Checkbutton(hostel,text=".mp4",command=lambda:chose(".mp4"),bg='#acdcdc')
    mp4.place(x=150,y=115)

    label8=Label(hostel,textvariable=vid_var,bg='#acdcdc',font=('Helvetica', '8'))
    label8.place(x=20,y=140)

    #document format option
    documents=Label(hostel,text="Documents:")
    documents.place(x=20,y=170)

    pdf=Checkbutton(hostel,text=".pdf",command=lambda:chose(".pdf"),bg='#acdcdc')
    pdf.place(x=100,y=170)
    docs=Checkbutton(hostel,text=".docs",command=lambda:chose(".docs"),bg='#acdcdc')
    docs.place(x=150,y=170)
    txt=Checkbutton(hostel,text=".txt",command=lambda:chose(".txt"),bg='#acdcdc')
    txt.place(x=200,y=170)

    label9=Label(hostel,textvariable=doc_var,bg='#acdcdc',font=('Helvetica', '8'))
    label9.place(x=20,y=195)

    #windows software format option
    software=Label(hostel,text="Software:")
    software.place(x=20,y=225)

    exe=Checkbutton(hostel,text=".exe",command=lambda:chose(".exe"),bg='#acdcdc')
    exe.place(x=100,y=225)

    label10=Label(hostel,textvariable=soft_var,bg='#acdcdc',font=('Helvetica', '8'))
    label10.place(x=20,y=250)
    
    

    #move files
    move=Button(hostel,text="Move",command=lambda:sort_docs("c"))
    move.place(x=200,y=275)

    #show moved successfully message
    
    msg=Label(hostel,textvariable=show,bg='#acdcdc')
    msg.place(x=20,y=305)

    
    menu=Button(hostel,text="Menu",command=frameraise)
    menu.place(x=20,y=275)
    hostel.grid(row=0, column=0, sticky='news')





################ frame for moving files around############################
def raiseroot():
    global msg
    root.tkraise()
    root.configure(background='#acdcdc')
    label22=Label(root,text="Select directory For Sorting:")
    label22.place(x=20,y=5)
    b1=Button(root,text="Browse ",command=lambda:seldir("a"))
    b1.place(x=200,y=5)

    
    label5=Label(root,textvariable=direct,bg='#acdcdc')
    label5.place(x=20,y=33)


    #image format option
    image=Label(root,text="Images:")
    image.place(x=20,y=60)

    jpg=Checkbutton(root,text=".jpg",bg='#acdcdc',command=lambda:chose(".jpg"))
    jpg.place(x=100,y=60)
    jpeg=Checkbutton(root,text=".jpeg",command=lambda:chose(".jpeg"),bg='#acdcdc')
    jpeg.place(x=150,y=60)
    png=Checkbutton(root,text=".png",command=lambda:chose(".png"),bg='#acdcdc')
    png.place(x=200,y=60)

    label7=Label(root,textvariable=image_var,bg='#acdcdc',font=('Helvetica', '8'))
    label7.place(x=20,y=85)

    #video format option
    video=Label(root,text="Videos:")
    video.place(x=20,y=115)

    mkv=Checkbutton(root,text=".mkv",command=lambda:chose(".mkv"),bg='#acdcdc')
    mkv.place(x=100,y=115)
    mp4=Checkbutton(root,text=".mp4",command=lambda:chose(".mp4"),bg='#acdcdc')
    mp4.place(x=150,y=115)

    label8=Label(root,textvariable=vid_var,bg='#acdcdc',font=('Helvetica', '8'))
    label8.place(x=20,y=140)

    #document format option
    documents=Label(root,text="Documents:")
    documents.place(x=20,y=170)

    pdf=Checkbutton(root,text=".pdf",command=lambda:chose(".pdf"),bg='#acdcdc')
    pdf.place(x=100,y=170)
    docs=Checkbutton(root,text=".docs",command=lambda:chose(".docs"),bg='#acdcdc')
    docs.place(x=150,y=170)
    txt=Checkbutton(root,text=".txt",command=lambda:chose(".txt"),bg='#acdcdc')
    txt.place(x=200,y=170)

    label9=Label(root,textvariable=doc_var,bg='#acdcdc',font=('Helvetica', '8'))
    label9.place(x=20,y=195)

    #windows software format option
    software=Label(root,text="Software:")
    software.place(x=20,y=225)

    exe=Checkbutton(root,text=".exe",command=lambda:chose(".exe"),bg='#acdcdc')
    exe.place(x=100,y=225)

    label10=Label(root,textvariable=soft_var,bg='#acdcdc',font=('Helvetica', '8'))
    label10.place(x=20,y=250)

    #Python files extension
    python=Label(root,text="Python:")
    python.place(x=20,y=275)

    py=Checkbutton(root,text=".py",command=lambda:chose(".py"),bg='#acdcdc')
    py.place(x=100,y=275)

    label11=Label(root,textvariable=py_var,bg='#acdcdc',font=('Helvetica', '8'))
    label11.place(x=20,y=300)

    #c files extension
    cfiles=Label(root,text="C Program:")
    cfiles.place(x=20,y=325)

    c=Checkbutton(root,text=".py",command=lambda:chose(".c"),bg='#acdcdc')
    c.place(x=100,y=325)

    label12=Label(root,textvariable=c_var,bg='#acdcdc',font=('Helvetica', '8'))
    label12.place(x=20,y=350)
    
    

    #move files
    move=Button(root,text="Move",command=lambda:sort_docs("a"))
    move.place(x=200,y=375)

    #show moved successfully message
    
    msg=Label(root,textvariable=show,bg='#acdcdc')
    msg.place(x=20,y=405)

    
    menu=Button(root,text="Menu",command=frameraise)
    menu.place(x=20,y=375)
    root.grid(row=0, column=0, sticky='news')
#########################################

############# option frame #############################
def frameraise():
    root.grid_forget()
    hostel.grid_forget()
    raiseframe()

#########raise frame or menu###########
def raiseframe():
    frame.configure(background='#acdcdc')
    label=Label(frame,text="Select Your option:",bg='#acdcdc')
    label.place(x=100,y=40)

    button1=Button(frame,text="Sorting Files \nWithin Directory" ,command=raiseroot)
    button1.place(x=30,y=80)

    button2=Button(frame,text="Sorting Of Files" ,command=raisehostel)
    button2.place(x=170,y=80)


    frame.grid(row=0, column=0, sticky='news')

raiseframe()
window.resizable(True, True)
window.mainloop()
