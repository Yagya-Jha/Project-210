import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import os
import pygame
from pygame import mixer

SERVER = None
PORT = 8050
IP_ADDRESS = '127.0.0.1'
BUFFER_SIZE = 4096

global song_counter
song_counter = 0

name = None
listbox = None
filePathLabel = None


def play():
    global song_selected
    
    song_selected = listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('./shared_files/' + song_selected)
    mixer.music.play()

    if(song_selected != ""):
        infoLabel.configure(text = "Now Playing: " + song_selected)
    else:
        infoLabel.configure(text="")

def stop():
    global song_selected

    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text = "")

def pause():
    global song_selected

    pygame
    mixer.init()
    mixer.music.load('shared_files/' + song_selected)
    mixer.music.pause()

def resume():
    global song_selected

    pygame
    mixer.init()
    mixer.music.load('shared_files/' + song_selected)
    mixer.music.play()


def musicWindow(): 

    global listbox
    global infoLabel
    global song_counter
    global filePathLabel
   
    window = Tk()
    window.title('!! Music Sharing App !!')
    window.geometry("500x500")
    window.configure(bg="black")

    selectSongLabel = Label(window, text = "Select Song", bg = 'white', font = ('Calibri', 8))
    selectSongLabel.place(x=210,y=1)

    listbox = Listbox(window, height = 10, width = 39, activestyle="dotbox",bg = "pink", borderwidth=2, font = ("Calibri", 10))
    listbox.place(x=100,y=18)

    for file in os.listdir('shared_files'):
        filename = os.fsdecode(file)
        listbox.insert(song_counter, filename)
        song_counter = song_counter + 1

    scrollBar1 = Scrollbar(listbox)
    scrollBar1.place(relheight = 1,relx=1)
    scrollBar1.config(command = listbox.yview)

    playButton = Button(window, text = "Play", width = 10, bd = 1, bg = "purple", font = ("Calibri", 10),command = play)
    playButton.place(x=120,y=225)

    stopButton = Button(window, text = "Stop", bd = 1, width = 10, bg = "red", font = ("Calibri",10), command = stop)
    stopButton.place(x=290,y=225)

    resumeButton = Button(window, text = "Resume", bd = 1, width = 10, bg = "orange", font = ("Calibri",10), command=resume)
    resumeButton.place(x=120, y=275)

    pauseButton = Button(window, text = "Pause", bd = 1, width = 10, bg = "blue", font = ("Calibri",10), command=pause)
    pauseButton.place(x=290, y=275)

    uploadButton = Button(window, text = "Upload", width = 10, bd = 1, bg = "yellow", font = ("Calibri", 10))
    uploadButton.place(x=120,y=325)

    downloadButton = Button(window, text = "Download", bd = 1, width = 10,bg = "green", font = ("Calibri",10))
    downloadButton.place(x=290,y=325)

    infoLabel = Label(window, text = "", fg = "blue", font = ("Calibri",8))
    infoLabel.place(x=4,y=350)

    window.mainloop()

def setup():

    global SERVER
    global PORT
    global IP_ADDRESS
    global song_counter

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))

    musicWindow()

setup()
