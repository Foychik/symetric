import socket
from Symmetry_code import decrypt, encrypt

sock = socket.socket()

sock.connect(('localhost', 9090))

print("Введите число g: ")
g = int(input())
print("Введите число p: ")
p = int(input())
print("Введите секретное число a: ")
a = int(input())
A = g ** a % p
msg = str(g) + " " + str(p) + " " + str(A)
sock.send(msg.encode())
K = ""
data = sock.recv(1024)
K = int(data.decode()) ** a % p
print("KEY:", K)
B = int(data.decode())
while True:
    print("Введите сообщение или exit для выхода: ")
    msg = input()
    if msg == "exit":
        break
    msg = encrypt(msg, K)
    msg = encrypt(msg, B)
    sock.send(msg.encode())

    data = sock.recv(1024)
    msg = data.decode()
    msg = decrypt(msg, B)
    msg = decrypt(msg, K)
    print(msg)

sock.close()
print("Разрыв соединения с сервером")
