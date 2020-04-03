from Client0 import Client
import termcolor
PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.253.170"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
# -- Send a message to the server
print("Sending a message to the server...")
response1 = "Message 1:..."
response2= "Message 2: Testing!!!"
response_list=[response1,response2]
for i in response_list:
    print("To server: ",response1,"\n","From server: ",c.debug_talk(i))

