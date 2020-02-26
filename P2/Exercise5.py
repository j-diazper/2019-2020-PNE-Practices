from Client0 import Client

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.253.170"
PORT = 8089

# -- Create a client object
c = Client(IP, PORT)
#Reading text
from pathlib import Path
FILENAME = "U5.txt"
file_contents = Path(FILENAME).read_text()
lines= file_contents.split("\n")
body=lines[1:]
bodystr= " "
bodystr= bodystr.join(body)


# -- Send a message to the server
print("Sending a message to the server...")
response1 = "Sending gene U5"
response2= bodystr
response_list=[response1,response2]
for i in response_list:
    print("To server: ",response1,"\n","From server: ",c.debug_talk(i))