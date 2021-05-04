def two_decimal_places(number):
    number = str(number)
    return float(number[:number.find('.')+3])