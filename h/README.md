# 🚀 Connect to Dataoorts GPU on Windows

### *Complete Step-by-Step Tutorial (Fix `.pem` Permissions + SSH Access)*

This guide walks you through the **exact steps required to connect to a Dataoorts GPU instance from Windows**, including fixing `.pem` file permissions, configuring PowerShell, and verifying your GPU once connected.

This README is written to be:

✔ Beginner-friendly
✔ Practical and executable
✔ Cleanly structured
✔ Verified commands used by Utkarsh

---

## 📌 **Prerequisites**

Before starting, ensure:

* You are on **Windows 10 / 11**
* You have:

  * A **`.pem` key file** (for SSH authentication)
  * A **Dataoorts GPU public IP**
  * The **Ubuntu username** (usually `ubuntu`)
* Windows **PowerShell** is available
* **OpenSSH** is installed (default in Windows 10/11)

---

# 1️⃣ Fix `.pem` File Permissions (Mandatory for SSH)

Windows assigns extra users and ACL entries to files by default, which SSH **rejects**.
We must clean the permissions so **only your user account** can read the file.

---

## ### **Step 1 — Open PowerShell as Administrator**

Right-click → **Run as Administrator**
This is required to modify ownership and ACLs.

---

## ### **Step 2 — Navigate to the folder containing your `.pem`**

```powershell
cd "D:\path\to\your\pem\folder"
```

Example:

```powershell
cd "D:\code\Course\SLM - Copy"
```

---

## ### **Step 3 — Take ownership of the `.pem` file**

```powershell
takeown /f "temporary.pem"
```

You should see confirmation like:

```
SUCCESS: The file (temporary.pem) is now owned by: DESKTOP-XXXX\Utkarsh
```

---

## ### **Step 4 — Reset all inherited permissions**

```powershell
icacls "temporary.pem" /reset
```

---

## ### **Step 5 — Disable permission inheritance**

```powershell
icacls "temporary.pem" /inheritance:r
```

This removes Windows’ default ACL inheritance.

---

## ### **Step 6 — Remove all existing users except you**

Run each command:

```powershell
icacls "temporary.pem" /remove "BUILTIN\Administrators"
icacls "temporary.pem" /remove "BUILTIN\Users"
icacls "temporary.pem" /remove "NT AUTHORITY\SYSTEM"
icacls "temporary.pem" /remove "NT AUTHORITY\Authenticated Users"
icacls "temporary.pem" /remove "BUILTIN\BUILTIN"
```

If any give “0 files processed”, that’s normal — it means the ACE didn’t exist.

---

## ### **Step 7 — Grant only your user read access**

```powershell
icacls "temporary.pem" /grant:r "$($env:USERNAME):R"
```

This is **mandatory** — SSH enforces “owner read only”.

---

## ### **Step 8 — Verify permissions**

```powershell
icacls "temporary.pem"
```

Correct output must look like:

```
temporary.pem DESKTOP-LE8RPT0\Utkarsh:(R)
```

✔ Only **one** user
✔ With **read** permission
✔ No inheritance
✔ No system/administrator entries

Your `.pem` file is now valid for SSH authentication 🎉

---

# 2️⃣ Connect to Your Dataoorts GPU Instance

With permissions fixed, run the SSH command:

```powershell
ssh -i temporary.pem ubuntu@YOUR_PUBLIC_IP -p 22
```

Example:

```powershell
ssh -i temporary.pem ubuntu@38.80.122.156 -p 22
```

If successful, you will see:

```
Welcome to Ubuntu 22.04.4 LTS
```

You are now inside the GPU server.

---

# 3️⃣ Verify Everything Is Working

Once connected:

---

## ### **Check which user you are logged in as**

```bash
whoami
```

Should return:

```
ubuntu
```

---

## ### **Check GPU availability**

```bash
nvidia-smi
```

This displays:

* GPU model
* CUDA version
* GPU usage
* Running processes
* Memory status

If you see this output → your Dataoorts GPU is fully accessible 🎉

---

# 4️⃣ (Optional) Run First-Time Setup

To make the server fully ML-ready:

---

## Install updates

```bash
sudo apt update && sudo apt upgrade -y
```

---

## Install Git

```bash
sudo apt install git -y
```

---

## Install Miniconda (recommended for Python environments)

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

Restart terminal:

```bash
source ~/.bashrc
```

---

## Create a GPU-enabled PyTorch environment

```bash
conda create -n gpu python=3.10 -y
conda activate gpu
```

Install PyTorch with CUDA:

```bash
pip install torch --index-url https://download.pytorch.org/whl/cu121
pip install torchvision torchaudio
```

Verify CUDA support:

```bash
python -c "import torch; print(torch.cuda.is_available())"
```

Expected output:

```
True
```

---

# 5️⃣ (Optional) Use VS Code Remote-SSH

Install the extension:

```
Remote - SSH
```

Add a new host:

```
ssh -i D:/path/to/temporary.pem ubuntu@YOUR_PUBLIC_IP
```

Then simply:

```
Connect
```

VS Code will open directly inside the GPU server — perfect for development.

---

# 🎉 You’re Done!

You have successfully:

✔ Fixed `.pem` permissions
✔ Connected to a Dataoorts GPU instance
✔ Verified CUDA & GPU access
✔ (Optionally) set up Python, PyTorch, and VS Code

---