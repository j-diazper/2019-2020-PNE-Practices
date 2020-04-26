import http.server
import http.client
import socketserver
from pathlib import Path
import json
# Port
PORT = 8080
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True
# List of sequences for Get option
Seq_List = ["AGATCGCGCCACTTCACTGCAGCCTCCGCGAAAGAGCGAAACTCCGTCTCA","TCCTTTCACTCCCAGCTCCCTGGAGTCTCTCACGTAGAATGTCCTCTCCACCCCCACCCA","CAGGAGGCTGAGGCGGGAGGATCGCTTGAGCCCAGGAGGTTGAGGCTGCAGTGAGGTGTG","CACTTGCAAATCATGCAGTTTATGTAGCATTTTCATTTAACACCTTCTCCCAACCATCTC","CTATGCTAACCCTGTGAACCGTTGCTCGCTTCTCCTTGACATCTGACGGCCTGGCCTTCT"""]
Folder = r"C:\\Users\\jesus.diaz\\PycharmProjects\\2019-2020-PNE-Practices\\Practice 1\\P1\\"
txt = ".txt"
# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """This method
        is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        print(self.requestline)
        # We get the first request line and then the path, goes after /. We get the arguments that go after the ? symbol
        req_line = self.requestline.split(' ')
        path = req_line[1]
        arguments = path.split('?')
        # Action is the first argument
        action = arguments[0]
        contents = Path('error.html').read_text()
        code = 200
        # First we open form-4.html if we don´t specify any action, this is the Index menu
        if action == "/":
            contents = Path('form-4.html').read_text()

        elif action == "/listSpecies":
            contents = f"""<!DOCTYPE html><html lang = "en"><head><meta charset = "utf-8" ><title></title ></head >
            <body><h2></h2><p>The total number of species in ensembl is: 267</p><p></p>"""
            # We get the arguments that go after the ? symbol
            get_value = arguments[1]
            # We get the seq index, after we have a couple of elements, the one which we need is the value of the index
            # position of the sequence
            seq_n = get_value.split('?')
            seq_name, index = seq_n[0].split("=")
            index = int(index)
            contents += f"""<p>The number of species you selected are: {index} </p>"""
            server = 'rest.ensembl.org'
            endpoint = 'info/species'
            parameters = '?content-type=application/json'
            conn = http.client.HTTPConnection(server)
            request = endpoint + parameters
            try:
                conn.request("GET", request)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()
            # -- Read the response message from the server
            response = conn.getresponse()
            # -- Read the response's body
            body = response.read().decode()
            limit_list = []
            body = json.loads(body)
            limit = body["species"]
            for element in limit:
                limit_list.append(element["display_name"])
                if len(limit_list) == index:
                    contents += f"""<p>The species are: </p>"""
                    for specie in limit_list:
                        contents += f"""<p> - {specie} </p>"""

            contents += f"""<a href="/">Main page</a></body></html>"""

        elif action == "/karyotype":
            contents = f"""<!DOCTYPE html><html lang = "en"><head><meta charset = "utf-8" ><title> Get </title ></head >
            <body><h2> The names of the chromosomes are:</h2>"""
            # We get the arguments that go after the ? symbol
            get_value = arguments[1]
            # We get the seq index, after we have a couple of elements, the one which we need is the value of the index
            # position of the sequence
            seq_n = get_value.split('?')
            seq_name, name_sp = seq_n[0].split("=")
            server = 'rest.ensembl.org'
            endpoint = 'info/assembly/'
            parameters = '?content-type=application/json'
            conn = http.client.HTTPConnection(server)
            request = endpoint + name_sp + parameters
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
            karyotype = body['karyotype']
            for chromosome in karyotype:
                contents += f"""<p> - {chromosome} </p>"""
            contents += f""""<a href="/"> Main page </a></body></html>"""

        elif action == "/chromosomeLength":
            # We get the arguments that go after the ? symbol
            pair = arguments[1]
            # We have a couple of elements, we need the sequence that we previously wrote and the operation to perform
            # that we previously selected
            pairs = pair.split('&')
            specie_name, specie = pairs[0].split("=")
            chromosome_index, chromosome = pairs[1].split("=")
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
            if specie == "" or chromosome == "":
                contents = Path('error.html').read_text()
            else:
                for chromo in chromosome_data:
                    if chromo["name"] == chromosome:
                        length = chromo["length"]
                        contents = f"""<!DOCTYPE html><html lang = "en"><head><meta charset = "utf-8" ><title> Length Chromosome</title >
                        </head ><body><h2> The length of the chromosome is: {length} </h2><a href="/">Main page</a></body></html>"""


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

