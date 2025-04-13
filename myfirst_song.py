import tkinter as tk
from tkinter import scrolledtext
import pygame
import os

# Initialize Pygame for audio
pygame.mixer.init()

# Song class
class Song:
    def __init__(self, title, author, audio, lyrics):
        self.title = title
        self.author = author
        self.audio = audio
        self.lyrics = lyrics

    def play_song(self):
        if os.path.exists(self.audio):
            pygame.mixer.music.load(self.audio)
            pygame.mixer.music.play()
        else:
            lyrics_box.config(state="normal")
            lyrics_box.insert(tk.END, "\nError: Audio file not found.")
            lyrics_box.config(state="disabled")

    def get_lyrics(self):
        return self.lyrics

# Song data
lyrics = [
    "The shoes match the pants",
    "The pants match the belt",
    "The belt match the shirt",
    "The shirt match her skirt",
    "And then her skirt match the hat",
    "The hat match the work",

    "Damn I told ya",
    "Damn I told ya, n****s really clowns, they at the circus",
    "I can tell you never made no money, 'cause you're nervous",
    "Pull up on ya, I might really close your curtains",

    "Back after back, made it back off the backend",
    "Track after track, made it crack off the mixtape",
    "Rack after rack, put some racks on your best friend",
    "On your best friend, on your bestie",
    "Pour some juice up in my cup, I'm feeling sexy",
    "Shawty know I'm feeling good, I tell her, 'Text me'",
    "Thanking God for every minute that He bless me",
    "Shawty said she finna block me, be for real",
    "I be drowning in that mud like Navy Seals",
    "Cristiano, I be really in the fields",

    "Yeah, I got my bands up, got my meals up, got my feels up",
    "Go, go, go, go",

    "Back, run it back, made it back",
    "Shawty wanna push it down my back, I tell her uhhhh",
    "Shawty wanna ride by my side, tell her uhhh",
    "Said she want a piece of my mind, tell her uhhh",
    "I don't wanna waste no more time, tell her uhhh",
    "Said she wanna be on my side, tell her uhhh",

    "Is you dumb? Is you stupid?",
    "When it come to dressing, n****s know I'm a student",
    "All my money talk, all your money it be muted",
    "I be off that, n**** know that I be booted",
    "So I told her",

    "The shoes match the pants",
    "The pants match the belt",
    "The belt match the shirt",
    "The shirt match her skirt",
    "And then her skirt match the hat",
    "The hat match the work",

    "Damn I told ya",
    "Damn I told ya, n****s really clowns, they at the circus",
    "I can tell you never made no money, 'cause you're nervous",
    "Pull up on ya, I might really close your curtains"
]


# Replace this with the correct full path to your audio file
audio_path = r"C:\Users\noela\Documents\yoshimitse.mp3 (online-audio-converter.com).wav"

my_song = Song(
    title="YOSHIMITSU",
    author="Cochise",
    audio=audio_path,
    lyrics=lyrics
)

# ---- GUI Setup ----
window = tk.Tk()
window.title("🎵 YOSHIFY")
window.geometry("450x400")
window.configure(bg="purple")

# Labels
title_label = tk.Label(window, text=my_song.title, font=("Helvetica", 16, "bold"), fg="purple",bg="pink")
title_label.pack(pady=5)

artist_label = tk.Label(window, text=f"by {my_song.author}", font=("Helvetica", 12), fg="purple")
artist_label.pack(pady=5)

# Lyrics box
lyrics_box = scrolledtext.ScrolledText(window, width=50, height=10, wrap=tk.WORD, state="disabled",bg="pink")
lyrics_box.pack(pady=10)

# Functions
def show_lyrics():
    lyrics_box.config(state="normal")
    lyrics_box.delete(1.0, tk.END)
    for line in my_song.get_lyrics():
        lyrics_box.insert(tk.END, line + "\n")
    lyrics_box.config(state="disabled")

def play_song():
    my_song.play_song()

# Buttons
lyrics_button = tk.Button(window, text="Show Lyrics", command=show_lyrics, fg="purple")
lyrics_button.pack(pady=5)

play_button = tk.Button(window, text="Play Song", command=play_song, fg="purple")
play_button.pack(pady=5)

# Run GUI
window.mainloop()
