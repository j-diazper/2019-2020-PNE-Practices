from Seq1 import Seq
FOLDER = r"C:\Users\jesus.diaz\PycharmProjects\2019-2020-PNE-Practices\Practice 1\P1"
FILE = r"\U5.txt"
FILENAME = FOLDER + FILE
baselist = ["A", "C", "G", "T"]
s = Seq()
s1 = Seq(s.read_fasta(FILENAME))
print("Sequence: (Length: ", s1.len(),": ",s1,"\n"," Bases: ",s1.count(baselist[0]),"\n","Rev: ",s1.reverse(),"\n","Comp: ",s1.complement())

