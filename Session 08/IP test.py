IP ="212.128.253.170"
Ping_self = """PING 212.128.253.170 (212.128.253.170) 56(84) bytes of data.
64 bytes from 212.128.253.170: icmp_seq=1 ttl=64 time=0.056 ms
64 bytes from 212.128.253.170: icmp_seq=2 ttl=64 time=0.050 ms
64 bytes from 212.128.253.170: icmp_seq=3 ttl=64 time=0.064 ms
64 bytes from 212.128.253.170: icmp_seq=4 ttl=64 time=0.063 ms"""

Ping_8_8_8_8 = """PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=55 time=3.94 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=55 time=3.93 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=55 time=4.14 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=55 time=3.97 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=55 time=3.94 ms
64 bytes from 8.8.8.8: icmp_seq=6 ttl=55 time=4.28 ms
64 bytes from 8.8.8.8: icmp_seq=7 ttl=55 time=3.94 ms"""
Ping_URJC ="""PING urjc.es (192.168.46.45) 56(84) bytes of data.
64 bytes from cuadrado.urjc.es (192.168.46.45): icmp_seq=1 ttl=126 time=2.32 ms
64 bytes from cuadrado.urjc.es (192.168.46.45): icmp_seq=2 ttl=126 time=2.52 ms
64 bytes from cuadrado.urjc.es (192.168.46.45): icmp_seq=3 ttl=126 time=2.33 ms
64 bytes from cuadrado.urjc.es (192.168.46.45): icmp_seq=4 ttl=126 time=3.37 ms"""
import socket

# Configure the Server's IP and PORT
PORT = 6855
IP = "212.128.253.170"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection!e
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(msg))

        # Send the messag
        message = "Hello from the teacher's server"
        send_bytes = str.encode(message)
        # We must write bytes, not a string
        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()