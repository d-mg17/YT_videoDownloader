#!/usr/bin/python

from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title:", yt.title, "\n")

print("Views:", yt.views, "\n")

print("\n")

video= yt.streams.get_highest_resolution()

video.download("C:\\Users\\diego\\Videos")
