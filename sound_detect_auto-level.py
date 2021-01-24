#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import subprocess
import audioop
import time
import pyaudio

myrmsavg = 0
myrmstotal = 0
mylevel = 700
sampling_rate = 22050
num_samples = 1024

#### turn on the microphone
subprocess.call("amixer set Capture Volume 70%  >> /dev/null", shell=True)

############### Set Ambient Levels #################
x=1
os.system('clear')
while (x <=20):
    time.sleep(.25)
    stream = None
    myrms = 0
    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paInt16, channels=2, rate=sampling_rate,input=True, frames_per_buffer=num_samples)
    data = stream.read(num_samples)
    myrms = audioop.rms(data, 2)
    myrmstotal = myrmstotal + myrms
    pa.close(stream)
    myrmsavg = int(myrmstotal / x)
    os.system('clear')
    print("Getting Ambient Sound Level")
    print("######################################################################")
    print("Abmient Sound Level Average : " + str(myrmsavg))
    print("Current RMS : " + str(myrms) + "  Running Total : " + str(myrmstotal))
    print("######################################################################")
    x=x+1

mytriggerlevel = int(myrmsavg * 1.5)
os.system('clear')
print("Ambient Sound Level Set")
print("######################################################################")
print("Abmient Sound Level Average : " + str(myrmsavg))
print("Setting Trigger Sound Level To : " + str(mytriggerlevel))
print("######################################################################")
time.sleep(3)
############### END Set Ambient Levels #################

############### Listen Loop ##################

while True:
    time.sleep(.15)
    os.system('clear')
    stream = None
    myrms = 0
    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paInt16, channels=2, rate=sampling_rate,input=True, frames_per_buffer=num_samples)
    data = stream.read(num_samples)
    myrms = audioop.rms(data, 2)
    pa.close(stream)
    if(myrms > mylevel):
        ##do somethin
        print("gotcha")         
        print(myrms)
        time.sleep(1)
###############END Listen Loop ##################    
