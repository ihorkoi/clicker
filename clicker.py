import time
import threading

from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 0.5
button = Button.left
start_key = KeyCode(char='a')
end_key = KeyCode(char='b')


class AutoClicker(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.active = True
        self.mouse = Controller()

    def exit(self):
        self.active = False

    def run(self):
        while self.active:
            self.mouse.click(self.button)
            time.sleep(self.delay)


clicker = AutoClicker(delay=delay, button=button)
clicker.start()


class MacroReader(threading.Thread):
    def __init__(self, toggle_key):
        super().__init__()
        self.active = True
        self.record = {}
        self.toggle_key = toggle_key
        pass

    def run(self, key):
        if key == self.toggle_key:
            while self.active:
                pass

    def exit():
        pass

    def save_config(self):
        pass


def on_press(key):
    print(key)
    if key == end_key:
        clicker.exit()
        return False


with Listener(on_press=on_press) as listener:
    listener.join()
