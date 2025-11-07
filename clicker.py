import time
import threading

import pynput.mouse as p_mouse
import pynput.keyboard as p_keyboard

# from pynput.mouse import Button, Controller, Listener
# from pynput.keyboard import Listener, KeyCode

delay = 0.5
button = p_mouse.Button.left
start_key = p_keyboard.KeyCode(char='a')
end_key = p_keyboard.KeyCode(char='b')


class AutoClicker(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        # self.config = config
        self.active = True
        self.mouse = p_mouse.Controller()

    def exit(self):
        self.active = False

    def run(self):
        while self.active:
            self.mouse.click(self.button)
            time.sleep(self.delay)


# clicker = AutoClicker(delay=delay, button=button)
# clicker.start()


class MacroReader(threading.Thread):
    def __init__(self, toggle_key):
        super().__init__()
        self.active = True
        self.record_moves = []
        self.record_clicks = []
        self.record_scrolls = []
        self.toggle_key = toggle_key
        self.listener = p_mouse.Listener(on_move=self.on_move,
                                         on_click=self.on_click,
                                         on_scroll=self.on_scroll)

    def run(self):
        self.listener.start()
        self.listener.join()

    def on_move(self, x, y):
        if self.active:
            self.record_moves.append({"x": x, "y": y})

    def on_click(self, x, y, button, pressed):
        print(self.record_clicks)
        if self.active:
            self.record_clicks.append({"x": x, "y": y, "button": button})

    def on_scroll(self, x, y, dx, dy):
        if self.active:
            self.record_scrolls.append({"x": x, "y": y, "dx": dx, "dy": dy})

    def exit(self):
        self.active = False

    def save_config(self):
        pass


# def on_press(key):
#     if key == end_key:
#         clicker.exit()
#         return False


# with p_keyboard.Listener(on_press=on_press) as listener:
#     listener.join()

recorder = MacroReader(p_keyboard.KeyCode(char='p'))
recorder.start()
