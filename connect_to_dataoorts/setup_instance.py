import subprocess
import os
import sys
import utils

# -------------------------
# CONFIGURATION
# -------------------------

# 👉 Change these before running
PATH = r"D:\code\Course\SLM\tempfile"
ssh_cmd = r'ssh -i temporary.pem ubuntu@149.36.1.41 -p 22'


PUBLIC_IP = utils.extract_public_ip(ssh_cmd)
print("Extracted PUBLIC_IP:", PUBLIC_IP)

PEM_PATH = utils.temporary(PATH)
print("PEM file PATH:", PEM_PATH)

# -------------------------
# Helper function
# -------------------------

def run(cmd):
    print(f"\n>>> Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("ERROR:", result.stderr)

# -------------------------
# Check if file exists
# -------------------------

if not os.path.exists(PEM_PATH):
    print(f"❌ PEM file not found at: {PEM_PATH}")
    sys.exit(1)

print("\n==============================")
print("  PEM PERMISSION FIX SCRIPT")
print("==============================\n")

print(f"Using PEM File: {PEM_PATH}")
print(f"Using Public IP: {PUBLIC_IP}\n")

# -------------------------
# Commands to run
# -------------------------

commands = [

    # 1. Take ownership
    fr'takeown /f "{PEM_PATH}"',

    # 2. Reset ACLs
    fr'icacls "{PEM_PATH}" /reset',

    # 3. Disable inheritance
    fr'icacls "{PEM_PATH}" /inheritance:r',

    # 4. Remove unwanted ACL entries
    fr'icacls "{PEM_PATH}" /remove "BUILTIN\Administrators"',
    fr'icacls "{PEM_PATH}" /remove "BUILTIN\Users"',
    fr'icacls "{PEM_PATH}" /remove "NT AUTHORITY\SYSTEM"',
    fr'icacls "{PEM_PATH}" /remove "NT AUTHORITY\Authenticated Users"',
    fr'icacls "{PEM_PATH}" /remove "BUILTIN\BUILTIN"',

    # 5. Grant only your user read access
    fr'icacls "{PEM_PATH}" /grant:r "{os.getlogin()}":R',

    # 6. Verify final permissions
    fr'icacls "{PEM_PATH}"'
]

# -------------------------
# Execute all commands
# -------------------------

for cmd in commands:
    run(cmd)

# -------------------------
# Print SSH Command
# -------------------------

print("\n==============================")
print("   ✔ DONE — PEM FIXED")
print("==============================\n")

print("==========================================================================================")
ssh_command = f'ssh -i "{PEM_PATH}" ubuntu@{PUBLIC_IP} -p 22'
print("Use this command to connect to your GPU server: \n")
print(f"👉 {ssh_command} \n")
print("whoami")
print("nvidia-smi")
print("==========================================================================================\n")