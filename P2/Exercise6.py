from Client0 import Client
from pathlib import Path

def dividing_seq(FILENAME):
    bodystr=""
    new_list= []
    total_list=[]
    file_contents = Path(FILENAME).read_text()
    lines = file_contents.split("\n")
    body = lines[1:]
    bodystr=bodystr.join(body).replace(",","")
    for i in bodystr:
        new_list.append(i)
        if len(new_list)==10:
            total_list.append(new_list)
            continue
    return total_list

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.253.170"
PORT = 8089

# -- Create a client object
c = Client(IP, PORT)
#Reading text

FILENAME = "FRAT1.txt"




# -- Send a message to the server
print("Sending a message to the server...")
response1 = "Sending gene U5"
response2= dividing_seq(FILENAME)
response_list=[response1,response2]
for i in response_list:
    print("To server: ",response1,"\n","From server: ",c.debug_talk(i))