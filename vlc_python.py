import os

os.add_dll_directory(r'C:/Program Files (x86)/VideoLAN/VLC')

import serial

import vlc

ser = serial.Serial('COM5', baudrate = 9600, timeout=1)

vlc_plays = vlc.MediaPlayer("A Silent Voice.mp4")#any file to be played will bw taken here.

playPauseFlag = 0

vlc_plays.play()
vlc_plays.toggle_fullscreen()


def volumnChange(change_direction):
    current_volumn = int(vlc_plays.audio_get_volume())
    
    if(change_direction == "up"):
        vlc_plays.audio_set_volume(current_volumn + 5)
    elif(change_direction == "down"):
        vlc_plays.audio_set_volume(current_volumn - 5)

def timeChange(change_direction):
    current_time = int(vlc_plays.get_time())
    
    if(change_direction == "forwards"):
        vlc_plays.set_time(current_time + 10_000)
    elif(change_direction == "backwards"):
        vlc_plays.set_time(current_time - 10_000)

while 1:
    arduinoData = ser.readline().decode('utf-8')
    arduinoData = arduinoData.rstrip('\r\n')
    print(arduinoData)

    if(arduinoData == "play/pause"):
        if(playPauseFlag == 0):
            vlc_plays.play()
            playPauseFlag = 1
        elif(playPauseFlag == 1):
            vlc_plays.pause()
            playPauseFlag = 0
    if(arduinoData == "volumn up"):
        volumnChange("up")
    if(arduinoData == "volumn down"):
        volumnChange("down")
    if(arduinoData == "skip 10+ s"):
        timeChange("forwards")
    if(arduinoData == "BACKskip 10- s"):
        timeChange("backwards")
    if(arduinoData == "toggle fullscreen"):
        vlc_plays.toggle_fullscreen()
    if(arduinoData == "EXIT"):
        vlc_plays.stop()