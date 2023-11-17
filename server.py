import socket

from random import randrange

from DHKEA import generate_key

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

            if data == "Awaiting handshake":

                connection.sendall("Handshake accepted")

            elif len(data) > 9 and data[:9] == "KeyData: ":
                
                _, B, p, min = data.split(" ")

                a = randrange(min, p)

                send_A = connection.sendall
                get_B = lambda: B

                print("Key:", generate_key(a, p, send_A, get_B))
            
            else:

                connection.sendall(data)
    
    def __del__(self):

        try:
            self.s.close()
        except Exception:
            pass