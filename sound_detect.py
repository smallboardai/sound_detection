import os
import time
import pyaudio
import audioop

mylevel = 700
SAMPLING_RATE = 22050
NUM_SAMPLES = 1024
os.system('clear')
while True:
    time.sleep(.15)
    _stream = None
    myrms = 0
    pa = pyaudio.PyAudio()
    _stream = pa.open(format=pyaudio.paInt16, channels=2, rate=SAMPLING_RATE,input=True, frames_per_buffer=NUM_SAMPLES)
    data = _stream.read(NUM_SAMPLES)
    myrms = audioop.rms(data, 2)
    pa.close(_stream)
    if(myrms > mylevel):
        ##do somethin
        print("gotcha")         
        print(myrms)
        time.sleep(1)
        os.system('clear')
