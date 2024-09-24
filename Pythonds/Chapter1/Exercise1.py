class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator
    def getnum(self):
        return self.numerator
    def getDen(self):
        return self.denominator
fraction=Fraction(3,4)
print("Numerator:",fraction.getnum())
print("Denominator:",fraction.getDen())