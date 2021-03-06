import http.server
import pathlib
import socketserver

# Port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


def reading_html(filename):  # read_file() is the function read_fasta_data() from other practice
    # -- Open and read the file
    file_contents = pathlib.Path(filename).read_text().split("\n")[1:]
    body = "".join(file_contents)
    return body


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        print(self.requestline)

        # ----------------------------------------------------------------------------------
        # Modifications for Practice 5

        # Message to send back to the client:
        Folder = r"C:\\Users\\jesus.diaz\\PycharmProjects\\2019-2020-PNE-Practices\\P5\\"
        if self.path == "" or self.path == "/index.html" or self.path == "/":
            File = "index.html"
            # Generating the response message
        else:
            File = self.path

        try:
            contents = reading_html(Folder + File)  # read_file() is the function read_fasta_data() from other practice
            # Generating the response message
            self.send_response(200)  # -- Status line: OK!
        except FileNotFoundError:
            File = "error.html"
            contents = reading_html(Folder + File)
            # Generating the response message
            self.send_response(404)  # -- Status line: ERROR NOT FOUND

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')  # Changed form text\plain to text text\html
        self.send_header('Content-Length', len(contents.encode()))

        # ----------------------------------------------------------------------------------

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

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