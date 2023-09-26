# Unihiker TR-808 Drum Machine
# Roni Bandini, September 2023
# Buenos Aires, Argentina
# https://bandini.medium.com/unihiker-tr-808-tributo-a-la-m%C3%ADtica-caja-de-ritmos-roland-3e19d518e86c
# Dependencies: $ gem install beats
# Hardware: 2 DFRobot rotation sensors, one USB sound card

import time
from pinpong.board import *
from pinpong.extension.unihiker import *
from unihiker import GUI
from unihiker import Audio
import subprocess

gui = GUI()
Board().begin()
audio = Audio()

# pot pins
pot1 = Pin(Pin.P21, Pin.ANALOG)
pot2 = Pin(Pin.P22, Pin.ANALOG)

# empty patterns
pattern = []
pattern0=list("................")
pattern1=list("................")
pattern2=list("................")
pattern3=list("................")
pattern4=list("................")
pattern5=list("................")
pattern.append(pattern0)
pattern.append(pattern1)
pattern.append(pattern2)
pattern.append(pattern3)
pattern.append(pattern4)
pattern.append(pattern5)

tempo=100
myY=100
counter=1
b2=0
cursor=0
lineNumber=0
page=1
isPlaying=0

print("Unihiker TR-808 Drum Machine")
print("@RoniBandini - September 2023 - MIT License")
print("")

gui.clear()
img = gui.draw_image(x=0, y=0, w=240, h=320, image='/home/images/portada.jpg')
time.sleep(5)

def updateScreenExporting():
    gui.clear()
    img = gui.draw_image(x=0, y=0, w=240, h=320, image='/home/images/exporting.jpg')

def updateScreenPlaying():
    gui.clear()
    img = gui.draw_image(x=0, y=0, w=240, h=320, image='/home/images/playing.jpg')
    gui.draw_image(x=120, y=265, w=92, h=33, image='/home/images/start.jpg', origin='center', onclick=lambda: play())

def updateScreen():

    gui.clear()
    img = gui.draw_image(x=0, y=0, w=240, h=320, image='/home/images/background.jpg')

    myY=55
    myLine="Page #"+str(page)+" Tempo: "+str(tempo)+" bpm"
    gui.draw_text(x = 120,y=myY,text=myLine, font_size=10, color="white", origin='top')

    myY=myY+45
    line=0

    while line<6:

        row=0
        myX=25

        gui.draw_text(x = 5,y=85,text="K", font_size=10, color="white", origin='top')
        gui.draw_text(x = 5,y=110,text="S", font_size=10, color="white", origin='top')
        gui.draw_text(x = 5,y=133,text="H", font_size=10, color="white", origin='top')
        gui.draw_text(x = 5,y=160,text="O", font_size=10, color="white", origin='top')
        gui.draw_text(x = 5,y=183,text="R", font_size=10, color="white", origin='top')
        gui.draw_text(x = 5,y=210,text="M", font_size=10, color="white", origin='top')

        while row<9:

            if page==1:

                # All these if should be one line but lambda is not accepting line, row parameters, so in the meanwhile a little copy-paste

                if line==0 and row==0:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(0, 0))
                if line==1 and row==0:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(1, 0))
                if line==2 and row==0:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(2, 0))
                if line==3 and row==0:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(3, 0))
                if line==4 and row==0:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(4, 0))
                if line==5 and row==0:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(5, 0))

                if line==0 and row==1:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(0, 1))
                if line==1 and row==1:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(1, 1))
                if line==2 and row==1:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(2, 1))
                if line==3 and row==1:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(3, 1))
                if line==4 and row==1:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(4, 1))
                if line==5 and row==1:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(5, 1))

                if line==0 and row==2:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(0, 2))
                if line==1 and row==2:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(1, 2))
                if line==2 and row==2:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(2, 2))
                if line==3 and row==2:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(3, 2))
                if line==4 and row==2:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(4, 2))
                if line==5 and row==2:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(5, 2))

                if line==0 and row==3:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(0, 3))
                if line==1 and row==3:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(1, 3))
                if line==2 and row==3:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(2, 3))
                if line==3 and row==3:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(3, 3))
                if line==4 and row==3:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(4, 3))
                if line==5 and row==3:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(5, 3))

                if line==0 and row==4:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(0, 4))
                if line==1 and row==4:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(1, 4))
                if line==2 and row==4:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(2, 4))
                if line==3 and row==4:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(3, 4))
                if line==4 and row==4:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(4, 4))
                if line==5 and row==4:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(5, 4))

                if line==0 and row==5:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(0, 5))
                if line==1 and row==5:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(1, 5))
                if line==2 and row==5:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(2, 5))
                if line==3 and row==5:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(3, 5))
                if line==4 and row==5:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(4, 5))
                if line==5 and row==5:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(5, 5))

                if line==0 and row==6:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(0, 6))
                if line==1 and row==6:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(1, 6))
                if line==2 and row==6:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(2, 6))
                if line==3 and row==6:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(3, 6))
                if line==4 and row==6:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(4, 6))
                if line==5 and row==6:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(5, 6))

                if line==0 and row==7:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(0, 7))
                if line==1 and row==7:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(1, 7))
                if line==2 and row==7:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(2, 7))
                if line==3 and row==7:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(3, 7))
                if line==4 and row==7:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(4, 7))
                if line==5 and row==7:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(5, 7))

            else:

                row=row+8

                if line==0 and row==8:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(0, 8))
                if line==1 and row==8:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(1, 8))
                if line==2 and row==8:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(2, 8))
                if line==3 and row==8:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(3, 8))
                if line==4 and row==8:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(4, 8))
                if line==5 and row==8:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(5, 8))

                if line==0 and row==9:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(0, 9))
                if line==1 and row==9:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(1, 9))
                if line==2 and row==9:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(2, 9))
                if line==3 and row==9:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(3, 9))
                if line==4 and row==9:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(4, 9))
                if line==5 and row==9:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(5, 9))

                if line==0 and row==10:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(0, 10))
                if line==1 and row==10:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(1, 10))
                if line==2 and row==10:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(2, 10))
                if line==3 and row==10:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(3, 10))
                if line==4 and row==10:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(4, 10))
                if line==5 and row==10:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(5, 10))

                if line==0 and row==11:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(0, 11))
                if line==1 and row==11:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(1, 11))
                if line==2 and row==11:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(2, 11))
                if line==3 and row==11:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(3, 11))
                if line==4 and row==11:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(4, 11))
                if line==5 and row==11:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(5, 11))

                if line==0 and row==12:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(0, 12))
                if line==1 and row==12:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(1, 12))
                if line==2 and row==12:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(2, 12))
                if line==3 and row==12:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(3, 12))
                if line==4 and row==12:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(4, 12))
                if line==5 and row==12:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(5, 12))

                if line==0 and row==13:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(0, 13))
                if line==1 and row==13:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(1, 13))
                if line==2 and row==13:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(2, 13))
                if line==3 and row==13:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(3, 13))
                if line==4 and row==13:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(4, 13))
                if line==5 and row==13:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(5, 13))

                if line==0 and row==14:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(0, 14))
                if line==1 and row==14:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(1, 14))
                if line==2 and row==14:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(2, 14))
                if line==3 and row==14:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(3, 14))
                if line==4 and row==14:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(4, 14))
                if line==5 and row==14:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(5, 14))

                if line==0 and row==15:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(0, 15))
                if line==1 and row==15:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(1, 15))
                if line==2 and row==15:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(2, 15))
                if line==3 and row==15:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(3, 15))
                if line==4 and row==15:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(4, 15))
                if line==5 and row==15:
                    gui.add_button(x=myX, y=myY, w=25, h=25, origin='center', text=pattern[line][row], onclick=lambda: change(5, 15))

                row=row-8

            row=row+1
            myX=myX+28

        myY=myY+25
        line=line+1

    myY=myY+40

    #gui.add_button(x=120, y=230, w=100, h=30, text="Play", origin='center', onclick=lambda: play())
    gui.draw_image(x=120, y=265, w=92, h=33, image='/home/images/start.jpg', origin='center', onclick=lambda: play())
    gui.draw_text(x = 120,y=290,text="Roni Bandini - 9/2023 - Argentina", font_size=10, color="white", origin='top')

