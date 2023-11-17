import socket

from random import randrange

from DHKEA import generate_key

class Client:

    def from_server(server):

        return Client(server.get_ip, server.get_port)

    def __init__(self, HOST, PORT):

        self.HOST = HOST
        self.PORT = PORT

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.s.connect((self.HOST, self.PORT))

        self.confirm_handshake()

    def confirm_handshake(self, timeout=2):

        old_time_out = self.s.timeout

        self.s.settimeout(timeout)
    
        self.s.sendall("Awaiting handshake")

        d = self.s.recv(1024)

        if d != "Handshake accepted":

            raise ValueError("Server did not accept handshake")

    def key_exchange(self, min = 2**31, max = 2**32):

        p = randrange(min, max)
        a = randrange(min-(max-p), p)

        send_A = lambda A: self.s.sendall(" ".join("KeyData:", str(A), str(p), str(min-(max-p))))
        get_B = lambda: int.from_bytes(self.s.recv(1024))

        return generate_key(a, p, send_A, get_B)