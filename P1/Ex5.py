from Seq1 import Seq

baselist = ["A", "C", "T", "G"]

# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

seq_list = [s1, s2, s3]
for i in seq_list:
        print("Sequence",(seq_list.index(i) + 1), ": (Length: ", i.len(), ")", i)
        for base in baselist:
            print(base, ":", i.count_base(base))