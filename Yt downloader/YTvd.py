from tkinter import *
from pytube import YouTube

root = Tk() #Makes the display windows
root.geometry('500x300') #Window Size
root.resizable(1000,1000) #Resizable Maximize- Minimize
root.title("Merlin's Youtube Video Downloader") #Words in the title bar.

Label(root, text = 'Youtube Video Downloader', font= 'Arial 20 bold').pack() #The Title display on the window, as we have put the tk() under root we just use root here for calling the windows
#pack organizes widgets in a block


link = StringVar() #is a string type variable that stores the youtube video link that the user enters.

#Another Text
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)

#Entry is used to create an input text field, place is to place the widget.
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

def Downloader():
    #The url variable gets the yt link from the link defied above and converts it into str
    url = YouTube(str(link.get()))
    #Video is downloaded by stream.first method
    video = url.streams.first()

    video.download()

    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x=180, y=150)
#This is simply the button and in the command we tell it to do the downloader function.
Button(root, text = 'DOWNLOAD', font = 'arial 15 bold', bg = 'pale violet red', padx = 2, command = Downloader).place(x=180, y=150)

root.mainloop()
#Mainloop() Executes the program when want to run it in an infinite loop, it stops when we close the window.
