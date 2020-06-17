# import tkinter as tk

from tkinter import * 
import wikipedia
from googlesearch import search 
import tkinter as tk

#Make the window
window = Tk()
window.title("Web Search")
window.iconbitmap('icon.ico')
window.configure(background = 'black')
window.geometry('490x720')
window.resizable(0,0)

#Photo Label
AssisstancePhoto = 'img.png'
photo1 = PhotoImage(file=AssisstancePhoto)
Label (window , image = photo1, bg ='black').grid(row=0, column = 0, sticky=W)

# def googleSearch(text_to_search):
#     query = text_to_search
#     for a in search(query, tld="com", lang='en', num=10, start=0, stop=1, pause=2):
#         None
#     for b in search(query, tld="com", lang='en', num=10, start=1, stop=1, pause=2):
#         None
#     for c in search(query, tld="com", lang='en', num=10, start=2, stop=2, pause=2):
#         None
#     links = (str(a)+"\n"+str(b)+"\n"+str(c))
#     return links


def search():
	topic = textentry.get()
	data = wikipedia.summary(topic, sentences=10, chars=500, auto_suggest=True, redirect=True)
	
	# googlesearch_link = googleSearch(topic)

	# data_final = data +str("\n")+googlesearch_link
	InsertText(data)
	return

def random():

	topic = wikipedia.random(pages=1)
	data = wikipedia.summary(topic, sentences=10, chars=500, auto_suggest=True, redirect=True)
	InsertText(data)

def google():
	from googlesearch import search 
	topic = textentry.get()
	links_list = []
	for j in search(topic, lang='en', num = 5,start=0, stop=5, pause=2):
		links_list.append(j)
	for i in range(len(links_list)):
		InsertText(links_list[i])





def clear():
	output.delete(1.0,END)
	textentry.delete(0,END)


# #Text Label
pos= N

#create a text entry box
textentry = Entry(window, width = 54 ,bg="white", highlightcolor = 'red',bd =3)
textentry.grid(row =4 , column=1, sticky =pos, columnspan= 8 ,padx = 3, pady = 10)
# text = textentry.get()

Label (window,text="Web Search", bg= 'black',fg = "white",font = "none 20 bold" ).grid (row=0 ,column =1, sticky=W)
Label (window,text="Search ", bg= 'black',fg = "yellow",font = "none 10 bold" ).grid (row=1 ,column =1, sticky=W)



#textbox
output = Text(window, width=60, height =29, wrap = WORD, bg= 'black',bd = 5 ,fg = "white")
output.grid(row=12, column=0, columnspan=6)
output.config(state=NORMAL)

#Add a submit button 
EnterButton = Button(window, text= "Enter", width = 10, fg = "#FFFFFF", bg= "#3E48DA",activeforeground = 'red',bd=2 ,activebackground= '#272324', command = search).grid(row=5, column=1)
ClearButton = Button(window, text= "Clear", width = 10, fg = "#FFFFFF", bg= "#3E48DA",activeforeground = 'red',bd=2 ,activebackground= '#272324', command = clear).grid(row=6, column=1)
LinksButton = Button(window, text= "Google", width = 10, fg = "#FFFFFF", bg= "#3E48DA",activeforeground = 'red',bd=2 ,activebackground= '#272324', command = google).grid(row=6, column=2)
RandomButton = Button(window, text= "Random", width = 10, fg = "#FFFFFF", bg= "#3E48DA",activeforeground = 'red',bd=2 ,activebackground= '#272324', command = random).grid(row=5, column=2)


def InsertText(text):
    output.delete('1.0',END)
    output.insert(tk.INSERT,text)


window.mainloop()
