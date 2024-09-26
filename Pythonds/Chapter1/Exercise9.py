class Fraction:
    def __init__(self,num,den):
        self.num=num
        self.den=den
    
    def __str__(self):
        return f"{self.num}/{self.den}"
    def __repr__(self):
        return f"Fraction({self.num},{self.den})"
    
f=Fraction(3,4)
print(str(f))
print(repr(f))
