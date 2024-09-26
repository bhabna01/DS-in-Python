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
   def __add__(self,other):
      if isinstance(other,Fraction):
         newnum=self.num*other.den+other.num*self.den
         newden=self.den*other.den
         return Fraction(newnum,newden)
      elif isinstance(other,int):
         newnum=self.num+other*self.den
         return Fraction(newnum,self.den)
      else:
         return NotImplemented
   def __radd__(self,other):
      return self.__add__(other)
   
x=Fraction(1,2)
y=Fraction(3,4)

print(x+y)
print(3+x)
print(x+3)
      