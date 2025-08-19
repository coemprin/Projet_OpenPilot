import paramiko
import time
from joystick import *

joystick = init_joystick()

COMMA_IP = "192.168.149.132" 
USERNAME = "comma"
#PASSWORD = ""  

#Generate a key with : ssh-keygen -t rsa -b 4096 -C "firstname.familyname@michelin.com"
#ADD it into GITHUB as Authentification #THIS MUST BE YOUR ONLY KET (I make it work like that)

#Put the path of private key here:
PRIVATE_KEY_PATH = "C:/Users/E119141/.ssh/id_rsa"

key = paramiko.RSAKey.from_private_key_file(PRIVATE_KEY_PATH)
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#client.connect(COMMA_IP, username=USERNAME, password=PASSWORD)
client.connect(COMMA_IP, username=USERNAME, pkey=key)

channel = client.invoke_shell()

channel.send("python3 /data/openpilot/selfdrive/controls/receiver.py\n") #déclencehement du script receiver.py
time.sleep(1)  

if joystick != None :
    try:
        while True:

            left_x, left_y, right_x, right_y, lt, rt, A, B, X, Y = read_joystick(joystick)
            command = f"{left_x:.2f} {left_y:.2f} {right_x:.2f} {right_y:.2f} {lt:.2f} {rt:.2f} {A} {B} {X} {Y}"
            channel.send(command + "\n")
            
            time.sleep(0.01)
            
            output = channel.recv(1024).decode('utf-8')
            print("\nRéponse du comma:\n", output, " \nFIN DE LA REPONSE\n")

    except KeyboardInterrupt:
        print("\nArrêt du programme.")
        channel.send("STOP\n") 
        time.sleep(1)
        output = channel.recv(1024).decode('utf-8')
        print("Réponse du comma:", output)
        client.close()

#commande pour se connecter au comma en ssh -> ssh comma@<adresse IP> 
#Adresse IP à trouver dans les parametres avancees du reseau sur le comma
