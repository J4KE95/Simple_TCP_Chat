import socket
import time
import threading

print("Welcome To The Channel!")
print("Server Is Now Initialising...")
time.sleep(1)

server = socket.socket()
HOST = socket.gethostname()
IP = socket.gethostbyname(HOST)
PORT = 55555

server.bind((HOST, PORT))
print(f"Now Serving On {HOST} With The IP {IP} And The Port {PORT}")
username = input("Enter Server Username: ")

server.listen(1)
print("Waiting For Incoming Connections...")
conn, addr = server.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(f"{s_name} Has Connected!\nType [E] To Exit The Channel")
conn.send(username.encode())

while True :
  message = input(str("Me: "))
  if message == "[E]" :
    message = "Left The Channel!"
    conn.send(message.encode())
    print("\n")
    break
  conn.send(message.encode())
  message = conn.recv(1024)
  message = message.decode()
  print(f"{s_name} : {message}")