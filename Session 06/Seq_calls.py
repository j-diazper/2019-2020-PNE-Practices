class Seq:
    """"A  class for representing seq object"""
    def __init__(self,strbases):
        self.strbases= strbases
        print("New sequence created ")
    def __str__(self):
        return self.strbases
    def len(self):
        return len(self.strbases)
    pass

class Gene(Seq):

    pass


#-- Main program
s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
