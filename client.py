import socket
import time
import threading

print("Welcome To The Chat!")
print("Please Wait...")
time.sleep(1)

server = socket.socket()
SHOST = socket.gethostname()
IP = socket.gethostbyname(SHOST)
print(f"Hostname Is: {SHOST} With The IP Address: {IP}")
HOST = input(str("Please Enter The Server IP Address: "))
username = input(str("Please Enter Your Username: "))
PORT = 55555
print(f"Attempting To Connect To Server With IP Address: {HOST} On Port: {PORT}...")
time.sleep(1)
server.connect((HOST, PORT))
print("Connected Sucessfully!")

server.send(username.encode())
s_name = server.recv(1024)
s_name = s_name.decode()
print(f"{s_name} Has Joined The Channel!\nType [E] To Exit The Channel")

while True :
  message = server.recv(1024)
  message = message.decode()
  print(f"{s_name} : {message}")
  message = input(str("Me: "))
  if message == "[E]" :
    message = "Left The Channel!"
    server.send(message.encode())
    print("\n")
    break
  server.send(message.encode())
