from Client0 import Client
from termcolor import colored
# -- Parameters of the server to talk to
IP = "212.128.253.170"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
counter=0

while True:
    msg= f"Message {counter}"
    msgtoserver= colored(msg,"blue")
    print("To server: ",msgtoserver)
    msgfromserver= colored(msg,"green")
    response= c.debug_talk(msgfromserver)
    print(f"From server: {response}")
    counter+=1
    if counter==5:
        break