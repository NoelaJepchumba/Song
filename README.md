Overview of the song.py
This project is a simple music player that allows you to play songs while displaying their lyrics. It uses Pygame for audio playback and Tkinter for the user interface. It supports basic functionalities like displaying lyrics and playing the audio.

Features:
Play Music: Play audio files directly from your computer.
Display Lyrics: Shows the lyrics of the song as it plays.
Abstract User Interface: Built using Tkinter, providing buttons to interact with the player.
Supported File Formats: The player supports MP3, WAV, and OGG audio formats.

INSTALLATION:
install pygame
install tkinter

Usage:
add file to the audio

WHEN RUNNING::
This will open a window with buttons that let you:
    Show Lyrics: Displays the lyrics of the song.
    Play Song: Plays the song from the provided audio file.
    Quit: Exits the program.

Known Issues:
   Audio Formats: The player might not work if the audio file format is not supported by Pygame (such as FLAC or AAC). Ensure that your file is MP3, WAV, or OGG.
   File Path Issues on Windows: Be careful with file paths on Windows. Use double backslashes \\ or raw strings r"..." for paths.

Troubleshooting:
  Error: Audio file not found: Make sure the file path is correct. You can use absolute paths or relative paths.
  Pygame mixer error: Ensure that your audio file is in a supported format (MP3, WAV, OGG).

These are the enhancements i need to make:
         Pause/Resume Feature: Add functionality to pause and resume music.
         Volume Control: Add a volume slider to control the playback volume.
