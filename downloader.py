#!/usr/bin/python

#import librarys
from pytube import YouTube
from sys import argv

#Save link in a variabe. Link was passed as a parameter 
link = argv[1]
yt = YouTube(link)

print("Title:", yt.title, "\n")

print("Views:", yt.views, "\n")

print("\n")

#getting video with highest res
video= yt.streams.get_highest_resolution()

#Saving the video on 'Videos' folder
video.download("C:\\Users\\diego\\Videos")
