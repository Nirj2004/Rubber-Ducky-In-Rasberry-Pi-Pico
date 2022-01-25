pico-ducky
Make a cheap but powerful USB Rubber Ducky with a Raspberry Pi Pico

GitHub code size in bytes GitHub license GitHub contributors GitHub commit activity GitHub Repo stars

Install

Install and have your USB Rubber Ducky working in less than 5 minutes.

    Download CircuitPython for the Raspberry Pi Pico. *Updated to 7.0.0

    Plug the device into a USB port while holding the boot button. It will show up as a removable media device named RPI-RP2.

    Copy the downloaded .uf2 file to the root of the Pico (RPI-RP2). The device will reboot and after a second or so, it will reconnect as CIRCUITPY.

    Download adafruit-circuitpython-bundle-7.x-mpy-YYYYMMDD.zip here and extract it outside the device.

    Navigate to lib in the recently extracted folder and copy adafruit_hid to the lib folder in your Raspberry Pi Pico.

    Click here, press CTRL + S and save the file as code.py in the root of the Raspberry Pi Pico, overwriting the previous file.

    Find a script here or create your own one using Ducky Script and save it as payload.dd in the Pico.

    Be careful, if your device isn't in setup mode, the device will reboot and after half a second, the script will run.

Setup mode

To edit the payload, enter setup mode by connecting the pin 1 (GP0) to pin 3 (GND), this will stop the pico-ducky from injecting the payload in your own machine. The easiest way to so is by using a jumper wire between those pins as seen bellow.

Setup mode with a jumper
USB enable/disable mode

If you need the pico-ducky to not show up as a USB mass storage device for stealth, follow these instructions.
Enter setup mode.
Copy boot.py to the root of the pico-ducky.
Copy your payload script to the pico-ducky.
Disconnect the pico from your host PC. Connect a jumper wire between pin 18 and pin 20. This will prevent the pico-ducky from showing up as a USB drive when plugged into the target computer.
Remove the jumper and reconnect to your PC to reprogram. The default mode is USB mass storage enabled.

USB enable/disable mode
Changing Keyboard Layouts

Copied from Neradoc/Circuitpython_Keyboard_Layouts
How to use one of these layouts with the pico-ducky repository.

Go to the latest release page, look if your language is in the list.
If your language/layout is in the bundle

Download the py zip, named circuitpython-keyboard-layouts-py-XXXXXXXX.zip

NOTE: You can use the mpy version targetting the version of Circuitpython that is on the device, but on Raspberry Pi Pico you don't need it - they only reduce file size and memory use on load, which the pico has plenty of.
If your language/layout is not in the bundle

Try the online generator, it should get you a zip file with the bundles for yout language

https://www.neradoc.me/layouts/
Now you have a zip file
Find your language/layout in the lib directory

For a language LANG, copy the following files from the zip's lib folder to the lib directory of the board.
DO NOT modify the adafruit_hid directory. Your files go directly in lib.
DO NOT change the names or extensions of the files. Just pick the right ones.
Replace LANG with the letters for your language of choice.

    keyboard_layout.py
    keyboard_layout_win_LANG.py
    keycode_win_LANG.py

Don't forget to get the adafruit_hid library.

This is what it should look like if your language is French for example.

CIRCUITPY drive screenshot
Modify the pico-ducky code to use your language file:

At the start of the file comment out these lines:

from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout
from adafruit_hid.keycode import Keycode

Uncomment these lines:
Replace LANG with the letters for your language of choice. The name must match the file (without the py or mpy extension).

from keyboard_layout_win_LANG import KeyboardLayout
from keycode_win_LANG import Keycode

Useful links and resources
Docs

CircuitPython

CircuitPython HID

Ducky Script
Video tutorials

pico-ducky tutorial by NetworkChuck

USB Rubber Ducky playlist by Hak5

CircuitPython tutorial on the Raspberry Pi Pico by DroneBot Workshop
