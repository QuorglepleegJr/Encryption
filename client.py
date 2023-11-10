import socket

HOST = '127.0.0.1'
PORT = 60000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))

    s.sendall(b'Hello world!')

    data = s.recv(1024)

    while data:

        print("Received '" + data.decode("utf-8").strip() + "'")

        s.sendall(bytes(input(), "utf-8"))

        data = s.recv(1024)