import http.server
import http.client
import socketserver
from pathlib import Path
import json
# Port
PORT = 8080
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

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
       option = arguments[0]
       content = Path('error.html').read_text()
       cod = 404

       try:
           if option == "/":
               content = Path('index.html').read_text()
               cod = 200

           elif option == "/listSpecies":
               list_Species = []
               SERVER = 'rest.ensembl.org'
               ENDP = 'info/species'
               PRMS = '?content-type=application/json'
               REQ = ENDP + PRMS
               content = f"""<!DOCTYPE html>
               <html lang = "en">
               <head>
               <meta charset = "utf-8" >
               <title>List of species in the browser</title >
               </head >
               <body>
               <p>The total number of species in ensembl is: 267</p>"""
               get_value = arguments[1]
               couple = get_value.split('?')
               limit, limit_value = couple[0].split("=")
               conn = http.client.HTTPConnection(SERVER)
               try:
                   conn.request("GET", REQ)
               except ConnectionRefusedError:
                   print("ERROR! Cannot connect to the Server")
                   exit()
               # -- Read the response message from the server
               answer = conn.getresponse()
               # -- Read the response's body
               content_json = answer.read().decode()
               content_json = json.loads(content_json)
               limit = content_json["species"]
               limit_value = int(limit_value)
               if limit_value > len(limit):
                   content = """<!DOCTYPE html>
                   <html lang = "en">
                   <head>
                   <meta charset = "utf-8" >
                   <title>Error</title >
                   </head>
                   <body style="background-color: red;">
                   <h1>Index Error </h1>
                   <p>Index out of range. You must introduce correct value</p>
                   <a href="/">Index</a></body></html>"""
               else:
                   for i in limit:
                       display_name = i["display_name"]
                       list_Species.append(display_name)
                       if len(list_Species) == limit_value:
                           content += f"""<p>The number of species you selected are: {limit_value} </p>
                           <p>The species are: </p>"""
                           for display_name in list_Species:
                               content += f"""<p> - {display_name} </p>"""
                   content += f"""<a href="/">Main page</a></body></html>"""
               cod = 200

           elif option == "/karyotype":
               SERVER = 'rest.ensembl.org'
               ENDP = 'info/assembly/'
               PRMS = '?content-type=application/json'
               content = f"""<!DOCTYPE html>
               <html lang = "en">
               <head>
               <meta charset = "utf-8">
                <title> Karyotype </title >
               </head >
               <body>
               <h2> The names of the chromosomes are:</h2>"""
               get_value = arguments[1]
               couple = get_value.split('?')
               karyotype, specie = couple[0].split("=")
               conn = http.client.HTTPConnection(SERVER)
               REQ = ENDP + specie + PRMS
               try:
                   conn.request("GET", REQ)
               except ConnectionRefusedError:
                   print("ERROR! Cannot connect to the Server")
                   exit()
               answer = conn.getresponse()
               content_json = answer.read().decode()
               content_json = json.loads(content_json)
               kdata = content_json["karyotype"]
               for chromo in kdata:

                   content += f"""<p> - {chromo} </p>"""
               cod = 200
               content += f"""<a href="/">Index </a></body></html>"""

           elif option == "/chromosomeLength":
               SERVER = 'rest.ensembl.org'
               ENDP = 'info/assembly/'
               PRMS = '?content-type=application/json'
               get_value = arguments[1]
               couple = get_value.split('&')
               name, specie = couple[0].split("=")
               index, chromosome = couple[1].split("=")
               conn = http.client.HTTPConnection(SERVER)
               REQ = ENDP + specie + PRMS
               try:
                   conn.request("GET", REQ)
               except ConnectionRefusedError:
                   print("ERROR! Cannot connect to the Server")
                   exit()

               answer = conn.getresponse()

               content_json = answer.read().decode()
               content_json = json.loads(content_json)
               chromo_data = content_json["top_level_region"]
               for chromo in chromo_data:
                   name= chromo["name"]
                   for i in name:
                       if i == str(chromosome):
                           l = chromo["length"]
                           content = f"""<!DOCTYPE html><html lang = "en"><head><meta charset = "utf-8" ><title> Length Chromosome</title >
                           </head ><body><h2> The length of the chromosome is: <p> - {l} </p><a href="/">Index </a></body></html>"""
                           cod = 200
           elif option == "/geneList":  # Return the names of the genes located in the chromosome "chromo" from the start to end positions

               contents = f"""<!DOCTYPE html>
                                         <html lang = "en">            
                                         <head>  
                                         <meta charset = "utf-8"
                                         <title> Gene List</title>
                                         </head>"""

               # We get the arguments that go after the ?
               get_value = arguments[1]

               # We get the seq index, after we have a couple of elements, the one which we need is the value of the index
               # position of the sequence
               pairs = get_value.split('&')  # splits by the &
               chromo_value, chromo = pairs[0].split("=")  # having pair[0] as the species name
               chromosome_start, start = pairs[1].split("=")  # chromosome start (pair[1] column)
               chromosome_end, end = pairs[2].split("=")  # chromosome end (pair[2] column)

               contents += f"""<p> List of genes of the chromosome {chromo}, which goes from {start} to {end} </p>"""
               server = 'rest.ensembl.org'
               endpoint = "overlap/region/human/"  # first endpoint --> human
               parameters = '?feature=gene;content-type=application/json'
               request = endpoint + chromo + ":" + start + "-" + end + parameters  # request line
               conn = http.client.HTTPConnection(server)
               try:
                   conn.request("GET", request)  # connection request

               except ConnectionRefusedError:
                   print("ERROR! Cannot connect to the Server")  # exception for connection error
                   exit()

               # ----------------------Main program of geneList------------------------
               # -- Read the response message from the server
               response = conn.getresponse()
               # -- Read the response's body
               body = response.read().decode("utf-8")  # utf_8 to admit all characters in the response
               body = json.loads(body)

               for element in body:  # iteration to print all the elements of the chromosome within the chosen limits
                   print(element["external_name"])
                   contents += f"""<p>{element["external_name"]}</p>"""
               contents += f"""<a href="/">Main page</a></body></html>"""


       except (KeyError, ValueError, IndexError,TypeError):
               content = Path('error.html').read_text()

       # Generating the response message
       self.send_response(cod)  # -- Status line: OK!

       # Define the content-type header:
       self.send_header('Content-Type', 'text/html')
       self.send_header('Content-Length', len(str.encode(content)))

       # The header is finished
       self.end_headers()

       # Send the response message
       self.wfile.write(str.encode(content))

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
