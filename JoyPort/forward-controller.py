import json
import socket

import pygame

pygame.init()
pygame.joystick.init()
js = pygame.joystick.Joystick(0)
js.init()

s = socket.socket()
s.connect(("localhost", 8002))

while True:
    pygame.event.pump()
    data = {"axes": [js.get_axis(i) for i in range(js.get_numaxes())], "buttons": [js.get_button(i) for i in range(js.get_numbuttons())]}
    s.sendall((json.dumps(data) + "\n").encode())
