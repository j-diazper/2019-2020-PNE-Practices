import http.client
import json
from Seq1 import Seq

gene_dict = {'FRAT1': 'ENSG00000165879', 'ADA': 'ENSG00000196839', 'FXN': 'ENSG00000165060', 'RNU6_269P': 'ENSG00000212379',
'MIR633': 'ENSG00000207552', 'TTTY4C': 'ENSG00000228296', 'RBMY2YP': 'ENSG00000227633', 'FGFR3': 'ENSG00000068078',
'KDR': 'ENSG00000128052', 'ANK2': 'ENSG00000145362'}
base_list = ['A', 'T', 'C', 'G']

server = 'rest.ensembl.org'
endpoint = '/sequence/id/'
parameters = '?content-type=application/json'

# We ask to introduce a gene´s name
name = input("Write the gene name: ")
url = server + endpoint + gene_dict[name] + parameters
print("Server:", server)
print("URL: ", url)

# Connect with the server
conn = http.client.HTTPConnection(server)
request = endpoint + gene_dict[name] + parameters
try:
    conn.request("GET", request)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
response = conn.getresponse()

# -- Print the status line
print("Response received!:", response.status, response.reason,"\n")

# -- Read the response's body
body = response.read().decode()

# -- Create a variable with the data,
# -- form the JSON received
gene = json.loads(body)

print("Gene", end="")
print(":", name)
print("Description", end="")
print(":", gene['desc'])

body = gene['seq']

# We use class Seq for using its functions
seq = Seq(body)
length = seq.len()
counter_a = seq.count_base('A')
counter_g = seq.count_base('G')
counter_c = seq.count_base('C')
counter_t = seq.count_base('T')
perc_a = round(100 * counter_a / length,1)
perc_g = round(100 * counter_g / length,1)
perc_c = round(100 * counter_c / length,1)
perc_t = round(100 * counter_t / length,1)
print(f"""Total length: {length} ç
A: {counter_a} ({perc_a}%)
G: {counter_g} ({perc_g}%)
C: {counter_c} ({perc_c}%)
T: {counter_t} ({perc_t}%)""")

# -- Dictionary with the values
dic = seq.count(base_list)

# -- Create a list with all the values
value_list = list(dic.values())

# -- Calculate the maximum
maximum = max(value_list)

# -- Print the base
print("Most frequent Base", end="")
print(": ",base_list[value_list.index(maximum)])