def play():

    global isPlaying

    if isPlaying==0:

        print("Exporting...")
        with open('/home/beats.txt', 'w') as f:
            f.write('Song:\n')
            f.write('  Tempo: '+str(tempo)+'\n')
            f.write('  Flow:\n')
            f.write('    - Verse:  x16\n')
            f.write('  Kit:\n')
            f.write('    - bassdrum:     BD.WAV\n')
            f.write('    - snaredrum:    SD.WAV\n')
            f.write('    - clsdhihat:    CH.WAV\n')
            f.write('    - openhihat:    OH.WAV\n')
            f.write('    - rimshot:      RS.WAV\n')
            f.write('    - maracas:      MA.WAV\n')
            f.write('\n')

            f.write('Verse:\n')
            f.write('  - bassdrum:     '+''.join(pattern[0])+'\n')
            f.write('  - snaredrum:    '+''.join(pattern[1])+'\n')
            f.write('  - clsdhihat:    '+''.join(pattern[2])+'\n')
            f.write('  - openhihat:    '+''.join(pattern[3])+'\n')
            f.write('  - rimshot:      '+''.join(pattern[4])+'\n')
            f.write('  - maracas:      '+''.join(pattern[5])+'\n')

        print("Beats...")
        subprocess.run(["beats", "/home/beats.txt"])
        print("Play...")

        updateScreenPlaying()
        audio.start_play('/home/beats.wav')
        isPlaying=1


    else:
        print("Stop")
        audio.stop_play()
        updateScreen()
        isPlaying=0


def change(line, row):

    buzzer.pitch(220, 1)
    #print("Changing cursor for "+str(line)+"-"+str(row))
    #print("Current content: "+str(pattern[line][row]))

    if str(pattern[line][row])==".":
        pattern[line][row]="X"
    else:
        pattern[line][row]="."

    updateScreen()


updateScreen()

# main loop

while True:

    # read pot values

    v1 = pot1.read_analog()
    v2 = pot2.read_analog()

    # change tempo
    if v1<1500:
        print("Changing tempo")
        tempo=tempo+5
        if tempo>200:
            tempo=200
        updateScreen()
        time.sleep(1)
    if v1>2300:
        print("Changing tempo")
        tempo=tempo-5
        if tempo<40:
            tempo=40
        updateScreen()
        time.sleep(1)

    # change page
    if v2>2300:
        if page==1:
            print("Changing page")
            page=2
            updateScreen()
            time.sleep(1)

    if v2<1500:
        if page==2:
            print("Changing page")
            page=1
            updateScreen()
            time.sleep(1)

    time.sleep(1)
