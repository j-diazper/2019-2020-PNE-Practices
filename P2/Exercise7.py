

from Client0 import Client
from pathlib import Path

def dividing_seq(FILENAME):
    bodystr=""
    file_contents = Path(FILENAME).read_text()
    lines = file_contents.split("\n")
    body = lines[1:]
    bodystr=bodystr.join(body).replace(",","")
    split_strings = []
    n = 9
    for index in range(0, len(bodystr), n):
        split_strings.append(bodystr[index: index + n])
    return bodystr,split_strings


PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.253.170"
PORT1 = 8080
PORT2=8089
PORT_list=[]
PORT_list.append(PORT1)
PORT_list.append(PORT2)
# -- Create a client object
c1 = Client(IP, PORT1)
c2= Client(IP,PORT2)

#Reading text

FILENAME = "FRAT1.txt"
#Even and odd lists
EVEN_list=[]
ODD_list= []
for i in dividing_seq(FILENAME)[1]:
    if dividing_seq(FILENAME)[1].index(i)%2==0:
        EVEN_list.append(i)
    else:
        ODD_list.append(i)



# -- Send a message to the server
print("Sending a message to the server...")
response = "NULL Seq created"
print("From server: ", c1.debug_talk(response))
print("From server: ", c2.debug_talk(response))
for i in EVEN_list:
    print("From server: ",c1.debug_talk(i))
    if EVEN_list.index(i)==4:
        break
for i in ODD_list:
    print("From server: ",c2.debug_talk(i))
    if ODD_list.index(i)==4:
        break