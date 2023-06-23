![zehef](https://github.com/N0rz3/N0rz3/assets/123885505/461b9b47-a28b-4f52-891f-1c42ef2d92ac)

[![python version](https://img.shields.io/badge/Python-3.10%2B-brightgreen)](https://www.python.org/downloads/)
[![license](https://img.shields.io/badge/License-GNU-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.fr.html)


# **Zehef is a osint tool who studies the emails 📩**


# **😇 Abouts zehef**
### Zehef is an osint tool which does not warn the target 😎


**Features of script**
 - full async
 - asynchrone scraping 
 - menu in cli format (commands)


**Summary of modules**
 - account -> website scraping with holehe
 - breached -> checking of breachs and leaks 
 - rep -> api scraping for found the reputation of the target email
 - possbile accounts -> check on snapchat & tiktok if a account exist with several formats of username
 - pastebin -> check all links pastebin related to email


**🗃️ API**
 Name                 | Function                                | Key          |
| ------------------- | --------------------------------------  | ----------------- |
| [emailrep.io](https://emailrep.io/)             | check the reputation of email                                |    ✖️🔑         |



📒 Networks (possible accounts)
- [x] TikTok
- [x] Snapchat


### **💼 Workflow**


![workflow](https://github.com/N0rz3/Zehef/assets/123885505/26e24f44-24aa-42da-b88a-95c0c1a2c7dc)





## **🛠️ Requirements / Launch**

- [Python 3](https://www.python.org/downloads/)

```
git clone https://github.com/N0rz3/Zehef.git
cd Zehef
pip install -r requirements.txt
```


### **😲 Usage**
```python zehef.py```
```
v0.0.3
               __    ________  _____ 
________ ____ |  |__ \_____  \/ ____\
\___   // __ \|  |  \  _(__  <   __\ 
 /    /\  ___/|   Y  \/       \  |   
/_____ \\___  >___|  /______  /__|      (BY 🦊 @N0rz3) 
      \/    \/     \/       \/       

      😡 Zehef OSINT Tool



usage: zehef.py [-h] <email adress>

option:
    -h, --help          show this help message and exit
```


**📚 Example input:**

```python zehef.py example@example.com```

**📚 Example output:**

![demo (1)](https://github.com/N0rz3/Zehef/assets/123885505/b275e7a1-659b-4463-9f30-f56c28959b5a)
![demo (2)](https://github.com/N0rz3/Zehef/assets/123885505/54b0b6a8-07cf-4cd2-9a49-ad1598b05dc4)





## **🌞 More**


### **✔️ / ❌ Rules**

**this tool was designed for educational purposes only and is not intended for any mischievous use, I am not responsible for its use.**


### **📜 License**

**This project is [License GPL v3](https://www.gnu.org/licenses/gpl-3.0.fr.html) be sure to follow all rules 👍**

### **📢 Credits**

💻 Code by me 🤗

If you like what i do, please subscribe 💖. And if you find this tool is useful don't forget to star 🌟



## **😈 [Holehe](https://github.com/megadose/holehe) modules**
| Name                | Domain                                 | Method            | Frequent Rate Limit |
| ------------------- | -------------------------------------- | ----------------- | ------------------- |
| aboutme             | about.me                               | register          | ✘               |
| amazon              | amazon.com                             | login             | ✘               |
| bitmoji             | bitmoji.com                            | login             | ✘               |
| bodybuilding        | bodybuilding.com                       | register          | ✘               |
| deliveroo           | deliveroo.com                          | register          | ✔               |
| discord             | discord.com                            | register          | ✘               |
| github              | github.com                             | register          | ✘               |
| google              | google.com                             | register          | ✔               |
| gravatar            | gravatar.com                           | other             | ✘               |
| instagram           | instagram.com                          | register          | ✔               |
| laposte             | laposte.fr                             | register          | ✘               |
| nike                | nike.com                               | register          | ✘               |
| pinterest           | pinterest.com                          | register          | ✘               |
| pornhub             | pornhub.com                            | register          | ✘               |
| protonmail          | protonmail.ch                          | other             | ✘               |
| redtube             | redtube.com                            | register          | ✘               |
| smule               | smule.com                              | register          | ✔               |
| spotify             | spotify.com                            | register          | ✔               |
| twitter             | twitter.com                            | register          | ✘               |
| venmo               | venmo.com                              | register          | ✔               |
| wordpress           | wordpress                              | login             | ✘               |
| xnxx                | xnxx.com                               | register          | ✔               |
| xvideos             | xvideos.com                            | register          | ✘               |
| yahoo               | yahoo.com                              | login             | ✔               |
