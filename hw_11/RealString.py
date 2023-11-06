import string

class RealString:
    def __init__(self, string = ""):
        self.string = string

    @classmethod
    def converter(cls, object):
        if type(object) == str:
            return cls(object)

    def __lt__(self, other):
        new_operand_2 = RealString.converter(other)
        return len(self.string) < len(new_operand_2.string)

    def __gt__(self, other):
        new_operand_2 = RealString.converter(other)
        return len(self.string) > len(new_operand_2.string)

    def __le__(self, other):
        new_operand_2 = RealString.converter(other)
        return len(self.string) <= len(new_operand_2.string)

    def __ge__(self, other):
        new_operand_2 = RealString.converter(other)
        return len(self.string) >= len(new_operand_2.string)

    def __eq__(self, other):
        new_operand_2 = RealString.converter(other)
        return len(self.string) == len(new_operand_2.string)

    def __ne__(self, other):
        new_operand_2 = RealString.converter(other)
        return len(self.string) != len(new_operand_2.string)



