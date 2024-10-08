import copykitten
from pynput.keyboard import Controller, Key
import threading
import time
import random

class ClipboardTyper:
    def __init__(self, type_delay_upper_bound,type_delay_lower_bound):
        self.keyboard = Controller()
        self._typing_thread = None
        self._stop_event = threading.Event()
        self.type_delay_upper_bound = type_delay_upper_bound
        self.type_delay_lower_bound = type_delay_lower_bound

    def _type_clipboard_content(self):
        clipboard_content = copykitten.paste()

        # Simulate typing out the clipboard content
        for char in clipboard_content:
            if self._stop_event.is_set():
                break  # Stop typing if the event is set

            if char.isupper() or char in "~!@#$%^&*()_+{}:\"<>?":  # Characters that require Shift
                with self.keyboard.pressed(Key.shift):
                    self.keyboard.type(char)
            else:
                self.keyboard.type(char)
            time.sleep(random.uniform(float(self.type_delay_lower_bound),float(self.type_delay_upper_bound))) 


        # Optionally, press Enter after typing
        if not self._stop_event.is_set():
            self.keyboard.press(Key.enter)
            self.keyboard.release(Key.enter)

    def start_typing(self):
        # Reset the stop event
        self._stop_event.clear()

        # Create and start the typing thread as a daemon
        self._typing_thread = threading.Thread(target=self._type_clipboard_content)
        self._typing_thread.daemon = True  # Set the thread as a daemon
        self._typing_thread.start()

    def stop_typing(self):
        # Set the stop event to signal stopping
        self._stop_event.set()

if __name__ == "__main__":
# Example usage:
    typer = ClipboardTyper()
    typer.start_typing()

# To stop typing:
# typer.stop_typing()
