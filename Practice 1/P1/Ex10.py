from Seq1 import Seq
Folder = r"C:\Users\jesus.diaz\PycharmProjects\2019-2020-PNE-Practices\Practice 1\P1\\"
GEN_list=["U5","ADA", "FRAT1", "FXN","RNU6_269P"]
baselist=["A","C","G","T"]
txt=".txt"
for elements in GEN_list:
    FILENAME= Folder + elements + txt
    s = Seq()
    s1 = Seq(s.read_fasta(FILENAME))
    print("Gene",elements,":",s1.processing_genes(baselist))
