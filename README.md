# breakbeats-mpr121
Mix breakbeats with an Adafruit mpr121 12 key capacitive touch sensor

Original code & beats files provided by @todbot. Thx for sharing your code & helping me learn!
Check out his repo for some slick code examples at: https://github.com/todbot/circuitpython-tricks/tree/main/larger-tricks

My example uses an Arduino Nano RP2040 Connect wired as below:
<img width="721" alt="wiring-for-arduino-nano-rp2040" src="https://user-images.githubusercontent.com/20801687/154826736-339f519d-eb4a-4cdc-a673-c53346ff3e03.png">

BUT I've had problems running on RP2040 processors (also tried on a QT Py RP2040). I found Mu regularly dropped the board & then the board couldn't connect as CIRCUITPY, so I had to do a complete re-install of CircuitPython to get things working again. Frustrating.

I had much mroe reliable success with a CircuitPlayground Bluefruit.
See comments in code for minor changes.
For wiring for the CPB, connect I2C of STEMMA-QT cabling as follows:
- Black to GND
- Red to 3.3v (not VOUT)
- Blue to A5 (also labeled SDA)
- Yellow to A4 (also labeled SCL)

Clip two alligator clips to the audio plug as shown above.
- Sleeve base of audio plug should connect to pad GND
- Tip of audio plug should connect to AUDIO
Assumption is that you're using a speaker that has separate power. I used a Hamburger-style speaker that you can get from Amazon, Walmart, or SparkFun.
