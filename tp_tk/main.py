from tkinter import *
from tkinter import ttk

def sayHello():
    print("Hello")

def main():
    root = Tk()
    
    tree = ttk.Treeview(root,columns=('id','userId','title','completed'))
    tree.heading('id',text="#")
    tree.heading('userId',text="userId")
    tree.heading('title',text="title")
    tree.heading('completed',text="completed")

    
    tree.pack(fill=BOTH,expand=True)
    root.mainloop()



def main_1():
    root = Tk()
    root.geometry('640x480')
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    ttk.Button(frm, text="Say Hello !", command=sayHello).grid(column=0, row=1)
    
    root.mainloop()

if __name__ == '__main__':
    main()