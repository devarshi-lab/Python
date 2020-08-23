from tkinter.filedialog import askdirectory
from tkinter import *
from tkinter.ttk import *
import pygame
import os
import random

root = Tk()
root.minsize(500,500)
root.maxsize(500,500)
root.title("MADS Music Player")
root.configure(background="skyblue")
color = ['orange','blue','green','skyblue','yellow','white','black','violet','pink','brown']
 

v=StringVar()
songlabel = Label(root,textvariable=v,width=40)

listofsongs = []
realnames =[]
index = 0
songname = ""
listbox = Listbox()
getcolor = ""
flag = 1

def playsong(event):
	if (flag == 1):
		stopbutton = Button(root,text ='Stop')
		stopbutton.place(relx = 0.47, rely = 0.72, anchor = CENTER)
		pygame.mixer.music.unpause()
		flag = 0
	elif (flag == 0):
		stopbutton = Button(root,text ='Play')
		stopbutton.place(relx = 0.47, rely = 0.72, anchor = CENTER)
		pygame.mixer.music.pause()
		flag = 1
	stopbutton.bind("<Button-1>",playsong)



def nextsong(event):
	global index
	index += 1
	pygame.mixer.music.load(listofsongs[index])
	pygame.mixer.music.play()
	updatable()

def previoussong(event):
	global index
	index -= 1
	pygame.mixer.music.load(listofsongs[index])
	pygame.mixer.music.play()
	updatable()

def stopsong(event):
	pygame.mixer.music.stop()
	v.set("")

def updatable():
	global index
	global songname
	v.set(listofsongs[index])
	return songname



def directorychooser(event):
	directory = askdirectory()
	os.chdir(directory)

	for files in os.listdir(directory):
		if (files.endswith(".mp3") or files.endswith(".m4a")):

			listofsongs.append(files)
			realnames.append(files)
			

	pygame.mixer.init()
	pygame.mixer.music.load(listofsongs[0])
	pygame.mixer.music.play()
	updatable()

	listbox = Listbox(root, width=35, height=20)
	listofsongs.reverse()

	for items in listofsongs:
		listbox.insert(0,items)

	listofsongs.reverse()
	
	def go(event):
		global index 
		song = listbox.curselection()
		pygame.mixer.music.load(listofsongs[song[0]])
		pygame.mixer.music.play()
		index = song[0]
		updatable()
		getcolor =  random.choice(color)
		root.configure(background = getcolor)

	listbox.bind('<Double-1>', go)
	listbox.place(relx = 0.47, rely = 0.36, anchor = CENTER)
	songlabel.place(relx = 0.49, rely = 0.80 ,anchor = CENTER)
 

selectdir = Button(root,text ='Select Folder')
selectdir.place(relx = 0.57, rely = 0.2, anchor = NE)
selectdir.bind("<Button-1>",directorychooser)




label = Label(root,text='MADS')
label.configure(background = getcolor)
label.pack()


previousbutton = Button(root,text='<-Previous')
previousbutton.place(relx = 0.32, rely = 0.72, anchor = CENTER)

nextbutton = Button(root,text ='Next->')
nextbutton.place(relx = 0.62, rely = 0.72, anchor = CENTER) 

nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",previoussong)

root.mainloop()