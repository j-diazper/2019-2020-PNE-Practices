class Seq:
    """"A  class for representing seq object"""
    def __init__(self,strbases):
        can_continue= ""
        gen_list=["A","C","G","T"]
        self.strbases= strbases
        for i in strbases:
            if i not in gen_list:
                can_continue="False"
            elif i in gen_list:
                can_continue="True"
        if can_continue == "True":
            print("New change created")
        elif can_continue=="False":
            print("ERROR")
    def __str__(self):
        return self.strbases
    def len(self):
        return len(self.strbases)
    pass

def generate_seqs(pattern, number):
    new_list = []
    base = ""
    for i in range(1, number + 1):
        base = i*pattern
        new_list.append(base)
    return new_list

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
for i in seq_list1:
    print(f"Sequence: {seq_list1.index(i)} (Length: {len(i)}) {i}")
print("List 2:")
for i in seq_list2:
    print(f"Sequence: {seq_list2.index(i)} (Length: {len(i)}) {i}")

