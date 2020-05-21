import http.client
import json

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", "/listusers")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
people = json.loads(data1)
print("CONTENT: ")
print()
print("Name: ", end="")
print(people['Firstname'], people['Lastname'])
print("Age: ", end="")
print(people['age'])
phoneNumbers = people['phoneNumber']
print("Phone numbers: ", end='')
print(len(phoneNumbers))
for i, num in enumerate(phoneNumbers):
    print("  Phone {}:".format(i))
    print("    Type: ", end='')
    print(num['type'])
    print("    Number: ", end='')
    print(num['number'])