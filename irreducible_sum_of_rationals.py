from fractions import Fraction
def sum_fracts(lst):
    frac = Fraction(sum([Fraction(a,b) for a,b in lst]))
    return [frac.numerator, frac.denominator] if frac.denominator > 1 else frac if frac.numerator>0 else None
