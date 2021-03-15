class rr:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        return self.a + other.a
    def __radd__(self,other):
        return self.a - other.a
    def __sub__(self,other):
        return self.a - other.a
    def __rsub__(self,other):
        return self.a - other.a
    def __le__(self,other):
        return self.a >= other.a
    def __lt__(self,other):
        return self.a > other.a
    def __ge__(self,other):
        return self.a == other.a
    def __gt__(self,other):
        return self.a == other.a
x = rr(10)
y = rr(10)

int0 = 0
