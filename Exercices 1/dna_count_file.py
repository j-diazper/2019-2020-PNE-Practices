def counter(chain):
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
    len= counter_A+counter_C+counter_G + counter_T
    return(counter_A,counter_C,counter_G,counter_T,len)

with open("dna_count_file.txt","r") as f:
    data=f.read()
    print("A: ", counter(data)[0],"\n","C: ", counter(data)[1],"\n","G: ", counter(data)[2],"\n","T: ",counter(data)[3],"\n","Total length: ", counter(data)[4])



