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

                    # We just add the final info to our html to be given us back, if we got here everything has
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

                # We just add an option to return to the index and our html is now completed,if we got here
                # everything has gone correctly
                contents += f"""<a href="/">Main page </a></body></html>"""
                code = 200

            # In this option we are asked to introduce the name of a specie of the ensembl data base and the name of one
            # of its chromosomes, the program should give us back the length of the chromosome

            elif action == "/chromosomeLength":

                # We get the arguments that go after the ? in the path, Specie = "whatever input we introduce" and
                # Chromosome = "whatever input we introduce"
                pair = arguments[1]
                pairs = pair.split('&')

                # We have two couple of elements, split each by =. The values that will be used are specie and
                # chromosome that we introduced
                specie_name, specie = pairs[0].split("=")
                chromosome_index, chromosome = pairs[1].split("=")
                specie = specie

                # We set the main elements that will be used to get the list: ensembl server, endpoint that was
                # previously searched for this function and parameters
                server = 'rest.ensembl.org'
                endpoint = f'info/assembly/'
                parameters = '?content-type=application/json'
                request = endpoint + specie + parameters

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

                # Create a variable with the data, form the JSON received. We get the key that interest us, chromosomic
                # data
                chromosomic_data = json.loads(body)

                # As it was researched at the Api of ensembl this will give us a superdictionary, we are looking for
                # specific elements that are inside key top_level_region, we will iterate through
                for chromo in chromosomic_data["top_level_region"]:

                    # The "sub"key we are looking for is name, we compare with the chromosome we introduced and if we
                    # get a coincidence we will get the value of key length of that specific chromosome
                        if chromosome == chromo["name"]:

                            # Once we have the value we will directly create the html with the info, the aim of this is
                            # to deal with possible errors in an easy way
                            length = chromo["length"]
                            contents = f"""<!DOCTYPE html><html lang = "en">
                            <head>
                            <meta charset = "utf-8" >
                            <title> Length Chromosome</title >
                            </head>
                            <body>
                            <h2> Chromosome length</h2>
                            <meta charset = "utf-8" >
                            <title> Chromosome length </title >
                            <p>The lenght of the chromosome {chromosome} from {specie} is : </p>
                            <p> {length}</p>
                            <a href="/">Main page</a></body></html>"""
                            code = 200
                # If we got here everything has gone correctly

            # This is the start of the medium level. The first option asks us to introduce the name of a gen of the
            # ensembl database and get back its  genomic sequence
            elif action == "/geneSeq":

                # This is the basic structure of the html page that we will get, it is incomplete...
                contents = f"""<!DOCTYPE html>
                <html lang = "en">            
                <head>  
                <meta charset = "utf-8"
                <title> Gene Sequence </title>
                </head>"""

                # We get the arguments that go after the ? in the path, Gen name = "whatever input we introduce"
                get_value = arguments[1]
                pair = get_value.split('?')

                # We have a couple of elements, split each by =. The value that will be used is the name of the gen
                gen, name_gene = pair[0].split("=")

                # Just addition to html response...
                contents += f"""<p> The sequence of gene {name_gene} is:  </p>"""

                # We set the main elements that will be used to get the list: ensembl server, endpoint that was
                # previously searched for this function and parameters
                server = 'rest.ensembl.org'
                first_endpoint = "xrefs/symbol/homo_sapiens/"
                parameters = '?content-type=application/json'
                first_request = first_endpoint + name_gene + parameters

                # Connect with the server
                conn = http.client.HTTPConnection(server)

                # Send the request message, using the GET method. We are
                # requesting the main page (/)
                try:
                    conn.request("GET", first_request)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # Read the response message from the server
                response = conn.getresponse()

                # -- Read the response's body
                body = response.read().decode()

                # Create a variable with the data, form the JSON received. We get the first element and the key of
                # dictionary that interest us, id
                body = json.loads(body)
                id_gene = body[0]
                id_gene = id_gene["id"]

                # Once we have the id (how it appears in ensemble database) of the gen that we want we perform a second
                # connection, now for getting the sequence that gene in concrete. We use the endpoint previously
                # researched in the ensembl api

                second_endpoint = "sequence/id/"
                second_request = second_endpoint + id_gene + parameters

                # Send the request message, using the GET method. We are
                # requesting the main page (/)
                try:
                    conn.request("GET", second_request)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # Read the second response message from the server
                response2 = conn.getresponse()

                # Read the second response's body
                body2 = response2.read().decode()

                # Create a variable with the data, form the second JSON received. We get the first element and the key
                # of dictionary that interest us, seq
                body2 = json.loads(body2)

                # We get the value associated to that key, the sequence of the gen. We add it to our html page
                sequence = body2["seq"]
                contents += f"""<p>{sequence}</p><a href="/">Main page</a></body></html>"""
                code = 200
                # If we got here everything has gone correctly

            # In this option we are asked to introduce a gene and get specific info about it

            elif action == "/geneInfo":

                # This is the basic structure of the html page that we will get, it is incomplete...
                contents = f"""<!DOCTYPE html>
                <html lang = "en">            
                <head>  
                <meta charset = "utf-8"
                <title> Gene Information</title>
                </head>"""

                # We get the arguments that go after the ? in the path, Gen name = "whatever input we introduce"
                get_value = arguments[1]
                pair = get_value.split('?')

                # We have a couple of elements, split each by =. The value that will be used is the name of the gen
                gen, name_gene = pair[0].split("=")

                # Just addition to html response...
                contents += f"""<p> The information of gene {name_gene} is:  </p>"""

                # We set the main elements that will be used to get the list: ensembl server, endpoint that was
                # previously searched for this function and parameters
                server = 'rest.ensembl.org'
                first_endpoint = "xrefs/symbol/homo_sapiens/"
                parameters = '?content-type=application/json'
                first_request = first_endpoint + name_gene + parameters

                # Connect to server
                conn = http.client.HTTPConnection(server)

                # Send the request message, using the GET method. We are
                # requesting the main page (/)
                try:
                    conn.request("GET", first_request)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # Read the response message from the server
                response = conn.getresponse()

                # Read the response's body
                body = response.read().decode()

                # Create a variable with the data, form the JSON received. We get the first element and the key of
                # dictionary that interest us, id
                body = json.loads(body)
                id_gene = body[0]
                id_gene = id_gene["id"]

                # Once we have the id (how it appears in ensemble database) of the gen that we want we perform a second
                # connection, now for getting the info that gene in concrete. We use the endpoint previously researched
                # in the ensembl api
                second_endpoint = "lookup/id/"
                second_request = second_endpoint + id_gene + parameters

                # Send the request message, using the GET method. We are
                # requesting the main page (/)
                try:
                    conn.request("GET", second_request)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # Read the second response message from the server
                response2 = conn.getresponse()

                # Read the second response's body
                body2 = response2.read().decode()

                # Create a variable with the data, form the JSON received. We get diferent values associated to the
                # keys that contain the info we are looking for
                body2 = json.loads(body2)
                length = int(body2["end"]) - int(body2["start"])

                # Once we have all the info collected, just complete the html response
                contents += f"""<p> The gene starts at: {body2["start"]} </p><p> The gene ends at: {body2["end"]} </p>
                <p> The gene length is: {length}</p>
                <p> The gene id is at: {id_gene} </p> <p> The gene is on chromosome: {body2["seq_region_name"]} </p>
                <a href="/">Main page</a></body></html>"""
                code = 200
                # If we got here everything has gone correctly

            # In this option we are asked to introduce a gene and perform some calculations with it, we will need Seq
            # from Seq1

            elif action == "/geneCalc":

                # This is the basic structure of the html page that we will get, it is incomplete...
                contents = f"""<!DOCTYPE html>
                <html lang = "en">            
                <head>  
                <meta charset = "utf-8"
                <title> Gene Calculations</title>
                </head>"""

                # We get the arguments that go after the ? in the path, Gen name = "whatever input we introduce"
                get_value = arguments[1]
                pair = get_value.split('?')

                # We have a couple of elements, split each by =. The value that will be used is the name of the gen
                seq_name, name_seq = pair[0].split("=")

                # We set the main elements that will be used to get the list: ensembl server, endpoint that was
                # previously searched for this function and parameters
                server = 'rest.ensembl.org'
                first_endpoint = "xrefs/symbol/homo_sapiens/"
                parameters = '?content-type=application/json'
                first_request = first_endpoint + name_seq + parameters

                # Connect with the server
                conn = http.client.HTTPConnection(server)

                # Send the request message, using the GET method. We are
                # requesting the main page (/)
                try:
                    conn.request("GET", first_request)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # Read the response message from the server
                response = conn.getresponse()
                # Read the response's body
                body = response.read().decode()

                # Create a variable with the data, form the JSON received. We get the first element and the key of
                # dictionary that interest us, id
                body = json.loads(body)
                id_gene = body[0]
                id_gene = id_gene["id"]

                # Once we have the id (how it appears in ensemble database) of the gen that we want we perform a second
                # connection, now for getting the info that gene in concrete. We use the endpoint previously researched
                # in the ensembl api
                second_endpoint = "sequence/id/"
                second_request = second_endpoint + id_gene + parameters

                # Send the request message, using the GET method. We are
                # requesting the main page (/)
                try:
                    conn.request("GET", second_request)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # Read the second response message from the server
                response2 = conn.getresponse()

                # Read the second response's body
                body2 = response2.read().decode()
                body2 = json.loads(body2)

                # Create a variable with the data, form the JSON received. We get  value associated to the
                # key that contain the info we are looking for, the gen sequence. We convert it into an object of our
                # class Seq in order to perform the calculations with it
                sequence = Seq(body2["seq"])
                list_of_bases = ["A", "C", "G", "T"]

                # Just addition to html response...
                contents += f"""<p> The length of gene {name_seq} is: {sequence.len()} </p>"""

                # We perform some calculations with the functions of Seq and add them to the html response to complete
                for base in list_of_bases:
                    perc_base = round(sequence.count_base(base) * 100 / sequence.len(), 2)
                    contents += f"""<p> {base} : {sequence.count_base(base)} ({perc_base}%) </p>"""
                contents += f"""<a href="/">Main page</a></body></html>"""
                code = 200
                # If we got here everything has gone correctly

            # In this last option we are asked to introduce a chromosome, an initial and final position within it and
            # get the list of genes that compose it located within thi interval

            elif action == "/geneList":

                # This is the basic structure of the html page that we will get, it is incomplete...
                contents = f"""<!DOCTYPE html>
                  <html lang = "en">            
                  <head>  
                  <meta charset = "utf-8"
                  <title> Gene List</title>
                  </head>"""

                # We get the arguments that go after the ? in the path, Chromosome  name = "whatever input we introduce"
                # Start = "whatever input we introduce" and End = "whatever input we introduce". We split this 3 couples
                # by &
                get_value = arguments[1]
                pairs = get_value.split('&')

                # We have a couple of elements, split each by =. The value that will be used is the name of the gen
                chromosome_name, chromosome = pairs[0].split("=")
                chromosome_start, start = pairs[1].split("=")
                chromosome_end, end = pairs[2].split("=")

                # Just addition to html response...
                contents += f"""<p> List of genes of the chromosome {chromosome}, which goes from {start} to {end} </p>
                """

                # We set the main elements that will be used to get the list: ensembl server, endpoint that was
                # previously searched for this function and parameters
                server = 'rest.ensembl.org'
                parameters = "?feature=gene;content-type=application/json"
                endpoint = "overlap/region/human/"
                request = endpoint + chromosome + ":" + start + "-" + end + parameters

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

                # Read the response's body
                body = json.loads(body)

                # We iterate through the dictionary and get the values associated with the key we are interested in
                for element in body:

                    # We add this info and our html response is now complete
                    contents += f"""<p>{element["external_name"]}</p>"""
                contents += f"""<a href="/">Main page</a></body></html>"""
                code = 200

        # With except we will be able to deal with whatever possible error, such as introducing invalid inputs or inputs
        # that don´t appear at the database, exceed the number of possible items of a list...
        except (KeyError, ValueError, IndexError, TypeError):
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