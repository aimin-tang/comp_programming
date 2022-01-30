
def is_colorful(num):
    result_d = {}
    str_num = str(num)
    length = len(str_num)
    for start in range(length):
        for end in range(start+1, length+1):
            sub_num = str_num[start:end]
            prod_sub_num = 1
            for d in sub_num:
                prod_sub_num *= int(d)
            if prod_sub_num in result_d:
                return False
            else:
                result_d[prod_sub_num] = (start, end)
    else:
        return True

if __name__ == '__main__':
    print(is_colorful(3245))
    print(is_colorful(326))
