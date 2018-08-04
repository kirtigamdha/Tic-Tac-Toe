import tkinter as tk
from tkinter.messagebox import showinfo
import sys
window=tk.Tk()

a=[[" "," "," "],[" "," "," "],[" "," "," "]]
b=[False for i in range(9)]

mark=False

    

window.title("tic tac toe")

window.geometry("242x260")
        


def popup(msg):
    showinfo("tic tac toe",msg)
    window.destroy()
    
def counter():
    count=0
    for i in b:
    
        if(i==True):
            count=count+1
    return count

def check(k):
    for i in a:
        z=0
        for j in range(3):
            if(i[j]==k):z=z+1
            if(z==3):return True
    for i in range(3):
        z=0
        for j in range(3):
            if(a[j][i]==k):z=z+1
            if(z==3):return True
    z=0
            
    for i in range(3):
         
         if(a[i][i]==k):z=z+1
         if(z==3):return True
    z=0
    for i in range(3):
         
         if(a[2-i][i]==k):z=z+1
         if(z==3):return True


def inputarray(num):
     player=" "
     if(b[num-1]==True):
         return
     global mark
     if(mark==False):
         player="X"
         mark=True
     else:
         player="O"
         mark=False
         
     b[num-1]=True
       
     if(num==1):
         a[0][0]=player
         button1["text"]=player
     if(num==2):
         a[0][1]=player
         button2["text"]=player
     if(num==3):
         a[0][2]=player
         button3["text"]=player
     if(num==4):
         a[1][0]=player
         button4["text"]=player
     if(num==5):
         a[1][1]=player
         button5["text"]=player
     if(num==6):
         a[1][2]=player
         button6["text"]=player
     if(num==7):
         a[2][0]=player
         button7["text"]=player
     if(num==8):
         a[2][1]=player
         button8["text"]=player
     if(num==9):
         a[2][2]=player
         button9["text"]=player
     
     if(check(player)==True):
         popup(" player  "+player+" won ")
         sys.exit()

     if(counter()==9):
         popup(" match draw ")
         sys.exit()
            
         
         




button1=tk.Button(text=" ",height=5,width=10,command=lambda:inputarray(1))
button1.grid(column=0,row=0)

button2=tk.Button(text=" ",height=5,width=10,command=lambda:inputarray(2))
button2.grid(column=1,row=0)

button3=tk.Button(text=" ",height=5,width=10,command=lambda:inputarray(3))
button3.grid(column=2,row=0)

button4=tk.Button(text=" ",height=5,width=10,command=lambda:inputarray(4))
button4.grid(column=0,row=1)

button5=tk.Button(text=" ",height=5,width=10,command=lambda:inputarray(5))
button5.grid(column=1,row=1)

button6=tk.Button(text=" ",height=5,width=10,command=lambda:inputarray(6))
button6.grid(column=2,row=1)

button7=tk.Button(text=" ",height=5,width=10,command=lambda:inputarray(7))
button7.grid(column=0,row=2)

button8=tk.Button(text=" ",height=5,width=10,command=lambda:inputarray(8))
button8.grid(column=1,row=2)

button9=tk.Button(text=" ",height=5,width=10,command=lambda:inputarray(9))
button9.grid(column=2,row=2)



    
     
     
  
window.mainloop()
