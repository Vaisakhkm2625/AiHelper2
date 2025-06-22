from pystray import Menu,MenuItem,Icon
from pynput import keyboard

import pprint

import os
from PIL import Image, ImageDraw
from generate_penguin_logo import draw_penguin_logo
from settings import load_settings, save_settings
from screenshot import take_and_crop_screenshot_thread
from clipboard_keyremap import Remapper
import  ui
import openaivision
import platformdirs
from type_paste import ClipboardTyper


app_auther = "vaisaskh"
app_name = "aihelper"
fake_app_name = app_name

config_dir = platformdirs.user_config_dir(app_name,app_auther)
config_file = os.path.join(config_dir,"settings.ini")
image_file_path = os.path.join(config_dir,"cropped_screenshot.png")

print(config_file)


settings = load_settings(config_file,app_name)


class HotkeyManager:

    def __init__(self):
        self.keyboard_instance = None
        self.listener = Remapper()
        self.clipboardtyper = ClipboardTyper(settings['type_delay_lower_bound'],settings['type_delay_upper_bound'])

    def start_key_remapping(self):
        print('on_start_remapping_pressed')
        self.listener.start_remapping()

    def resume_key_remapping(self):
        print('keybinding_to_resume_remapping pressed')
        self.listener.resume_remapping()

    def stop_key_remapping(self):
        print('keybinding_to_stop_remapping pressed')
        self.listener.stop_remapping()

    def take_screenshot(self):
        print('take screenshot pressed')
        take_and_crop_screenshot_thread(image_file_path)

    def sent_image_to_chat_gpt(self):
        print('senting image to open ai')
        openaivision.openai_image_reponse(settings['openai_key'],image_file_path)

    def start_type_from_clipboard(self):
        print('typing clipboard')
        #typer = ClipboardTyper(settings['type_delay_lower_bound'],settings['type_delay_upper_bound'])
        #typer.start_typing()
        self.clipboardtyper.start_typing()

    def resume_type_from_clipboard(self):
        print('resume typing clipboard')
        self.clipboardtyper.resume_typing()

    def stop_type_from_clipboard(self):
        print('typing clipboard')
        #typer = ClipboardTyper(settings['type_delay_lower_bound'],settings['type_delay_upper_bound'])
        #typer.start_typing()
        self.clipboardtyper.stop_typing()


    def start_hotkeys(self):
        if self.keyboard_instance is None:

            # here we set the global keybindings from 
            # the settings
            keybinding_prefix = "keybinding_to_"
            self.keyboard_instance = keyboard.GlobalHotKeys({
                settings[key]: getattr(self, key.replace(keybinding_prefix, ""))
                for key in settings
                if key.startswith(keybinding_prefix) and hasattr(self, key.replace(keybinding_prefix, ""))
            })

            self.keyboard_instance.start()

    def stop_hotkeys(self):
        if self.keyboard_instance:
            self.keyboard_instance.stop()
            self.keyboard_instance = None



#def on_press(ev):
#    print(ev)
#
#with keyboard.Listener(on_press=on_press) as listener:
#    listener.join()
#

# Initialize HotkeyManager
hotkey_manager = HotkeyManager()
hotkey_manager.start_hotkeys()

icon = Icon(
    'Start Listening',
    icon=draw_penguin_logo(64, 64),
    menu=Menu(
        MenuItem('Start Hotkeys', hotkey_manager.start_hotkeys),
        MenuItem('Stop Hotkeys', hotkey_manager.stop_hotkeys),
        MenuItem('Show Settings',lambda: ui.create_settings_gui(config_file,app_name)),
        MenuItem('Quit', lambda: icon.stop())
    )
)

icon.run()

