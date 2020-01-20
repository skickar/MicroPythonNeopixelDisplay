## Wipe Pixels

## Import neopixels and create object, include the Pin number and Number of pixels

## On the D1 Mini, the "D4" pin, located next to power and ground, is actually Pin 2. 
# You can see the pinout on the D1 mini for more info on finding the right pin to connect to


import machine, neopixel, random, math, time, utime
np = neopixel.NeoPixel(machine.Pin(2), 70)

## Create a random function
def randint(lower, upper):
    gap = upper - lower
    if gap == 0:
        return lower
    return (random.getrandbits(int(math.log(gap, 2)))% gap) + lower

#Erase all pixels function
def ErasePixels():
    for i in range(0,70):
        np[i] = (0,0,0)
        np.write()
        
## Make a list for each segment
        
listA = []
listB = []
listC = []
listD = []
listE = []
listF = []
listG = []

## Populate each list with the correct pixels

for i in range (0,10):
    listA.append(i)
for i in range (10,20):
    listB.append(i)
for i in range (20,30):
    listC.append(i)
for i in range (30,40):
    listD.append(i)
for i in range (40,50):
    listE.append(i)
for i in range (50,60):
    listF.append(i)
for i in range (60,70):
    listG.append(i)

## Define all numbers as functions and create default values for the color and time to display each number

def Zero(Color = (255, 0, 0), TotalTime = 1):
    for x in (listC + listD + listE + listF + listG + listB):
        np[x] = Color
        np.write()
    time.sleep(TotalTime)
    ErasePixels()

def One(Color = (255, 0, 0), TotalTime = 1):
    for x in (listB + listG):
        np[x] = Color
        np.write()
    time.sleep(TotalTime)
    ErasePixels()
    
def Two(Color = (255, 0, 0), TotalTime = 1):
    for x in (listA + listB + listC + listF + listE):
        np[x] = Color
        np.write()
    time.sleep(TotalTime)
    ErasePixels()

def Three(Color = (255, 0, 0), TotalTime = 1):
    for x in (listA + listB + listC + listF + listG):
        np[x] = Color
        np.write()
    time.sleep(TotalTime)
    ErasePixels()

def Four(Color = (255, 0, 0), TotalTime = 1):
    for x in (listA + listB + listD + listG):
        np[x] = Color
        np.write()
    time.sleep(TotalTime)
    ErasePixels()

def Five(Color = (255, 0, 0), TotalTime = 1):
    for x in (listC + listD + listA + listF + listG):
        np[x] = Color
        np.write()
    time.sleep(TotalTime)
    ErasePixels()

def Six(Color = (255, 0, 0), TotalTime = 1):
    for x in (listC + listD + listE + listF + listG + listA):
        np[x] = Color
        np.write()
    time.sleep(TotalTime)
    ErasePixels()

def Seven(Color = (255, 0, 0), TotalTime = 1):
    for x in (listC + listB + listG):
        np[x] = Color
        np.write()
    time.sleep(TotalTime)
    ErasePixels()

def Eight(Color = (255, 0, 0), TotalTime = 1):
    for x in (listC + listD + listE + listF + listG + listA + listB):
        np[x] = Color
        np.write()
    time.sleep(TotalTime)
    ErasePixels()

def Nine(Color = (255, 0, 0), TotalTime = 1):
    for x in (listC + listD + listG + listA + listB):
        np[x] = Color
        np.write()
    time.sleep(TotalTime)
    ErasePixels()
    
## Define letters too
    
def LetterH(Color = (255, 0, 0), TotalTime = 1):
    for x in (listA + listB + listD + listE + listG):
        np[x] = Color
        np.write()
    time.sleep(TotalTime)
    ErasePixels()
    
def LetterE(Color = (255, 0, 0), TotalTime = 1):
    for x in (listA + listC + listD + listE + listF):
        np[x] = Color
        np.write()
    time.sleep(TotalTime)
    ErasePixels()

def LetterL(Color = (255, 0, 0), TotalTime = 1):
    for x in (listD + listE + listF):
        np[x] = Color
        np.write()
    time.sleep(TotalTime)
    ErasePixels()
    
def LetterO(Color = (255, 0, 0), TotalTime = 1):
    for x in (listB + listC + listD + listE + listF + listG):
        np[x] = Color
        np.write()
    time.sleep(TotalTime)
    ErasePixels()
    
def LetterI(Color = (255, 0, 0), TotalTime = 1):
    for x in (listD + listE):
        np[x] = Color
        np.write()
    time.sleep(TotalTime)
    ErasePixels()

## Create a list with all numbers and letters so we can iterate through them
    
Num = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
Letter = [LetterH, LetterE, LetterL, LetterO, LetterH, LetterI]

## Create colors to cycle through, and a message to play

Colors = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (128, 255, 0), (0, 255, 0), (255, 128, 0), (0, 255, 255), (0, 0, 255), (255, 0, 255), (255, 127, 0)]

## Pick random numbers and colors

while True:
    Num[randint(0,10)](Colors[randint(0,10)])
    time.sleep(.1)
