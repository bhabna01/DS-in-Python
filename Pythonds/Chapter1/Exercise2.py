def gcd(m,n):
    while m%n!=0:
        oldm=m
        oldn=n
        m=oldn
        n=oldm%oldn
    return n
class Fraction:
    def __init__(self,top,bottom):
        common=gcd(top,bottom)
        self.num=top//common
        self.den=bottom//common
    def __str__(self):
        return str(self.num)+'/'+str(self.den)
    def __add__(self,otherFraction):
        newnum=self.num*otherFraction.den+self.den*otherFraction.num
        newden=self.den*otherFraction.den
        return Fraction(newnum,newden)
    def __eq__(self,other):
        firstnum=self.num*other.den
        secondnum=other.num*self.den
        return firstnum==secondnum
x=Fraction(1,2)
y=Fraction(2,3)
print(x+y)
print(x==y)

