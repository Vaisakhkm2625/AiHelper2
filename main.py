from pystray import Menu,MenuItem,Icon
from pynput import keyboard

import os
from PIL import Image, ImageDraw
from generate_penguin_logo import draw_penguin_logo
from settings import load_settings, save_settings
from screenshot import take_and_crop_screenshot_thread
from clipboard_keyremap import Remapper
import  ui
import openaivision
import platformdirs


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

    def on_start_remapping_pressed(self):
        print('on_start_remapping_pressed')
        self.listener.start_remapping()

    def on_stop_remapping_pressed(self):
        print('keybinding_to_stop_remapping pressed')
        self.listener.stop_remapping()

    def on_take_screenshot_pressed(self):
        print('take screenshot pressed')
        take_and_crop_screenshot_thread(image_file_path)

    def on_sent_image_to_chat_gpt_pressed(self):
        print('senting image to open ai')
        openaivision.openai_image_reponse(settings['openai_key'],image_file_path)

    def on_press(self, key):
        print(f"Key pressed: {key}")

    def on_release(self, key):
        print(f"Key released: {key}")

    def start_hotkeys(self):
        if self.keyboard_instance is None:
            self.keyboard_instance = keyboard.GlobalHotKeys({
                settings['keybinding_to_start_typing']: self.on_start_remapping_pressed,
                settings['keybinding_to_stop_typing']: self.on_stop_remapping_pressed,
                settings['keybinding_to_take_screenshot']: self.on_take_screenshot_pressed,
                settings['keybinding_to_sent_image_to_chat_gpt']: self.on_sent_image_to_chat_gpt_pressed
            })
            self.keyboard_instance.start()

    def stop_hotkeys(self):
        if self.keyboard_instance:
            self.keyboard_instance.stop()
            self.keyboard_instance = None



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

