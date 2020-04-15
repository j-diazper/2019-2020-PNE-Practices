from Client0 import Client
GENE_LIST =["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]


print(f"-----| Practice 3, Exercise 7 |------")

# IP and PORT
IP = "127.0.0.1"
PORT = 8080

# CLient configuration
c = Client(IP, PORT)
print(c)

# Test PING
print("* Testing PING...")
print(c.talk("PING"))

# Test GET
print("* Testing GET...")
for i in range(5):
    comand = f"GET {i}"
    print(f"{comand}: {c.talk(comand)}")

# Test INFO
seq = c.talk("GET 0")
print("* Testing INFO...")
comand = f"INFO {seq}"
print(c.talk(comand))

# Test COMP
print("* Testing COMP...")
comand = f"COMP {seq}"
print(comand)
print(c.talk(comand))

# Test REV
print("* Testing REV...")
cmd = f"REV {seq}"
print(comand)
print(c.talk(comand))

# Test GENE
print("* Testing GENE...")
for gene in GENE_LIST:
    comand = f"GENE {gene}"
    print(comand)
    print(c.talk(comand))