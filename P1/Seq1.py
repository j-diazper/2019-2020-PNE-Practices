from pathlib import Path


class Seq:
    """"A  class for representing seq object"""
    def __init__(self, strbases=None):
        can_continue = ""
        gen_list = ["A", "C", "G", "T"]
        self.strbases= strbases
        if strbases == None:
            print("NULL Seq created")
            self.strbases = "NULL"
        else:
            for i in strbases:
                if i not in gen_list:
                    can_continue="False"

                elif i in gen_list:
                    can_continue="True"
            if can_continue == "True":
                print("New sequence created")
            elif can_continue=="False":
                print("Invalid sequence")
                self.strbases = "ERROR"

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):
        count = 0
        if self.strbases == "ERROR":
            return "0"
        elif self.strbases == "NULL":
            return "0"
        else:
            for element in self.strbases:
                if element == base:
                    count = count + 1
        return count

    def count(self, base):
        list_of_bases = ["A", "C", "G", "T"]
        value_list=[]
        counter_A = 0
        counter_C = 0
        counter_G = 0
        counter_T = 0
        for i in self.strbases:
            if self.strbases == "NULL" or self.strbases == "ERROR":
                counter_A = 0
                counter_C = 0
                counter_G = 0
                counter_T = 0
                value_list.append(counter_A)
                value_list.append(counter_C)
                value_list.append(counter_T)
                value_list.append(counter_G)
                dict_1 = dict(zip(list_of_bases, value_list))
                return dict_1

            else:
                for i in self.strbases:
                    if i == "A":
                        counter_A += 1
                    elif i == "C":
                        counter_C += 1
                    elif i == "G":
                        counter_G += 1
                    elif i == "T":
                        counter_T += 1
                value_list.append(counter_A)
                value_list.append(counter_C)
                value_list.append(counter_G)
                value_list.append(counter_T)
                dict_1 = dict(zip(list_of_bases, value_list))
                return dict_1

    def reverse(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        else:
            return self.strbases[::-1]

    def complement(self):
        complements = ""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        else:
            for i in self.strbases:
                if i == "A":
                    i = "T"
                    complements = complements + i
                elif i == "T":
                    i = "A"
                    complements = complements + i
                elif i == "C":
                    i = "G"
                    complements = complements + i
                elif i == "G":
                    i = "C"
                    complements = complements + i
        return complements

    def read_fasta(self, filename):
        bodystr = ""
        file_contents = Path(filename).read_text()
        lines = file_contents.split('\n')
        body = lines[1:]
        bodystr = bodystr.join(body).replace(" ", "")
        return bodystr

    def processing_genes(self, baselist):
        dict_value = self.count(baselist)
        max_val = max(dict_value, key=dict_value.get)
        return max_val
    pass

