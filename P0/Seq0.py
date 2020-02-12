from pathlib import Path

list=[]
def seq_ping():
    print("Ok")
def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    lines = file_contents.split("\n")
    body = lines[1:]
    bodystr = " "
    bodystr = bodystr.join(body).replace(" ","")
    first20= bodystr[0:20]
    return (first20)
def seq_len(filename):
    file_contents = Path(filename).read_text()
    lines = file_contents.split("\n")
    body = lines[1:]
    bodystr = " "
    bodystr = bodystr.join(body).replace(" ", "")
    return(len(bodystr))
def seq_count_base(seq, base):
    counter=0
    file_contents = Path(seq).read_text()
    lines = file_contents.split("\n")
    body = lines[1:]
    bodystr = " "
    seq = bodystr.join(body).replace(" ", "")
    for i in seq:
        if i== base:
            counter+=1
    return(counter)



