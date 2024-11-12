# AiHelper

Total downloads: [![Github All Releases](https://img.shields.io/github/downloads/Vaisakhkm2625/AiHelper2/total.svg)]()


A app that listens for keybindings and do various tasks


go to release page and download exe file
https://github.com/Vaisakhkm2625/AiHelper2/releases/tag/v0.0.2


## For developers

for getting nix flake for this project, checkout 

running the app for windows

```
git clone git@github.com:Vaisakhkm2625/AiHelper2.git
# or 
git clone https://github.com/Vaisakhkm2625/AiHelper2.git
.\venv\Scripts\activate
pip install -r requirements.txt
python main.py

```
releasing the file
```
pyinstaller.exe --onefile --windowed --icon=logo.ico --name aihelper main.py
```

## Limitaion

- currently do not support wayland on linux(i tried its hard to due security)

