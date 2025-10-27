<h1 align="center" id="title">Z e h e f</h1><br>

![](assets/zehef_logo.png)

[![python version](https://img.shields.io/badge/Python-3.10%2B-brightgreen)](https://www.python.org/downloads/)
[![license](https://img.shields.io/badge/License-GNU-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.fr.html)

# **Zehef is an osint tool who studies the emails 📩**

# **😇 Abouts zehef**

> Zehef v2 is a tool focused on finding public information on a targeted email.

## 🌠 Features

- Check if the email is in a paste ([Pastebin](https://fr.wikipedia.org/wiki/Pastebin.com))
- Find leaks with [HudsonRock](https://www.hudsonrock.com/)
- Checking social media accounts (Instagram, Spotify, Deezer, Adobe, 𝕏 etc...)
- Generate email combinations


## **📦 Installation**

- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

```
$ git clone https://github.com/N0rz3/Zehef.git
$ cd ./Zehef
$ pip3 install -r requirements.txt
```

## **🎲 Usage**

```
usage: zehef.py [-h] [email]

positional arguments:
  email       Search informations on email (breaches, pastes, accounts ...)

options:
  -h, --help  show this help message and exit
```
![](assets/terminal.jpg)

### `$ python3 zehef.py email@domain.com `

## **🌞 More**

## Building a Windows standalone executable (optional)

You can build a single-file Windows executable using PyInstaller. The repository includes a helper PowerShell script `build_exe.ps1` to automate the build inside a temporary venv.

From the repository root (PowerShell):

```powershell
# Build (creates .\build_venv, installs PyInstaller, and builds .\dist\Zehef.exe)
.\build_exe.ps1

# Clean previous venv and build, then rebuild
.\build_exe.ps1 -Clean
```

After the build completes the executable will be at `./dist/Zehef.exe`. Run it from a command prompt:

```powershell
.\dist\Zehef.exe email@domain.com
```

Alternatively you can keep using the PowerShell launcher `run_zehef.ps1` (already included) which detects a Python 3 interpreter and runs `zehef.py` forwarding any arguments:

```powershell
.\run_zehef.ps1 email@domain.com
```

Notes:
- The build script creates a local virtual environment (`build_venv`) to avoid changing your global Python environment.
- You can edit `build_exe.ps1` to add an icon or other PyInstaller options.
- Creating an installer (Inno Setup) or a GUI wrapper can be added as a follow-up.
- Creating an installer (Inno Setup) can be added as a follow-up.

### Building the GUI executable

The repository includes a minimal Tkinter GUI at `zehef_gui.py`. To build a windowed GUI executable (no console) run the build script with the `-Target gui` flag:

```powershell
# Build GUI exe (creates .\build_venv and .\dist\ZehefGUI.exe)
.\build_exe.ps1 -Target gui

# Build GUI exe with a custom icon (relative to repo root)
.\build_exe.ps1 -Target gui -Icon assets\zehef_icon.ico
```

After the build completes you will have `./dist/ZehefGUI.exe` which can be launched by double-clicking or from a Start menu/installer.

If you prefer the console CLI exe instead, build with `-Target cli` (default):

```powershell
.\build_exe.ps1 -Target cli
```

## Electron desktop app (Windows exe)

You can wrap the FastAPI web UI in an Electron shell to produce a native desktop application (exe). The repository includes a scaffold under `web/electron/` and a helper script `build_electron.ps1`.

Prerequisites:
- Node.js + npm (for electron and electron-builder)
- Python 3 and the project dependencies (see `requirements.txt`)

Dev run (start backend + Electron window):

```powershell
# from repo root
cd web\electron
npm install
npm start
```

Build distributable (Windows EXE/installer):

```powershell
# from repo root
.\build_electron.ps1
```

Notes:
- `build_electron.ps1` runs `npm install` and then `electron-builder` (configured in `web/electron/package.json`). The produced artifacts are under `electron_dist`.
- The Electron main process starts the FastAPI backend (using your system Python) and opens the frontend in a window. Ensure Python + project deps are available on the machine that runs the packaged app.
- Packaging with electron-builder will include the Node side, but the Python backend is started from the system Python at runtime; for a fully standalone product you would need to bundle the Python runtime and your app (more advanced). I can help with that next if you want.


### **✔️ / ❌ Rules**

- **This tool was designed for educational purposes only and is not intended for any mischievous use, I am not responsible for its use.**


### **📜 License**

- **This project is [License GPL v3](https://www.gnu.org/licenses/gpl-3.0.fr.html) be sure to follow all rules 👍**

### **💖 Thanks**
- If you like what i do please subscribe 💖. And if you find this tool is useful don't forget to star 🌟

- 💶 Support me 👇

<a href="https://www.buymeacoffee.com/norze" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="50" ></a> 
