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

class Gene(Seq):
    pass
#-- Main program
seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
for i in seq_list:
    print("Sequence",seq_list.index(i),":(Length:", i.len(),")",i)