import http.client
import json
from Seq1 import Seq


gene_list = {'FRAT1': 'ENSG00000165879', 'ADA': 'ENSG00000196839', 'FXN': 'ENSG00000165060', 'RNU6_269P': 'ENSG00000212379',
'MIR633': 'ENSG00000207552', 'TTTY4C': 'ENSG00000228296', 'RBMY2YP': 'ENSG00000227633', 'FGFR3': 'ENSG00000068078',
'KDR': 'ENSG00000128052', 'ANK2': 'ENSG00000145362'}

base_list = ['A', 'T', 'C', 'G']

server = 'rest.ensembl.org'
endpoint = '/sequence/id/'
parameters = '?content-type=application/json'

# -- List for storing the A percentages


# -- Repeat the process for all the genes
for name in gene_list:

    url = server + endpoint + gene_list[name] + parameters

    print()
    print(f"Server: {server}")
    print(f"URL: {url}")

    # Connect with the server
    conn = http.client.HTTPConnection(server)
    request = endpoint + gene_list[name] + parameters

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

    # -- Create the object sequence from the string
    # We use class Seq for using its functions
    seq = Seq(body)
    length = seq.len()
    counter_a = seq.count_base('A')
    counter_g = seq.count_base('G')
    counter_c = seq.count_base('C')
    counter_t = seq.count_base('T')
    perc_a = 100 * counter_a / length
    perc_g = 100 * counter_g / length
    perc_c = 100 * counter_c / length
    perc_t = 100 * counter_t / length

    print("Total lengh", end="")
    print(":", length)

    print("A", end="")
    print(":", counter_a, perc_a,"%")
    print("C", end="")
    print(":", counter_c, perc_c,"%")
    print("G", end="")
    print(":", counter_g, perc_g,"%")
    print("T", end="")
    print(":", counter_t, perc_t, "%")

    # -- Dictionary with the values
    dic = seq.count(base_list)

    # -- Create a list with all the values
    value_list = list(dic.values())

    # -- Calculate the maximum
    maximum = max(value_list)

    # -- Print the base
    print("Most frequent Base", end="")
    print(f": {base_list[value_list.index(maximum)]}")
