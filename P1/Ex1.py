from Seq1 import Seq
seq_list = [Seq("ACT")]
for i in seq_list:
    print("Sequence",(seq_list.index(i)+1),":(Length:", i.len(),")",i)