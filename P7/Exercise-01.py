import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
PARAMETERS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMETERS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")


conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + PARAMETERS)

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()


response = conn.getresponse()


print(f"Response received!: {response.status} {response.reason}\n")


data1 = response.read().decode()


response = json.loads(data1)

ping = response['ping']

if ping == 1:
    print("PING OK! The database is running!")