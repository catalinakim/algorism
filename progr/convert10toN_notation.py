import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]

# print('5의 3진법', convert(5,3))
# print('6의 3진법', convert(6,3))
# print('7의 3진법', convert(7,3))
# print('8의 3진법', convert(8,3))
# print('9의 3진법', convert(9,3))
# print('10의 3진법', convert(10,3))
# print('11의 3진법', convert(11,3))
# print('12의 3진법', convert(12,3))
# print('13의 3진법', convert(13,3))