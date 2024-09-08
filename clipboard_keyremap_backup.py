from pynput import keyboard
import copykitten
import time


class Remapper:


# The string to type instead of the user's input
    replacement_string = "oopsy"

    listener = None
    index = 0  

    def on_press(self,key):
        global index
        try:
            # Intercept any key press and type the next character of the replacement string
            if self.index >= len(self.replacement_string):
                return False
            if key.char!= self.replacement_string[self.index]:
                keyboard.Controller().press(self.replacement_string[self.index])
                keyboard.Controller().release(self.replacement_string[self.index])
                self.index += 1
            

        except AttributeError:
            pass

    def on_release(self,key):
        # Stop the listener if ESC is pressed
        if key == keyboard.Key.esc:
            return False
        if self.index >= len(self.replacement_string):
            return False



    def start_remapping(self):
        print('replacing with clipboard content') 
        self.index = 0
        self.replacement_string = copykitten.paste()
        print(self.replacement_string)
        # Use context management to automatically clean up the listener
        if self.listener is None or not self.listener.running:
            self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release,suppress=True)
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
