from Client0 import Client
from pathlib import Path

def dividing_seq(FILENAME):
    bodystr=""
    file_contents = Path(FILENAME).read_text()
    lines = file_contents.split("\n")
    body = lines[1:]
    bodystr=bodystr.join(body).replace(",","")
    split_strings = []
    n = 10
    for index in range(0, len(bodystr), n):
        split_strings.append(bodystr[index: index + n])
    return bodystr,split_strings


PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.253.170"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
#Reading text

FILENAME = "FRAT1.txt"




# -- Send a message to the server
print("Sending a message to the server...")
response1 = "NULL Seq created"
response2= dividing_seq(FILENAME)[0]
print("From server: ", c.debug_talk(response1))
print("From server: ", c.debug_talk(response2))
for i in dividing_seq(FILENAME)[1]:
    print("From server: ",c.debug_talk(i))
    if dividing_seq(FILENAME)[1].index(i)>3:
        break