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
def seq_count(seq):
        i = 0
        list_of_bases=["A","C","T","G"]
        value_list=[]
        counter_A = 0
        counter_C = 0
        counter_G = 0
        counter_T = 0
        file_contents = Path(seq).read_text()
        lines = file_contents.split("\n")
        body = lines[1:]
        bodystr = " "
        bodystr = bodystr.join(body).replace(" ", "")
        for i in bodystr:
            if i == "A":
                counter_A += 1
            elif i == "C":
                counter_C += 1
            elif i == "G":
                counter_G += 1
            elif i == "T":
                counter_T += 1
        value_list.append(counter_A)
        value_list.append(counter_T)
        value_list.append(counter_C)
        value_list.append(counter_G)
        dict_1= dict(zip(list_of_bases,value_list))
        return dict_1
def seq_reverse(seq):
    file_contents = Path(seq).read_text()
    lines = file_contents.split("\n")
    body = lines[1:]
    bodystr = " "
    bodystr = bodystr.join(body).replace(" ","")
    first20= bodystr[0:20]
    first20_reversed= first20[::-1]
    return (first20,first20_reversed)
def seq_complement(seq):
     file_contents = Path(seq).read_text()
    lines = file_contents.split("\n")
    body = lines[1:]
    bodystr = " "
    bodystr = bodystr.join(body).replace(" ","")
    first20= bodystr[0:20]
    complements=""
    for i in first20:
        if i=="A":
            i="T"
            complements=coomplements + i
        elif i=="T":
            i="A"
            complements=coomplements + i
        elif i=="C":
            i=="G"
            complements=coomplements + i
        elif i=="C":
            i=="G"
            complements=coomplements + i
     return(first20,complements)
  def processing_genes(seq):
        dict_value= seq_count(seq)
        max_val= max(dict_value, key= dict_value.get)
        return max_val








