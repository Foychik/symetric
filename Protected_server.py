import socket
from Symmetry_code import decrypt, encrypt
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
while True:

    conn, addr = sock.accept()
    print("Подключился клиент: ", addr)

    print("Введите секретное число b: ")
    b = int(input())
    data = conn.recv(1024)
    msg = data.decode()
    msg = msg.split()
    msg = list(map(int, msg))
    g = msg[0]
    p = msg[1]
    A = msg[2]
    B = g ** b % p
    K = A ** b % p
    print("KEY:", K)
    conn.send(str(B).encode())
    while True:
        data = conn.recv(1024)
        msg = data.decode()
        msg = decrypt(msg, B)
        msg = decrypt(msg, K)
        print(msg)
        print("Введите сообщение или exit для выхода: ")
        msg = input()
        if msg == "exit":
            break
        msg = encrypt(msg, K)
        msg = encrypt(msg, B)
        conn.send(msg.encode())






    conn.close()
    print("Введите <<exit>> для выхода")
    work_case = input()
    if work_case == "exit":
        break
print("Сервер остановлен...")
