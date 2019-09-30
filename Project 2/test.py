class Fraction(object):
    def __init__(self, top, bottom):
        self.numerator = top
        self.denominator = bottom

    def __str__(self):
      # return str(self.numerator) + "/" + str(self.denominator)
       return str(float(self.numerator/self.denominator))

    def __float__(self):
        return float(self.numerator/self.denominator)

    #def __gt__(self, other):
    #    if(self > other):
    #        return True
    #    else: 
    #        return False

def main():
    f1 = Fraction(2,3)
    f2 = Fraction(1,2)
    if(float(f1) > float(f2)):
        print("fl > f2")

main()