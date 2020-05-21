# Final project

# We import the elements that we will need for the server working
import http.server
import http.client
import socketserver
from pathlib import Path
import json
from Seq1 import Seq

# Port
PORT = 8080

# -- This is for preventing the error: "Port already in use"

socketserver.TCPServer.allow_reuse_address = True

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method
        is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print request line
        print(self.requestline)

        # Split request line by space and get the path
        req_line = self.requestline.split(' ')
        path = req_line[1]

        # Split path
        arguments = path.split('?')

        # Action is the first argument
        action = arguments[0]

        # If there is no argument we will receive an error
        contents = Path('error.html').read_text()
        code = 404

        # The main program composed by basic and medium levels starts at this point

        try:

            # First we open index.html if we don´t specify any action or it is /index we will be taken to  the initial
            # menu that returns us the index.html file

            if action == "/" or action == "/index":
                contents = Path('index.html').read_text()

            # Once we are in the initial menu we have different options to perform, basic and medium levels.

            # In the first option we are asked to introduce a limit value, once we have done it the program will take us
            # to an html file in which we can see a list, whose is equal to the limit, of species stored in the ensembl
            # data base

            elif action == "/listSpecies":

                # This is the basic structure of the html page that we will get, it is incomplete...
                contents = f"""<!DOCTYPE html>
                <html lang = "en">
                <head>
                 <meta charset = "utf-8" >
                 <title>List of species in the browser</title >
                </head >
                <body>
                <p>The total number of species in ensembl is: 267</p>"""

                # We get the arguments that go after the ? in the path, Limit = "whatever input we introduce"
                get_value = arguments[1]
                limit_input = get_value.split('?')

                # We have the couple of elements, split by = and get them separated, the value that will be used is
                # limit value

                limit_action, limit_value = limit_input[0].split("=")

                # We try to convert it into an integer to return error page if there is a value error
                limit_value = int(limit_value)

                # Just addition to html response...
                contents += f"""<p>The number of species you selected are: {limit_value} </p>"""

                # We set the main elements that will be used to get the list: ensembl server, endpoint that was
                # previously searched for this function and parameters
                server = 'rest.ensembl.org'
                endpoint = 'info/species'
                parameters = '?content-type=application/json'
                request = endpoint + parameters

                # Connect with the server
                conn = http.client.HTTPConnection(server)

                # Send the request message, using the GET method. We are
                # requesting the main page (/)
                try:
                    conn.request("GET", request)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # Read the response message from the server
                response = conn.getresponse()

                # Read the response's body
                body = response.read().decode()

                # We create blank list where we will store the data received from JSON
                limit_list = []

                # Create a variable with the data, form the JSON received. We get the key that interest us, species.
                body = json.loads(body)
                species = body["species"]

                # First we compare if our input of limit is higher than the available numbre of species. On that case
                # we will be taken to an error page

                if limit_value > len(species):
                    contents = f"""<!DOCTYPE html>
                            <html lang = "en">
                            <head>
                             <meta charset = "utf-8" >
                             <title>ERROR</title >
                            </head>
                            <body>
                            <p>ERROR LIMIT OUT OF RANGE. Introduce a valid limit value</p>
                            <a href="/">Main page</a></body></html>"""

                # In case our input is valid, we iterate through all the species and get the key we are looking for,
                # their names, which appears as display_name. We will introduce them to our blank list; once its length
                # is equal to the limit value we introduce we stop iterating and get the  final list of species

                else:
                    for element in species:
                        limit_list.append(element["display_name"])
                        if len(limit_list) == limit_value:
                            contents += f"""<p>The species are: </p>"""
                            for specie in limit_list:
                                contents += f"""<p> - {specie} </p>"""
                    contents += f"""<a href="/">Main page</a></body></html>"""
                    code = 200

                    # We just add the final info to our html to be given us back, if we get up to here everything has
                    # gone correctly

            # In this option we are asked to introduce the name of a specie of the ensembl data base, the program should
            # give us back a list of the chromosomes of that specie

            elif action == "/karyotype":

                # This is the basic structure of the html page that we will get, it is incomplete...
                contents = f"""<!DOCTYPE html>
                <html lang = "en">
                <head>
                <meta charset = "utf-8">
                <title> Karyotype </title >
                </head >
                <body>
                <h2> The names of the chromosomes are:</h2>"""

                # We get the arguments that go after the ? in the path, Specie = "whatever input we introduce"
                get_value = arguments[1]
                specie_input = get_value.split('?')

                # We have the couple of elements, split by = and get them separated, the value that will be used is
                # specie name
                specie_action, name_sp = specie_input[0].split("=")

                # We set the main elements that will be used to get the list: ensembl server, endpoint that was
                # previously searched for this function and parameters
                server = 'rest.ensembl.org'
                endpoint = 'info/assembly/'
                parameters = '?content-type=application/json'
                request = endpoint + name_sp + parameters

                # Connect with the server
                conn = http.client.HTTPConnection(server)

                # Send the request message, using the GET method. We are
                # requesting the main page (/)
                try:
                    conn.request("GET", request)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # Read the response message from the server
                response = conn.getresponse()

                # Read the response's body
                body = response.read().decode("utf-8")

                # Create a variable with the data, form the JSON received. We get the key that interest us, karyotype.
                body = json.loads(body)
                karyotype_data = body["karyotype"]

                # This key has associated a list with the different chromosomes, we just get them and add to our html
                for chromosome in karyotype_data:
                    contents += f"""<p> - {chromosome} </p>"""

                # We just add an option to return to the index and our html is now completed,if we get up to here
                # everything has gone correctly
                contents += f"""<a href="/">Main page </a></body></html>"""
                code = 200


            elif action == "/chromosomeLength":
                # We get the arguments that go after the ? symbol
                pair = arguments[1]
                # We have a couple of elements, we need the sequence that we previously wrote and the operation to perform
                # that we previously selected
                pairs = pair.split('&')
                specie_name, specie = pairs[0].split("=")
                chromosome_index, chromosome = pairs[1].split("=")
                specie = specie
                contents = f"""<!DOCTYPE html>
                <html lang = "en">
                <head>
                 <meta charset = "utf-8" >
                 <title>ERROR</title >
                </head>
                <body>
                <p>ERROR INVALID VALUE. Introduce an integer value for chromosome</p>
                <a href="/">Main page</a></body></html>"""
                server = 'rest.ensembl.org'
                endpoint = 'info/assembly/'
                parameters = '?content-type=application/json'
                conn = http.client.HTTPConnection(server)
                request = endpoint + specie + parameters
                try:
                    conn.request("GET", request)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()
                # -- Read the response message from the server
                response = conn.getresponse()
                # -- Read the response's body
                body = response.read().decode()
                body = json.loads(body)
                chromosome_data = body["top_level_region"]
                for chromo in chromosome_data:
                    if chromo["name"] == str(chromosome):
                        length = chromo["length"]
                        contents = f"""<!DOCTYPE html><html lang = "en"><head><meta charset = "utf-8" ><title> Length Chromosome</title >
                            </head ><body><h2> The length of the chromosome is: {length}</h2><a href="/"> Main page</a"""
                code = 200
            elif action == "/geneSeq":
                contents= f"""<!DOCTYPE html>
                <html lang = "en">            
                <head>  
                <meta charset = "utf-8"
                <title> Gene Sequence </title>
                </head>"""
                # We get the arguments that go after the ? symbol
                get_value = arguments[1]
                # We get the seq index, after we have a couple of elements, the one which we need is the value of the index
                # position of the sequence
                seq_n = get_value.split('?')
                seq_name, name_seq = seq_n[0].split("=")
                contents += f"""<p> The sequence of gene {name_seq} is:  </p>"""
                server = 'rest.ensembl.org'
                first_endpoint = "xrefs/symbol/homo_sapiens/"
                parameters = '?content-type=application/json'
                first_request = first_endpoint + name_seq + parameters
                conn = http.client.HTTPConnection(server)
                try:
                    conn.request("GET", first_request)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()
                response = conn.getresponse()
                # -- Read the response's body
                body = response.read().decode()
                body = json.loads(body)
                id_gene = body[0]
                id_gene = id_gene["id"]

                second_endpoint = "sequence/id/"
                second_request = second_endpoint + id_gene + parameters
                try:
                    conn.request("GET", second_request)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()
                response2 = conn.getresponse()
                # -- Read the response's body
                body2 = response2.read().decode()
                body2 = json.loads(body2)
                sequence = body2["seq"]
                contents += f"""<p>{sequence}</p><a href="/">Main page</a></body></html>"""
                code = 200
            elif action == "/geneInfo":
                contents = f"""<!DOCTYPE html>
                    <html lang = "en">            
                    <head>  
                    <meta charset = "utf-8"
                    <title> Gene Information</title>
                    </head>"""
                # We get the arguments that go after the ? symbol
                get_value = arguments[1]
                # We get the seq index, after we have a couple of elements, the one which we need is the value of the index
                # position of the sequence
                seq_n = get_value.split('?')
                seq_name, name_seq = seq_n[0].split("=")
                contents += f"""<p> The information of gene {name_seq} is:  </p>"""
                server = 'rest.ensembl.org'
                first_endpoint = "xrefs/symbol/homo_sapiens/"
                parameters = '?content-type=application/json'
                first_request = first_endpoint + name_seq + parameters
                conn = http.client.HTTPConnection(server)
                try:
                    conn.request("GET", first_request)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()
                response = conn.getresponse()
                # -- Read the response's body
                body = response.read().decode()
                body = json.loads(body)
                id_gene = body[0]
                id_gene = id_gene["id"]
                second_endpoint = "lookup/id/"
                second_request = second_endpoint + id_gene + parameters
                try:
                    conn.request("GET", second_request)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()
                response2 = conn.getresponse()
                # -- Read the response's body
                body2 = response2.read().decode()
                body2 = json.loads(body2)
                length = int(body2["end"]) - int(body2["start"])
                contents += f"""<p> The gene starts at: {body2["start"]} </p><p> The gene ends at: {body2["end"]} </p>
                <p> The gene length is: {length}</p>
                <p> The gene id is at: {id_gene} </p> <p> The gene is on chromosome: {body2["seq_region_name"]} </p>
                <a href="/">Main page</a></body></html>"""
                code = 200
            elif action == "/geneCalc":
                contents = f"""<!DOCTYPE html>
                        <html lang = "en">            
                        <head>  
                        <meta charset = "utf-8"
                        <title> Gene Calculations</title>
                        </head>"""
                # We get the arguments that go after the ? symbol
                get_value = arguments[1]
                # We get the seq index, after we have a couple of elements, the one which we need is the value of the index
                # position of the sequence
                seq_n = get_value.split('?')
                seq_name, name_seq = seq_n[0].split("=")
                server = 'rest.ensembl.org'
                first_endpoint = "xrefs/symbol/homo_sapiens/"
                parameters = '?content-type=application/json'
                first_request = first_endpoint + name_seq + parameters
                conn = http.client.HTTPConnection(server)
                try:
                    conn.request("GET", first_request)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()
                response = conn.getresponse()
                # -- Read the response's body
                body = response.read().decode()
                body = json.loads(body)
                id_gene = body[0]
                id_gene = id_gene["id"]
                second_endpoint = "sequence/id/"
                second_request = second_endpoint + id_gene + parameters
                try:
                    conn.request("GET", second_request)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()
                response2 = conn.getresponse()
                # -- Read the response's body
                body2 = response2.read().decode()
                body2 = json.loads(body2)
                sequence = Seq(body2["seq"])
                contents += f"""<p> The length of gene {name_seq} is: {sequence.len()} </p>"""
                list_of_bases = ["A", "C", "G", "T"]
                for base in list_of_bases:
                    perc_base = round(sequence.count_base(base) * 100 / sequence.len(),2)
                    contents += f"""<p> {base} : {sequence.count_base(base)} ({perc_base}%) </p>"""
                contents += f"""<a href="/">Main page</a></body></html>"""
                code = 200

            elif action == "/geneList":
                contents = f"""<!DOCTYPE html>
                  <html lang = "en">            
                  <head>  
                  <meta charset = "utf-8"
                  <title> Gene List</title>
                  </head>"""
                endpoint = "overlap/region/human/"
                get_value = arguments[1]
                # We get the seq index, after we have a couple of elements, the one which we need is the value of the index
                # position of the sequence
                pairs = get_value.split('&')
                chromo_value, chromo = pairs[0].split("=")
                chromosome_start, start = pairs[1].split("=")
                chromosome_end, end = pairs[2].split("=")
                contents += f"""<p> List of genes of the chromosome {chromo}, which goes from {start} to {end} </p>"""
                server = 'rest.ensembl.org'
                parameters = '?feature=gene;content-type=application/json'
                request = endpoint + chromo + ":" + start + "-" + end + parameters

                conn = http.client.HTTPConnection(server)
                try:
                    conn.request("GET", request)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()
                response = conn.getresponse()
                # -- Read the response's body
                body = response.read().decode("utf-8")
                body = json.loads(body)
                for element in body:
                    print(element["external_name"])
                    contents += f"""<p>{element["external_name"]}</p>"""
                contents += f"""<a href="/">Main page</a></body></html>"""
                code = 200





#97321915  97319271

        except (KeyError,ValueError,IndexError,TypeError):
            contents = Path('error.html').read_text()


        # Generating the response message
        self.send_response(code)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()