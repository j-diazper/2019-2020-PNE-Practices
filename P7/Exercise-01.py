import http.client
import json
server = 'rest.ensembl.org'
endpoint = '/info/ping'
params = '?content-type=application/json'
url = server + endpoint + params
print()
print(f"Server: {server}")
print(f"URL: {url}")
# Connect with the server
conn = http.client.HTTPConnection(server)

try:
    conn.request("GET", endpoint + params)

except ConnectionRefusedError:
    print("ERROR! Can´t connect")
    exit()
# Get response from the server
response = conn.getresponse()
# Status line
print(f"Response received!: {response.status} {response.reason}\n")
# Read the body of response, we will use it in json form
body = response.read().decode()
response = json.loads(body)
ping = response['ping']
if ping == 1:
    print("PING OK! The database is running!")