#TO-DO: improve function so it works for negative denary
def binary_converter(denary_num):
    if denary_num < 0:
        is_neg = True
        denary_num = abs(denary_num)
    else:
        is_neg = False
    result = ''
    if denary_num == 0:
        result = '0'
    while denary_num > 0:
        result = str(denary_num%2) + result
        denary_num = denary_num//2
    if is_neg:
        result = '-' +result
    return result