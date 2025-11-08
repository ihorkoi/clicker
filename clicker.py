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
toggle_record_key = p_keyboard.KeyCode(char='r')


class AutoClicker(threading.Thread):
    def __init__(self, delay, config=None):
        super().__init__()
        self.delay = delay
        # self.button = button
        self.config = config
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
    def __init__(self):
        super().__init__()
        self.active = True
        self.record_moves = []
        self.record_clicks = []
        self.record_scrolls = []
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
        if self.active and pressed:
            self.record_clicks.append({"x": x, "y": y, "button": button})
        print(self.record_clicks)

    def on_scroll(self, x, y, dx, dy):
        if self.active:
            self.record_scrolls.append({"x": x, "y": y, "dx": dx, "dy": dy})

    def exit(self):
        self.active = False

    def save_config(self):
        pass


recorder = MacroReader()


def on_press(key):
    macro_record = False
    if key == toggle_record_key and macro_record:
        recorder.exit()
        return False
    if key == toggle_record_key:
        macro_record = True
        recorder.start()


with p_keyboard.Listener(on_press=on_press) as listener:
    listener.join()
