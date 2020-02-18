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
    new_list= pattern * number
    return new_list
seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print(seq_list1)
print("List 2:")
print(seq_list2)