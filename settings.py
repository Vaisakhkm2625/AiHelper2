import os
import configparser

# Function to load settings
def load_settings(config_file,app_name):
    config = configparser.ConfigParser()

    config_dir=os.path.dirname(config_file)
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    if not os.path.exists(config_file):
        config["SETTINGS"] = {
            "openai_key": "",
            "ocr_option": "tesseract",
            "keybinding_to_start_typing": "b+k+r",
            "keybinding_to_stop_typing": "e+k+r",
            "keybinding_to_resume_typing": "<ctrl>+<alt>+r",
            "keybinding_to_take_screenshot": "<ctrl>+<alt>+s",
            "keybinding_to_sent_image_to_chat_gpt": "<ctrl>+<alt>+o",
            "keybinding_to_type_clipboard_contents": "<ctrl>+<alt>+p",
            "type_delay_upper_bound": "0.5",
            "type_delay_lower_bound": "0.1",
            "fake_app_name":"avg antivirus"

        }
        with open(config_file, 'w') as configfile:
            config.write(configfile)
    else:
        config.read(config_file)

    
    settings = {
        "openai_key": config.get("SETTINGS", "openai_key", fallback=""),
        "ocr_option": config.get("SETTINGS", "ocr_option", fallback="tesseract"),
        "keybinding_to_start_typing": config.get("SETTINGS", "keybinding_to_start_typing", fallback="b+k+r"),
        "keybinding_to_stop_typing": config.get("SETTINGS", "keybinding_to_stop_typing", fallback="e+k+r"),
        "keybinding_to_resume_typing": config.get("SETTINGS", "keybinding_to_resume_typing", fallback="c+k+r"),
        "keybinding_to_take_screenshot": config.get("SETTINGS", "keybinding_to_take_screenshot", fallback="<ctrl>+<alt>+s"),
        "keybinding_to_sent_image_to_chat_gpt": config.get("SETTINGS", "keybinding_to_sent_image_to_chat_gpt", fallback="<ctrl>+<alt>+o"),
        "keybinding_to_type_clipboard_contents": config.get("SETTINGS", "keybinding_to_type_clipboard_contents", fallback="<ctrl>+<alt>+p"),
        "type_delay_upper_bound": config.get("SETTINGS", "type_delay_upper_bound", fallback="0.5"),
        "type_delay_lower_bound": config.get("SETTINGS", "type_delay_lower_bound", fallback="0.1"),
        "fake_app_name": config.get("SETTINGS", "fake_app_name", fallback=app_name)
    }
    
    return settings



# Function to save settings
def save_settings(config_file, settings):
    config = configparser.ConfigParser()
    config["SETTINGS"] = settings
    
    with open(config_file, 'w') as configfile:
        config.write(configfile)

