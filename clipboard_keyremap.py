from pynput import keyboard
import copykitten
import time


class Remapper:

    def __init__(self):
        self.replacement_string = "oopsy"
        self.listener = None
        self.index = 0
        self.controller = keyboard.Controller()
        self.is_remapping = False  # Flag to prevent recursion during remapping

    def on_press(self, key):
        try:
            if not self.is_remapping:
                # Suppress original key and replace it with custom input
                if self.index < len(self.replacement_string):
                    # Set the flag to prevent recursion
                    self.is_remapping = True

                    # Inject the next character from the replacement string
                    self.controller.press(self.replacement_string[self.index])
                    self.controller.release(self.replacement_string[self.index])
                    self.index += 1

                    # Reset the flag after injecting input
                    self.is_remapping = False

                # Stop listening if we've finished replacing
                if self.index >= len(self.replacement_string):
                    return False

        except AttributeError:
            pass  # Ignore non-character keys like shift, ctrl, etc.

    def on_release(self, key):
        # Stop the listener if ESC is pressed
        if key == keyboard.Key.esc:
            return False

    def start_remapping(self):
        print('replacing with clipboard content')
        self.index = 0
        self.replacement_string = copykitten.paste()
        print(self.replacement_string)

        # Use context management to automatically clean up the listener
        if self.listener is None or not self.listener.running:
            self.listener = keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release,
                suppress=True  # Suppress user inputs
            )
            self.listener.start()

    def stop_remapping(self):
        print('keybinding_to_stop_typing pressed')
        if self.listener:
            self.listener.stop()
            self.listener = None


if __name__ == '__main__':
    r = Remapper()
    r.start_remapping()
    time.sleep(10)
    r.stop_remapping()
    time.sleep(10)
