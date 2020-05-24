from Seq1 import Seq
# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")
seq_list = [s1, s2]

for i in seq_list:
    print("Sequence", (seq_list.index(i)+1), ":", i)
