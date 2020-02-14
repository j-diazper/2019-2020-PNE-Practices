from Seq0 import *
Folder= "/home/alumnos/jdiazper/PycharmProjects/2019-2020-PNE-Practices/Session 04/Exercise 1/"
GEN_list=["U5","ADA", "FRAT1", "FXN","U5"]
for elements in GEN_list:
    FILENAME2= Folder + elements + ".txt"
    print("Gene", elements,"---> Length: ",seq_len(FILENAME2))