from pathlib import Path



FILENAME = "ADA.txt"
file_contents = Path(FILENAME).read_text()
lines= file_contents.split("\n")
body=lines[1:]
bodystr= " "
bodystr= bodystr.join(body).replace(" ","")
dna_chain=bodystr
print("Total length: ", len(dna_chain))

