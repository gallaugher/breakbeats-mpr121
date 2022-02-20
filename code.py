# audiomixer_demo.py -- show how to fade up and down playing loops
# note this causes glitches and crashes on RP2040
# 9 Feb 2022 - @todbot / Tod Kurt
# Modified (probably poorly) by Prof. John Gallaugher to include
# adafruit_mpr121 mixing support. Sorry if I butchered your code, Tod.

import time, board, audiocore, audiomixer, adafruit_mpr121
#from audiopwmio import PWMAudioOut as AudioOut  # for RP2040 etc
#from audioio import AudioOut as AudioOut  # for SAMD51/M4 etc
try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        print("This board does not support AudioOut")
        pass # Not all boards can play audio with AudioOut

# configure AudioOut & set path where sounds can be found
audio = AudioOut(board.D3)

beats = ["amenfull_22k_s16.wav",
        "amen6_22k_s16.wav",
        "amen7_22k_s16.wav",
        "ohohoh2.wav",
        "bass_hit_c.wav",
        "bd_tek.wav",
        "bd_zome.wav",
        "drum_cowbell.wav",
        "duck-scratch.wav",
        "yo.wav",
        "watch-this.wav",
        "freakie-freak.wav"]

path = "beats/"

num_voices = len(beats)

mixer = audiomixer.Mixer(voice_count=num_voices, sample_rate=22050, channel_count=1,
                         bits_per_sample=16, samples_signed=True)
# attach mixer to audio playback
audio.play(mixer)

for i in range(len(beats)):
    print(i)
    wave = audiocore.WaveFile(open(path+beats[i],"rb"))
    mixer.voice[i].play(wave, loop=True )
    mixer.voice[i].level = 0.0

time.sleep(1.0)  # let drums play a bit

i2c = board.I2C()
touch_pad = adafruit_mpr121.MPR121(i2c)

while True:
    touched = False
    for i in range(len(beats)):
        if touch_pad[i].value:
            print("You touched pad # {}!".format(i))
            mixer.voice[i].level = 1.0
        else:
            mixer.voice[i].level = 0.0
