import socket

HOST = ''
PORT = 60000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST, PORT))

    print("Established, listening for connection on port", PORT)

    while True:

        try:

            s.listen(1)
            connection, address = s.accept()
            
            with connection:

                print("Connected to by", address)
                
                while True:

                    data = connection.recv(1024)
                    
                    if not data: break

                    print("Recieved '" + data.decode("utf-8") + "' from", address)

                    connection.sendall(data)
                
                print(address, "disconnected, listening for new connection on port", PORT)
        
        except KeyboardInterrupt:

            print("\nShutting down server")
            break
