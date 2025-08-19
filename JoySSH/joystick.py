import pygame

def init_joystick():
    pygame.init()
    pygame.joystick.init()
    
    if pygame.joystick.get_count() == 0:
        print("Aucune manette detectee")
        return None

    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Manette détecte : {joystick.get_name()}")
    return joystick

def read_joystick(joystick):
    pygame.event.pump()  

    # Lire les joysticks (axes)
    left_x = joystick.get_axis(0)  # Stick gauche (axe X)
    left_y = joystick.get_axis(1)  # Stick gauche (axe Y)
    right_x = joystick.get_axis(2) # Stick droit (axe X)
    right_y = joystick.get_axis(3) # Stick droit (axe Y)

    # Lire les boutons
    buttons = {i: joystick.get_button(i) for i in range(joystick.get_numbuttons())}

    # Lire les gâchettes
    lt = joystick.get_axis(4)  # Gâchette gauche
    rt = joystick.get_axis(5)  # Gâchette droite

    return left_x, left_y, right_x, right_y, lt, rt, buttons[0], buttons[1], buttons[2], buttons[3]

#A -> active accel
#B -> desactive accel
#X -> active volant
#Y -> desactive volant