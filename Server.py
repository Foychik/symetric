import socket

sock = socket.socket()

sock.bind(('', 9090))
print("Запуск сервера...")

sock.listen(1)
print("Начало прослушивания порта...")

while True:

    conn, addr = sock.accept()
    print("Подключился клиент: ", addr)

    print("Введите секретное число b: ")
    b = int(input())
    print("Начало передачи данных...")
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
    print("Сообщение от клиента:", msg)
    print("Конец передачи данных...")
    print("Начало отправки данных...")
    conn.send(str(B).encode())
    print("Конец отправки данных...")
    conn.close()
    print("Клиент отключился")
    print("Введите <<exit>> для выхода")
    work_case = input()
    if work_case == "exit":
        break
print("Сервер остановлен...")
