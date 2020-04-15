import socket
from Seq1 import Seq
#IP and PORT
IP = "127.0.0.1"
PORT = 8080

# -- Sequences for the GET command
SEQ_LIST = [
    "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
    "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
    "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
    "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT",
]

FOLDER = r"C:\\Users\\jesus.diaz\\PycharmProjects\\2019-2020-PNE-Practices\\Practice 1\P1\\"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

# GET option returns a sequence associated with the number introduced
def GET(SEQ_Index):
    return SEQ_LIST[SEQ_Index]

# INFO option returns the info associated with a sequence
def INFO(SEQ):
    # First convert the string into an object Seq, the using th class functions calculate the info with count_base and len
    s = Seq(SEQ)
    length = s.len()
    counter_A = s.count_base('A')
    perc_A = (100 * counter_A / length)
    counter_C = s.count_base('C')
    perc_C = (100 * counter_C / length)
    counter_G = s.count_base('G')
    perc_G = (100 * counter_G / length)
    counter_T = s.count_base('T')
    perc_T = (100 * counter_T / length)
    INFO = f"Sequence: {s},\n,Total length: {length},A: {counter_A} ({perc_A}%),\n,C: {counter_C} ({perc_C}%),\n,G: {counter_G} ({perc_G}%),\n,T: {counter_T} ({perc_T}%)"
    return INFO

# COMP option returns the complementary sequence of a sequence introduced previously
def COMP(SEQ):
    #First convert the string into an object Seq, then using the class function complement we return the complentary seq
    s = Seq(SEQ)
    return s.complement()


def REV(SEQ):
    # First convert the string into an object Seq, then using the class function reverse we return the reversed seq
    s = Seq(SEQ)
    return s.reverse()


def GENE(FILENAME):
    s = Seq(FILENAME)
    s = Seq(s.read_fasta(FOLDER + FILENAME + EXT))
    return str(s)


# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:

        # -- Receive the request message
        req_raw = cs.recv(2000)
        req = req_raw.decode()

        # ------ Process the command
        # -- Remove the \n
        lines = req.split("\n")
        line0 = lines[0].strip()

        # -- Separate the line into command an argument
        # -- Eliminate the blank spaces
        lcmds = line0.split(' ')

        # -- The first element is the command
        comand= lcmds[0]

        # -- Get the first argument
        try:
            argument = lcmds[1]
        except IndexError:
            # -- No arguments
            argument = ""

        # -- Response message
        answer = ""

        if comand == "PING":
            print("PING command!")
            answer = "OK!"
        elif comand == "GET":
            print("GET")
            answer = GET(int(argument))
        elif comand == "INFO":
            print("INFO")
            answer = INFO(argument)
        elif comand == "COMP":
            print("COMP")
            answer = COMP(argument)
        elif comand == "REV":
            print("REV")
            answer = REV(argument)
        elif comand == "GENE":
            print("GENE")
            answer = GENE(argument)
        else:
            print("Unknown command!!!")
            answer = "Unkwnown command"

        # -- Send the response message
        answer += '\n'
        print(answer)
        cs.send(answer.encode())
        cs.close()