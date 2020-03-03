import socket
#$ printf "Test1..." | nc 212.128.253.170 8080
#$ printf "Test2..." | nc 212.128.253.170 8080
#$ printf "Test3..." | nc 212.128.253.170 8080
#$ printf "Test4..." | nc 212.128.253.170 8080
#$ printf "Test5..." | nc 212.128.253.170 8080


# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.253.170"
Connection_counter=0
listCONNECTION = []

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

        element_listCONNECTION = client_ip_port
        listCONNECTION.append(element_listCONNECTION)

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:
        Connection_counter+=1
        print("CONNECTION ",Connection_counter,"Client IP, PORT:(",client_ip_port,")")
        element_listCONNECTION= client_ip_port


        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()

        # -- Print the received message
        print(f"Message received: {msg}")

        # -- Send a response message to the client
        response = f"ECHO: {msg}"

        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the data socket
        cs.close()
        if Connection_counter==5:
            print("The following clients have connected to the server: ")
            for i in listCONNECTION:
                print("CONECCTION",listCONNECTION.index(i),": ",i)

