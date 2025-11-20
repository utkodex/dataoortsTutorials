# 🚀 Connect VS Code to Dataoorts GPU Instance Using Remote-SSH

*A complete beginner-friendly and practical setup guide*

This guide walks you through the **exact steps** required to connect your **Windows machine**, **PEM key**, and **VS Code Remote-SSH** to a **Dataoorts GPU server**.
Once done, you'll be able to write, edit, and run code directly on the GPU instance from inside VS Code.

---

# 📌 Prerequisites

Before starting, make sure you have:

* A valid **Dataoorts GPU instance** (Ubuntu)

* A working **SSH command** like:

  ```
  ssh -i "D:\code\Course\SLM - Copy\temporary.pem" ubuntu@38.80.122.156 -p 22
  ```

* `.pem` file with correct permissions
  (Use the provided permission-fix script if needed)

* VS Code installed on Windows

---

# 🧩 1. Install the Remote-SSH Extension

1. Open **VS Code**

2. Click on **Extensions** (left sidebar)

3. Search for:

   ```
   Remote - SSH
   ```

4. Install the extension published by **Microsoft**

✔ This is the only extension required.

---

# 🛠 2. Open the Command Palette

Press:

```
Ctrl + Shift + P
```

Type:

```
Remote-SSH: Add New SSH Host
```

Select it and hit **Enter**.

---

# 🔑 3. Add Your SSH Command

Paste your full SSH command exactly as you use in PowerShell:

```
ssh -i "D:\code\Course\SLM - Copy\temporary.pem" ubuntu@38.80.122.156 -p 22
```

VS Code will then ask:

> **Where do you want to save the SSH configuration?**

Select:

```
C:\Users\<YourUser>\.ssh\config
```

For example:

```
C:\Users\Utkarsh\.ssh\config
```

---

# ✏️ 4. Verify / Edit `config` File

Open the SSH config file:

```
C:\Users\<YourUser>\.ssh\config
```

Make sure it looks like this (no quotes):

```
Host dataoorts
    HostName 38.80.122.156
    User ubuntu
    Port 22
    IdentityFile D:\code\Course\SLM - Copy\temporary.pem
```

### ✔ Important rules

* No extra quotes `" "`
* Full absolute path to `.pem`
* Correct username: `ubuntu`
* Correct port: `22`

---

# 🔌 5. Connect to the Remote GPU Machine

In VS Code:

1. Look at the **bottom-left corner**
2. Click the `><` Remote icon
3. Choose:

```
Connect to Host...
```

Then select:

```
dataoorts
```

VS Code will open a **new window** showing:

```
Opening Remote...
```

After 5–10 seconds, you are inside the GPU server.

---

# 🔐 6. First-Time Permission Warning (If Any)

If VS Code shows:

```
Permissions are too open: "temporary.pem"
```

It means your `.pem` file ACLs are incorrect.

Fix with your PEM permission script or manually run:

```
icacls "temporary.pem"
```

Make sure only **your user** has Read permissions.

---

# 🧪 7. Verify the Connection in VS Code Terminal

Open the terminal:

```
Ctrl + `
```

Check the user:

```bash
whoami
```

Expected:

```
ubuntu
```

Check the GPU:

```bash
nvidia-smi
```

If you see GPU details (driver version, CUDA version, memory usage, etc.) —
🎉 **your VS Code is now fully connected to the Dataoorts GPU instance!**

---