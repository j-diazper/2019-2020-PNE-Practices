from Seq1 import Seq
Folder= "/home/alumnos/jdiazper/PycharmProjects/2019-2020-PNE-Practices/Session 04/Exercise 1/"
DNA_file= "U5.txt"
FILENAME1= Folder + DNA_file
# -- Create a Null sequence
s = Seq()
# -- Initialize the null seq with the given file in fasta format
s.read_fasta(FILENAME1)

print("Sequence:  (Length: ",i.len(),")",i,"\n",i.count(BASE_list),"\n","Rev: ",i.reverse(),"\n","Comp: ",i.complement())