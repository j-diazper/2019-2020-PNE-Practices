# Counting DNA chains and its components

def counter(chain):
    i=0
    counter_A=0
    counter_C = 0
    counter_G = 0
    counter_T = 0
    for i in chain:
        if i=="A":
            counter_A+=1
        elif i=="C":
            counter_C += 1
        elif i=="G":
            counter_G += 1
        elif i=="T":
            counter_T+=1
    return(counter_A,counter_C,counter_G,counter_T)


dna_chain=input("Introduce the sequence: ")
print("Total length: ", len(dna_chain),"\n","A: ", counter(dna_chain)[0],"\n","C: ", counter(dna_chain)[1],"\n","G: ", counter(dna_chain)[2],"\n","T: ", counter(dna_chain)[3],)





