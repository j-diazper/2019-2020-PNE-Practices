import http.client
import json

server = 'rest.ensembl.org'
endpoint = '/sequence/id/'
params = '?content-type=application/json'

gene_list = {'FRAT1': 'ENSG00000165879', 'ADA': 'ENSG00000196839', 'FXN': 'ENSG00000165060', 'RNU6_269P': 'ENSG00000212379',
'MIR633': 'ENSG00000207552', 'TTTY4C': 'ENSG00000228296', 'RBMY2YP': 'ENSG00000227633', 'FGFR3': 'ENSG00000068078',
'KDR': 'ENSG00000128052', 'ANK2': 'ENSG00000145362'}

name = 'MIR633'
url = server + endpoint + gene_list[name] + params
print("Server:", server)
print("URL:", url)

# Connect with the server
conn = http.client.HTTPConnection(server)
request = endpoint + gene_list[name] + params
try:
    conn.request("GET", request)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
response = conn.getresponse()

#status line
print("Response received!:", response.status, response.reason,"\n")

# Read the body of response, we will use it in json form
body = response.read().decode()
# We create the dict with the gene info
gene = json.loads(body)
print("Gene", end="")
print(":", name)
print("Description", end="")
print(":", gene['desc'])
print("Bases", end="")
print(":", gene['seq'])