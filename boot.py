from board import* 
import digitalio
import storage

noStorageStatus = False 
noStoragePin = digitalio.DigitalInOut(GP15)
noStoragePin.switch_to_input(pull=digitalio.Pull.UP)
noStorageStatus = not noStoragePin.value

if(noStorageStatus == True):
    # dont show USB drive to Host PC
    storage.disable_usb_drive()
    print("Disabling Usb drive() to retieve go to task manager and select unwanted task, select and press the end task button")
else: 
    # for normal boot up :
    print("USB drive enabled")
    