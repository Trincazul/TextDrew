import sys

v=sys.version()

if "2.7" in v:
    from Tkinter import * 
    import tkFileDialog

elif "3.3" in v or "3.9" in v:
    from tkinter import *
    import tkinter.tkFileDialog

root=Tk("Text Drew")
text=Text(root) 
text.grid() 

def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation=tkFileDialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

button=Button(root, text="Salvar", command=saveas) 
button.grid()

def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

font=Menubutton(root, text="Fonte") 
font.grid() 
font.menu=Menu(font, tearoff=0) 
font["menu"]=font.menu
Helvetica=IntVar() 
arial=IntVar() 
times=IntVar() 
Courier=IntVar()

#importação de fontes
font.menu.add_checkbutton(label="Courier", variable=Courier, 
command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica,
command=FontHelvetica) 

root.mainloop()