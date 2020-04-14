from Seq0 import *
Folder = "/home/alumnos/jdiazper/PycharmProjects/2019-2020-PNE-Practices/Session 04/Exercise 1/"
DNA_file = "U5.txt"
FILENAME1 = Folder + DNA_file
print("DNA file: ", DNA_file)
print("The first 20 bases are: \n", seq_read_fasta(FILENAME1))