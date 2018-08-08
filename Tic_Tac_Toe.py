import tkinter as tk
from tkinter.messagebox import showinfo

import random


window=tk.Tk()

a=[[" "," "," "],[" "," "," "],[" "," "," "]]
b=[False for i in range(9)]
mark=False

playerno=""

window.title("tic tac toe")

window.geometry("242x260")
        
button1=""
button2=""
button3=""
button4=""
button5=""
button6=""
button7=""
button8=""
button9=""

def counter(b):
    count=0
    for i in b:
    
        if(i==True):
            count=count+1
    return count


def check(k,a):
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

def display(a):
    c=0
    for i in range(3):
        print(a[i][c]+" | "+a[i][c+1]+" | "+a[i][c+2])
        print("-----------------")

def markingfunction(i,j,b):
    
    if(i==0 and j==0):
        b[0]=True
    elif(i==0 and j==1 ):
        b[1]=True
    elif(i==0 and j==2 ):
        b[2]=True
    elif(i==1 and j==0 ):
        b[3]=True
    elif(i==1 and j==1 ):
        b[4]=True        
    elif(i==1 and j==2 ):
        b[5]=True
    elif(i==2 and j==0 ):
        b[6]=True
    elif(i==2 and j==1 ):
        b[7]=True
    elif(i==2 and j==2 ):
        b[8]=True


def  copylistfunction(a):
    duplicatelist=[[" "," "," "],[" "," "," "],[" "," "," "]]
    for i in range(3):
        for j in range(3):
            duplicatelist[i][j]=a[i][j]
    return duplicatelist

def randomnumbergenerator():
    num1=random.randint(0,2)
    num2=random.randint(0,2)

    return num1,num2

def popup(msg):
    
    showinfo("tic tac toe",msg)
    window.destroy()
    return
    

       
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
      
     if(check(player,a)==True):
         popup(" player  "+player+" won ")
     elif(counter(b)==9):
         popup(" match draw ")
         

     
         

     

def inputoneplayer(num):
     global b
     if(b[num-1]==True):
         return
     b[num-1]=True
     
     player="X"
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
     
     
     if(check("X",a)==True):
         popup(" you won")    
     
     elif(counter(b)==9):
         popup(" match draw ")       
     computerplay()
     
     
     if(check("O",a)==True):
         popup(" you lose")

     

def updatedisplay():
    
    button1["text"]=a[0][0]
    button2["text"]=a[0][1]
    button3["text"]=a[0][2]
    button4["text"]=a[1][0]
    button5["text"]=a[1][1]
    button6["text"]=a[1][2]
    button7["text"]=a[2][0]
    button8["text"]=a[2][1]
    button9["text"]=a[2][2]
    
         




def InitialDisplay():
    oneplayer=tk.Button(text="Play against computer",height=2,command=lambda:singleplayer())
    oneplayer.place(rely=0.25,relx=0.2)
         
    twoplayer=tk.Button(text="  Play against human ",height=2,command=lambda:multiplayer())
    twoplayer.place(rely=0.55,relx=0.2)


          
           
def singleplayer():
    
    
    GuiComponentInitOne()

def multiplayer():
    
    
    GuiComponentInit()

def computerplay():


    global mark
    global a
    global b
    
    
    copylist=copylistfunction(a)
    
    
    flag=False
    
    for i in range(3):
        
        for j in range(3):
            
            if(copylist[i][j]=="X" or copylist[i][j]=="O"):
                
                continue
            
            copylist[i][j]="O"
           
            
            if(check("O",copylist)==True):
              
                a[i][j]="O"
                updatedisplay()
                markingfunction(i,j,b)
                return
            else:
                
                
                copylist=copylistfunction(a)
               
                
    for i in range(3):
        
        
        for j in range(3):
            
            if(copylist[i][j]=="X" or copylist[i][j]=="O"):
                continue
            copylist[i][j]="X"
            
            
            if(check("X",copylist)==True):
                 
                 a[i][j]="O"
                 markingfunction(i,j,b)
                 updatedisplay()
                 
                 return
            else:
                 copylist=copylistfunction(a)
    while not flag:
        
        
        num1,num2=randomnumbergenerator()
        
        if(a[num1][num2]==" "):
            
            a[num1][num2]="O"
            updatedisplay()
            markingfunction(num1,num2,b)
            flag=True
            
            
            
def GuiComponentInit():
    global button1,button2,button3,button4,button5,button6,button7,button8,button9
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

def GuiComponentInitOne():
    global button1,button2,button3,button4,button5,button6,button7,button8,button9
    button1=tk.Button(text=" ",height=5,width=10,command=lambda:inputoneplayer(1))
    button1.grid(column=0,row=0)

    button2=tk.Button(text=" ",height=5,width=10,command=lambda:inputoneplayer(2))
    button2.grid(column=1,row=0)

    button3=tk.Button(text=" ",height=5,width=10,command=lambda:inputoneplayer(3))
    button3.grid(column=2,row=0)

    button4=tk.Button(text=" ",height=5,width=10,command=lambda:inputoneplayer(4))
    button4.grid(column=0,row=1)

    button5=tk.Button(text=" ",height=5,width=10,command=lambda:inputoneplayer(5))
    button5.grid(column=1,row=1)

    button6=tk.Button(text=" ",height=5,width=10,command=lambda:inputoneplayer(6))
    button6.grid(column=2,row=1)

    button7=tk.Button(text=" ",height=5,width=10,command=lambda:inputoneplayer(7))
    button7.grid(column=0,row=2)

    button8=tk.Button(text=" ",height=5,width=10,command=lambda:inputoneplayer(8))
    button8.grid(column=1,row=2)

    button9=tk.Button(text=" ",height=5,width=10,command=lambda:inputoneplayer(9))
    button9.grid(column=2,row=2)

        
    
    
    
     
InitialDisplay() 
window.mainloop()

