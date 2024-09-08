# AiHelper

A app that listens for keybindings and do various tasks


got to release page and download exe file


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

