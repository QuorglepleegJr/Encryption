import socket

from random import randrange

from DHKEA import generate_key, power_mod

class Server:

    def __init__(self, HOST, PORT):

        self.HOST = HOST
        self.PORT = PORT

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.HOST, self.PORT))
    
    def get_ip(self):

        return self.HOST
    
    def get_port(self):

        return self.HOST
    
    def run(self):

        while True:

            try:

                self.s.listen(1)
                conn, addr = self.s.accept()
                Server.handle_client(conn, addr)
            
            except KeyboardInterrupt:

                print("\nShutting down server")
                break

    def handle_client(connection, address):

        print("Handling client at", address)

        while True:

            data = connection.recv(1024)

            if not data: break

            data = data.decode("utf-8")

            print("Received from", address, ":", data)

            if data == "Awaiting handshake":

                print("Handshake with", address, "completed")

                connection.sendall("Handshake accepted".encode("utf-8"))

            elif len(data) > 9 and data[:9] == "KeyData: ":

                print("Processing as keydata")
                
                _, B, p, min = data.split(" ")

                a = randrange(int(min), int(p))

                send_A = lambda A: connection.send(int.to_bytes(A, 1024, 'big'))
                get_B = lambda: int(B)

                print("Key:", generate_key(a, int(p), get_B, send_A))
            
            else:

                connection.sendall(data)
    
    def __del__(self):

        try:
            self.s.close()
        except Exception:
            pass