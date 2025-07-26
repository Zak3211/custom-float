class customFloat:
    def __init__(self, prefix_bits, suffix_bits, sign):
        self.bits = [False]*(prefix_bits + suffix_bits)
        self.suffix_bits = suffix_bits
        self.prefix_bits = prefix_bits
        self.sign = sign
    
    def __add__(self, other):
        """self + other"""

        #Ensuring both numbers are of the same structure
        if self.differentTypes(other):
            return None
        
        #If opposite signs, calls sister function
        if self.sign != other.sign:
            if not self.sign:
                return self.addOpposite(other)
            return other.addOpposite(self)

        #Adding the two numbers
        res = customFloat(self.prefix_bits, self.suffix_bits, self.sign)
        
        carry = False
        for i in range(len(res.bits) - 1, -1, -1):

            if not carry:
                if self.bits[i] and other.bits[i]:
                    carry = True
                elif self.bits[i] or other.bits[i]:
                    res.bits[i] = True
                continue
            
            if self.bits[i] and other.bits[i]:
                res.bits[i] = True
            elif not (self.bits[i] and other.bits[i]):
                carry = False
                res.bits[i] = True
            
        return res

    def addOpposite(self, other):
        """Handles Suboperation of opposite signs"""

        #self.sign == negative, other.sign == positive
        try:
            assert (not self.sign and other.sign)
        except AssertionError as error:
            print(error)
            return None
        
        res = customFloat(self.prefix_bits, self.suffix_bits, max(self, other).sign)

        
        carry = False
        for i in range(len(res.bits) - 1, -1, -1):
            continue
    
    def abs(self):
        res = 
    def __eq__(self, other):
        """self == other"""

        if self.differentTypes(other):
            return False
        return all(self.bits[i] == other.bits[i] for i in range(len(self.bits))) and self.sign == other.sign
    
    def __ne__(self, other):
        """self != other"""

        return not (self == other)
    
    def __gt__(self, other):
        """self > other"""

        if self.differentTypes(other):
            return None

        #If self is positive and other is negative
        if self.sign and not other.sign:
            return True

        #If other is positive and self is negative
        if other.sign and not self.sign:
            return False
            
        
        for i in range(len(self.bits)):
            if self.bits[i] and not other.bits[i]:
                return self.sign
            if other.bits[i] and not self.bits[i]:
                return not self.sign
        
        #The bits are equal
        return False
    
    def __ge__(self, other):
        """self >= other"""

        return self == other or self > other

    def __lt__(self, other):
        """self < other"""

        return not (other >= self) 
    
    def __le__(self, other):
        """self <= other"""

        return self < other or self == other
    
    def differentTypes(self, other):
        """Checks that the types are compaitable and returns True if they are not"""

        try :
            assert other.type == self.type, "Cannot add different types"
            assert self.prefix_bits == other.prefix_bits, "Cannot add different prefix bits"
            assert self.suffix_bits == other.suffix_bits, "Cannot add different suffix bits"
        except AssertionError as error:
            print(error)
            return True
        
        return False
