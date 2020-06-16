from tkinter import*

window = Tk()
window.title("Dark Calculator")
window.iconbitmap('dark90.ico')
window['bg'] = 'orange'


E1= Entry(window,width=45,borderwidth=3,selectbackground="orange",selectforeground="black",fg="black")
E1.grid(row=0,column=0,columnspan=5,padx=5,pady=5)

def button_click(number):
    current = E1.get()
    E1.delete(0,END)
    E1.insert(0,str(current)+str(number))

def button_clear():
    E1.delete(0,END)
   

def button_add():
    first_number = E1.get()
    global f_num
    global math
    math = "additon"
    f_num= int(first_number)   
    E1.delete(0,END)

def button_sub():
    first_number = E1.get()
    global f_num
    global math
    math = "subtraction"
    f_num= int(first_number)
    E1.delete(0,END)

def button_mult():
    first_number = E1.get()
    global f_num
    global math
    math = "multiplication"
    f_num= int(first_number)   
    E1.delete(0,END)

def button_div():
    first_number = E1.get()
    global f_num
    global math
    math = "division"
    f_num= int(first_number)    
    E1.delete(0,END)

def button_equal():
    second_number = E1.get()
    E1.delete(0,END)
    s_num = int(second_number)
    if math == "additon":
        E1.insert(0,f_num+s_num)
    elif math == "subtraction":
        E1.insert(0,f_num-s_num)   
    elif math == "multiplication":
        E1.insert(0,f_num*s_num)
    elif math == "division":
        E1.insert(0,f_num/s_num)       



button1 = Button(window,text="1",padx=40,pady=20,activeforeground="black",bg="black",fg="orange",command=lambda: button_click(1))
button2 = Button(window,text="2",padx=40,pady=20,activeforeground="black",bg="black",fg="orange",command=lambda: button_click(2))
button3 = Button(window,text="3",padx=40,pady=20,activeforeground="black",bg="black",fg="orange",command=lambda: button_click(3))
button4 = Button(window,text="4",padx=40,pady=20,activeforeground="black",bg="black",fg="orange",command=lambda: button_click(4))
button5 = Button(window,text="5",padx=40,pady=20,activeforeground="black",bg="black",fg="orange",command=lambda: button_click(5))
button6 = Button(window,text="6",padx=40,pady=20,activeforeground="black",bg="black",fg="orange",command=lambda: button_click(6))
button7 = Button(window,text="7",padx=40,pady=20,activeforeground="black",bg="black",fg="orange",command=lambda: button_click(7))
button8 = Button(window,text="8",padx=40,pady=20,activeforeground="black",bg="black",fg="orange",command=lambda: button_click(8))
button9 = Button(window,text="9",padx=40,pady=20,activeforeground="black",bg="black",fg="orange",command=lambda: button_click(9))
button0 = Button(window,text="0",padx=40,pady=20,activeforeground="black",bg="black",fg="orange",command=lambda: button_click(0))


button_add=Button(window,text="+",padx=40,pady=20,activeforeground="black",bg="black",fg="orange",command=button_add)
button_sub=Button(window,text="-",padx=40,pady=20,activeforeground="black",bg="black",fg="orange",command=button_sub)    
button_mult=Button(window,text="x",padx=40,pady=20,activeforeground="black",bg="black",fg="orange",command=button_mult)    
button_div=Button(window,text="/",padx=40,pady=20,activeforeground="black",bg="black",fg="orange",command=button_div)

button_clear=Button(window,text="c",padx=40,pady=20,activeforeground="black",bg="black",fg="orange",command=button_clear)    
button_equal=Button(window,text="=",padx=40,pady=20,activeforeground="black",bg="black",fg="orange",command=button_equal)




button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button_add.grid(row=1,column=3)


button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button_sub.grid(row=2,column=3)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button_mult.grid(row=3,column=3)

button0.grid(row=4,column=0)
button_equal.grid(row=4,column=1)
button_clear.grid(row=4,column=2)
button_div.grid(row=4,column=3)

window.mainloop()            
