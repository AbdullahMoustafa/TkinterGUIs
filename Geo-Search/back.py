from tkinter import * 
import wikipedia
from googlesearch import search 
import tkinter as tk

#Make the window
window = Tk()
window.title("GEO-Search")
window.iconbitmap('icon.ico')
window.configure(background = '#7CA763')
window.geometry('420x500')
window.resizable(0,0)

#Photo Label
photo1 = PhotoImage(file='img4.png')
Label (window , image = photo1, bg ='#7CA763').grid(row=0, column = 3, sticky=W)


def search():
	Latitude = textentry.get()
	Longitude= textentry2.get()
	d = wikipedia.geosearch(float(Latitude), float(Longitude),results=10) 
	data = "Latitude: "+str(Latitude)+"\n"+"Longitude: "+str(Longitude) +"\n\n"+str(d)

	
	InsertText(data)


def clear():
	output.delete(1.0,END)
	textentry.delete(0,END)
	textentry2.delete(0,END)




#create a text entry box
textentry = Entry(window, width = 30 ,bg="white", highlightcolor = 'red',bd =5)
textentry.grid(row =4 , column=0, sticky =N, columnspan= 4 ,padx = 3, pady = 10)

#create a text entry box
textentry2 = Entry(window, width = 30 ,bg="white", highlightcolor = 'red',bd =5)
textentry2.grid(row =4 , column=3, sticky =N, columnspan= 4 ,padx = 3, pady = 10)



Label (window,text="   Latitude ", bg= '#7CA763',fg = "#873600",font = "none 15 bold" ).grid (row=1 ,column =2, sticky=W)
Label (window,text="   Longitude ", bg= '#7CA763',fg = "#873600",font = "none 15 bold" ).grid (row=1 ,column =4, sticky=W)

Label (window,text=" Get your nearnest places", bg= '#7CA763',fg = "#873600",font = "none 7 bold" ).grid (row=30 ,column =2)



#textbox
output = Text(window, width=50, height =10, wrap = WORD, bg= '#EDBB99',bd = 7 ,fg = "#0A3827")
output.grid(row=12, column=0, columnspan=6)
output.config(state=NORMAL)

#Add a submit button 
EnterButton = Button(window, text= "Enter", width = 10, fg = "#FFFFFF", bg= "#EA4C4C",activeforeground = 'red',bd=5 ,activebackground= '#272324', command = search).grid(row=5, column=3)
ClearButton = Button(window, text= "Clear", width = 10, fg = "#FFFFFF", bg= "#EA4C4C",activeforeground = 'red',bd=5 ,activebackground= '#272324', command = clear).grid(row=6, column=3)


def InsertText(text):
    output.delete(1.0,END)
    output.insert(tk.INSERT,text)

window.mainloop()
