#!/usr/bin/env python
from signal import pause
from time import sleep
from gpiozero import LED, Button
from evdev import uinput, ecodes as e

# Pinout
# =================
# Left    | Right
# =================
# 3.3 VDC | 5.0 VDC
# GPIO 2  | 5.0 VDC
# GPIO 3  | Ground
# GPIO 4  | GPIO 14
# Ground  | GPIO 15
# GPIO 17 | GPIO 18
# GPIO 27 | Ground
# GPIO 22 | GPIO 23
# 3VDC2   | GPIO 24
# GPIO 10 | Ground
# GPIO 9  | GPIO 25
# GPIO 11 | GPIO 8
# Ground  | GPIO 7
# GPIO 0  | GPIO 1
# GPIO 5  | Ground
# GPIO 6  | GPIO 12
# GPIO 13 | Ground
# GPIO 19 | GPIO 16
# GPIO 26 | GPIO 20
# Ground  | GPIO 21
# =================

led1 = LED(27)
led1.off()

buttons = [{
	"button": Button(2),
	"key": e.KEY_LEFT
}, {
	"button": Button(22),
	"key": e.KEY_DOWN
}, {
	"button": Button(4),
	"key": e.KEY_UP
}, {
	"button": Button(17),
	"key": e.KEY_RIGHT
}, {
	"button": Button(10),
	"key": e.KEY_ENTER
}, {
	"button": Button(9),
	"key": e.KEY_ESC
}]

ui = uinput.UInput()

def make_press(key, val):
	def do_press():
		led1.toggle()
		ui.write(e.EV_KEY, key, val)
		ui.syn()
	return do_press

try:
	for button_conf in buttons:
		button_conf["button"].when_pressed = make_press(button_conf["key"], 1)
		button_conf["button"].when_released = make_press(button_conf["key"], 0)
	pause()
finally:
	ui.close()
	pass
