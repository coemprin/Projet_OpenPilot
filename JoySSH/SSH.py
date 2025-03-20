import paramiko
import time
from joystick import *

joystick = init_joystick()

COMMA_IP = "192.168.176.132" 
USERNAME = "comma"
PASSWORD = ""  

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(COMMA_IP, username=USERNAME, password=PASSWORD)

channel = client.invoke_shell()

channel.send("python3 /data/openpilot/selfdrive/controls/receiver.py\n")
time.sleep(1)  

if joystick != None :
    try:
        while True:

            left_x, left_y, right_x, right_y, lt, rt = read_joystick(joystick)
            command = f"{left_x:.2f} {left_y:.2f} {right_x:.2f} {right_y:.2f} {lt:.2f} {rt:.2f}"
            channel.send(command + "\n")
            
            time.sleep(0.01)
            
            output = channel.recv(1024).decode('utf-8')
            print("Réponse du comma:", output)

    except KeyboardInterrupt:
        print("\nArrêt du programme.")
        channel.send("STOP\n") 
        time.sleep(1)
        output = channel.recv(1024).decode('utf-8')
        print("Réponse du comma:", output)
        client.close()

#commande pour se connecter au comma en ssh -> ssh comma@<adresse IP> 
#Adresse IP à trouver dans les parametres avancees du reseau sur le comma
