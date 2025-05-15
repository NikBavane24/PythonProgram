


def Change_string(str1):
    print(str1[-1:])
    print(str1[1:-1])
    print(str1[:-1])

    return str1[-1:] + str1[1:-1] + str1[:1]


Change_string("ABCDE")