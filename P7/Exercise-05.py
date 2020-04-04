import http.client
import json
from Seq1 import Seq


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

BASES = ['A', 'T', 'C', 'G']

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
PARAMETERS = '?content-type=application/json'

# -- List for storing the A percentages
list_A = []

# -- Repeat the process for all the genes
for name in GENES:

    REQ = ENDPOINT + GENES[name] + PARAMETERS
    URL = SERVER + REQ

    print()
    print(f"Server: {SERVER}")
    print(f"URL: {URL}")

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

print("Gene", end="")
print(":", name)
print("Description", end="")
print(":", gene['desc'])

genestr = gene['seq']

# -- Create the object sequence from the string
s = Seq(genestr)

sl = s.len()
ca = s.count_base('A')
pa = "{:.1f}".format(100 * ca / sl)
cc = s.count_base('C')
pc = "{:.1f}".format(100 * cc / sl)
cg = s.count_base('G')
pg = "{:.1f}".format(100 * cg / sl)
ct = s.count_base('T')
pt = "{:.1f}".format(100 * ct / sl)

print("Total lengh", end="")
print(":", sl)

print("A", end="")
print(":", ca, pa,"%")
print("C", end="")
print(":", cc, pc,"%")
print("G", end="")
print(":", cg, pg,"%")
print("T", end="")
print(":", ct, pt, "%")

# -- Dictionary with the values
d = s.count(BASES)

# -- Create a list with all the values
ll = list(d.values())

# -- Calculate the maximum
m = max(ll)

# -- Print the base
print("Most frequent Base", end="")
print(f": {BASES[ll.index(m)]}")
