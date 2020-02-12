from Seq0 import *
Folder= "/home/alumnos/jdiazper/PycharmProjects/2019-2020-PNE-Practices/Session 04/Exercise 1/"
DNA_file= "U5.txt"
FILENAME1= Folder + DNA_file
print("Calling ping...")
seq_ping()
print("DNA file: ", DNA_file)
print("The first 20 bases are: \n",seq_read_fasta(FILENAME1))
GEN_list=["U5","ADA", "FRAT1", "FXN","U5"]
for elements in GEN_list:
    FILENAME2= Folder + elements + ".txt"
    print("Gene", elements,"---> Length: ",seq_len(FILENAME2))
BASE_list=["A","C","T","G"]
for elements in GEN_list:
    FILENAME2= Folder + elements + ".txt"
    for i in BASE_list:
        print("Gene", elements,"\n", i, seq_count_base(FILENAME2,i))