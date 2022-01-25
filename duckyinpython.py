from operator import truediv
from sre_constants import REPEAT
import usb_hid 
from adafruit_hid.keyboard import Keyboard 

from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout
from adafruit_hid.keycode import Keycode 
import time 
import digitalio
from board import*
led = digitalio.DigitalIO(LED)
led.direction = digitalio.Direction.OUTPUT 

duckyCommands = {
    'WINDOWS': Keycode.WINDOWS, 'GUI': Keycode.GUI,
    'APP': Keycode.APPLICATION, 'MENU': Keycode.APPLICATION, 'SHIFT': Keycode.SHIFT,
    'ALT': Keycode.ALT, 'CONTROL': Keycode.CONTROL, 'CTRL': Keycode.CONTROL,
    'DOWNARROW': Keycode.DOWN_ARROW, 'DOWN': Keycode.DOWN_ARROW, 'LEFTARROW': Keycode.LEFT_ARROW,
    'LEFT': Keycode.LEFT_ARROW, 'RIGHTARROW': Keycode.RIGHT_ARROW, 'RIGHT': Keycode.RIGHT_ARROW,
    'UPARROW': Keycode.UP_ARROW, 'UP': Keycode.UP_ARROW, 'BREAK': Keycode.PAUSE,
    'PAUSE': Keycode.PAUSE, 'CAPSLOCK': Keycode.CAPS_LOCK, 'DELETE': Keycode.DELETE,
    'END': Keycode.END, 'ESC': Keycode.ESCAPE, 'ESCAPE': Keycode.ESCAPE, 'HOME': Keycode.HOME,
    'INSERT': Keycode.INSERT, 'NUMLOCK': Keycode.KEYPAD_NUMLOCK, 'PAGEUP': Keycode.PAGE_UP,
    'PAGEDOWN': Keycode.PAGE_DOWN, 'PRINTSCREEN': Keycode.PRINT_SCREEN, 'ENTER': Keycode.ENTER,
    'SCROLLLOCK': Keycode.SCROLL_LOCK, 'SPACE': Keycode.SPACE, 'TAB': Keycode.TAB,
    'BACKSPACE': Keycode.BACKSPACE,
    'A': Keycode.A, 'B': Keycode.B, 'C': Keycode.C, 'D': Keycode.D, 'E': Keycode.E,
    'F': Keycode.F, 'G': Keycode.G, 'H': Keycode.H, 'I': Keycode.I, 'J': Keycode.J,
    'K': Keycode.K, 'L': Keycode.L, 'M': Keycode.M, 'N': Keycode.N, 'O': Keycode.O,
    'P': Keycode.P, 'Q': Keycode.Q, 'R': Keycode.R, 'S': Keycode.S, 'T': Keycode.T,
    'U': Keycode.U, 'V': Keycode.V, 'W': Keycode.W, 'X': Keycode.X, 'Y': Keycode.Y,
    'Z': Keycode.Z, 'F1': Keycode.F1, 'F2': Keycode.F2, 'F3': Keycode.F3,
    'F4': Keycode.F4, 'F5': Keycode.F5, 'F6': Keycode.F6, 'F7': Keycode.F7,
    'F8': Keycode.F8, 'F9': Keycode.F9, 'F10': Keycode.F10, 'F11': Keycode.F11,
    'F12': Keycode.F12,

}
def convertLine(line):
    newline = []
    for key in filter(None, line.aplit(" ")):
        key = key.upper()
        command_keycode = duckyCommands.get(key, None)
        if command_keycode is not None:
            newline.append(command_keycode)
        elif hasattr(Keycode, key):
            newline.append(getattr(Keycode, key))
        else:
            print("/n Unknown key: <{key}>")
    return newline 
def runScript(line):
    for k in line:
        kbd.press(k)
    kbd.release_all()
def sendString(line):
    layout.write(line)
def parseLine(line):
    if(line[0:3] == "REM"):
        pass
    elif(line[0:4] == "DELAY"):
        pass
    elif(line[0:5] == "String"):
        pass
    elif(line[0:6] == "Print"):
        pass
    elif(line[0:7] == "Import"):
        pass
    elif(line[0:8] == "Default_Delay"):
        pass
    elif(line[0:9] == "Default_Delay"):
        pass
    elif(line[1:3] == "Default_Forward"):
        pass
    elif(line[1:4] == "Led"):
        pass 
    if(led.value == True):
        led.value = False
    else:
        led.value = True
    else:
        newScriptLine = convertLine(line)
        runScriptLine(newScriptLine)
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)
time.sleep(.5)
progStatus = False
progStatusPin = digitalio.DigitalInputOutput(GPIO)
progStatusPin.switch_to_input(pull=digitalio.Pull.UP)
progStatus = not progStatusPin.value
defaultDelay = 0
def runScript(file):
    global defaultDelay

    duckyScriptPath = filef = open(duckyScriptPath,"r",encoding='utf-8')
    previousLine = ""
    duckyScript = f.readLines()
    for linr in duckyScript:
        line = line.rstrip()
        if(line[0:6] == "REPEAT"):
            for i in range(int(line[0:7])):
                parseLine(previousLine)
                time.sleep(float(defaultDelay)/1000)
        else:
            parseLine(line)
            previosLine = line
        time.sleep(float(defaultDelay)/1000)
if(progStatus == False):
    print("Running selected payload")
    runScript("payload.dd")
    print("Done")
else:
    print("Update or change your selected payload file")
    