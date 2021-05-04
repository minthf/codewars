class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        return [(x, ''.join(map(str,integers_list)).count(str(x))) for x in digits_list]