import http.client
import json
import termcolor

GENES = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362',
}

GENENAME = 'MIR633'
SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
PARAMS = '?content-type=application/json'
REQ = ENDPOINT + GENES[GENENAME] + PARAMS
URL = SERVER + REQ

print()
print("Server:", SERVER)
print("URL:", URL)

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", REQ)

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!:", r1.status, r1.reason,"\n")

# -- Read the response's body
data1 = r1.read().decode()

# -- Create a variable with the data,
# -- form the JSON received
gene = json.loads(data1)

termcolor.cprint("Gene", 'green', end="")
print(":", GENENAME)
print("Description", end="")
print(":", gene['desc'])
print("Bases", end="")
print(":", gene['seq'])