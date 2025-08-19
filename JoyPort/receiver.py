import json
import socket

s = socket.socket()

print("Waiting for connection from controller...")
s.bind(("localhost", 8002))
s.listen(1)
conn, _ = s.accept()
print("Connected to the controller")

while True:
    line = conn.recv(4096)
    if not line:
        break
    try:
        data = json.loads(line)

        for i, button in enumerate(data["buttons"]):
            if button == 1:
                print(f"Button {i} pressed")

    except json.JSONDecodeError:
        continue
