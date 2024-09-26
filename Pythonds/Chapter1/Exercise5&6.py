def gcd(m,n):
   while(m%n!=0):
      oldm=m
      oldn=n
      m=oldn
      n=oldm%oldn
   return n
class Fraction:
   def __init__(self,top,bottom):
      if not isinstance(top,int) or not isinstance(bottom,int):
         raise TypeError("Numerator and denominator must both be integer")
      if bottom==0:
         raise ValueError("Denominator cannot be zero")
      if bottom<0:
         top=-top
         bottom=-bottom
      common=gcd(top,bottom)
      self.num=top//common
      self.den=bottom//common
   def __str__(self):
      return str(self.num)+"/"+str(self.den)
   def __add__(self,otherfraction):
      newnum=self.num*otherfraction.den+otherfraction.num*self.den
      newden=self.den*otherfraction.den
      return Fraction(newnum,newden)
   def __sub__(self,otherfraction):
      newnum=self.num*otherfraction.den-otherfraction.num*self.den
      newden=self.den*otherfraction.den
      return Fraction(newnum,newden)
   def __mul__(self,otherfraction):
      newnum=self.num*otherfraction.num
      newden=self.den*otherfraction.den
      return Fraction(newnum,newden)
   def __truediv__(self,otherfraction):
      newnum=self.num*otherfraction.den
      newden=self.den*otherfraction.num
      return Fraction(newnum,newden)
   def __eq__(self,other):
      firstnum=self.num*other.den
      secondnum=other.num*self.den
      return firstnum==secondnum
   def __ne__(self,other):
      return not self.__eq__(other)
   def __gt__(self,other):
      return self.num*other.den>other.num*self.den
   
   def __ge__(self,other):
      return self.num*other.den>=other.num*self.den
   def __lt__(self,other):
      return self.num*other.den<other.num*self.den
   def __le__(self,other):
      return self.num*other.den<=other.num*self.den

x=Fraction(1,-2)

y=Fraction(3,-4)

z=Fraction(-2,4)
print(x) 
print(y) 
print(z) 
print(x>y)
print(x<y)