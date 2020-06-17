# import tkinter as tk

from tkinter import * 

#Make the window
window = Tk()
window.title("Web Search")
window.iconbitmap('icon.ico')
window.configure(background = 'black')
window.geometry('500x720')
window.resizable(0,0)

#Photo Label
AssisstancePhoto = 'img.png'
photo1 = PhotoImage(file=AssisstancePhoto)
Label (window , image = photo1, bg ='black').grid(row=0, column = 0, sticky=W)



def search():
	return




def clear():
	return


# #Text Label
pos= N

#create a text entry box
textentry = Entry(window, width = 54 ,bg="white", highlightcolor = 'red',bd =3)
textentry.grid(row =4 , column=1, sticky =pos, columnspan= 8 ,padx = 3, pady = 10)
# text = textentry.get()

Label (window,text="Web Search", bg= 'black',fg = "white",font = "none 20 bold" ).grid (row=0 ,column =1, sticky=W)
Label (window,text="Search ", bg= 'black',fg = "yellow",font = "none 10 bold" ).grid (row=1 ,column =1, sticky=W)





#Add a submit button 
EnterButton = Button(window, text= "Enter", width = 10, fg = "#272324", bg= "#A9A9A9",activeforeground = 'red',bd=2 ,activebackground= '#272324', command = search).grid(row=5, column=1)
ClearButton = Button(window, text= "Clear", width = 10, fg = "#272324", bg= "#A9A9A9",activeforeground = 'red',bd=2 ,activebackground= '#272324', command = clear).grid(row=6, column=1)

#textbox
output = Text(window, width=60, height =29, wrap = WORD, bg= 'black',bd = 5 ,fg = "#00D1FF")
output.grid(row=12, column=0, columnspan=6)
output.config(state=NORMAL)

window.mainloop()
