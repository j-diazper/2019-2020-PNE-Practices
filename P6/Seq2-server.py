import http.server
import socketserver
from pathlib import Path
from Seq1 import Seq


# Port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

Seq_List = ["AGATCGCGCCACTTCACTGCAGCCTCCGCGAAAGAGCGAAACTCCGTCTCA","TCCTTTCACTCCCAGCTCCCTGGAGTCTCTCACGTAGAATGTCCTCTCCACCCCCACCCA","CAGGAGGCTGAGGCGGGAGGATCGCTTGAGCCCAGGAGGTTGAGGCTGCAGTGAGGTGTG","CACTTGCAAATCATGCAGTTTATGTAGCATTTTCATTTAACACCTTCTCCCAACCATCTC","CTATGCTAACCCTGTGAACCGTTGCTCGCTTCTCCTTGACATCTGACGGCCTGGCCTTCT"]

Folder = r"C:\\Users\\jesus.diaz\\PycharmProjects\\2019-2020-PNE-Practices\\P6\\"
txt = ".txt"


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        print(self.requestline)
        # We get the first request line and then the path, goes after /. We get the arguments that go after the ? symbol
        req_line = self.requestline.split(' ')
        path = req_line[1]
        arguments = path.split('?')
        # Action is the first argument
        action = arguments[0]
        contents = Path('error.html').read_text()
        code = 404
        # First we open form-4.html if we don´t specify any action, this is the Index menu
        if action == "/":
            contents = Path('form-4.html').read_text()
            code = 200

        elif action == "/ping":
            contents = """
                    <!DOCTYPE html>
                    <html lang = "en">
                    <head>
                    <meta charset = "utf-8" >
                    <title> Ping </title >
                    </head >
                    <body>
                    <h2> PING OK!</h2>
                    <p> The SEQ2 server in running.... </p>
                    <a href="/">Main page</a>
                    </body>
                    </html>
                    """
            code = 200
        elif action == "/get":
            # -- Get the argument to the right of the ? symbol
            pair = arguments[1]
            # -- Get all the pairs name = value
            pairs = pair.split('&')
            # -- Get the two elements: name and value
            name, value = pairs[0].split("=")
            n = int(value)

            # -- Get the sequence
            seq = Seq_List[n]

            # -- Generate the html code
            contents = f"""
                                <!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                <meta charset = "utf-8" >
                                <title> Get </title >
                                </head >
                                <body>
                                <h2> Sequence number {n}</h2>
                                <p> {seq} </p>
                                <a href="/">Main page</a>
                                </body>
                                </html>
                                """
            code = 200
        elif action == "/gene":
            # -- Get the argument to the right of the ? symbol
            pair = arguments[1]
            # -- Get all the pairs name = value
            pairs = pair.split('&')
            # -- Get the two elements: name and value
            name, gene = pairs[0].split("=")

            s = Seq()
            Filename= Folder + gene + txt
            s1= Seq(s.read_fasta(Filename))
            gene_str = str(s1)
            # -- Generate the html code
            contents = f"""
                                <!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                <meta charset = "utf-8" >
                                  <title> Gene </title >
                                </head >
                                <body>
                                <h2> Gene: {gene}</h2>
                                <textarea readonly rows="20" cols="80"> {gene_str} </textarea>
                                <br>
                                <br>
                                <a href="/">Main page</a>
                                </body>
                                </html>
                                """
            code = 200
        elif action == "/operation":
            # -- Get the argument to the right of the ? symbol
            pair = arguments[1]
            # -- Get all the pairs name = value
            pairs = pair.split('&')
            # -- Get the two elements: name and value
            name, seq = pairs[0].split("=")
            # -- Get the two elements of the operation
            name, op = pairs[1].split("=")

            # -- Create the sequence
            s = Seq(seq)

            if op == "comp":
                result = s.complement()
            elif op == "rev":
                result = s.reverse()
            else:
                sl = s.len()
                ca = s.count_base('A')
                pa = "{:.1f}".format(100 * ca / sl)
                cc = s.count_base('C')
                pc = "{:.1f}".format(100 * cc / sl)
                cg = s.count_base('G')
                pg = "{:.1f}".format(100 * cg / sl)
                ct = s.count_base('T')
                pt = "{:.1f}".format(100 * ct / sl)

                result = f"""
                        <p>Total length: {sl}</p>
                        <p>A: {ca} ({pa}%)</p>
                        <p>C: {cc} ({pc}%)</p>
                        <p>G: {cg} ({pg}%)</p>
                        <p>T: {ct} ({pt}%)</p>"""

            contents = f"""
                                <!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                <meta charset = "utf-8" >
                                  <title> Operation </title >
                                </head >
                                <body>
                                <h2> Sequence </h2>
                                <p>{seq}</p>
                                <h2> Operation: </h2>
                                <p>{op}</p>
                                <h2> Result: </h2>
                                <p>{result}</p>
                                <br>
                                <br>
                                <a href="/">Main page</a>
                                </body>
                                </html>
                                """
            code = 200

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