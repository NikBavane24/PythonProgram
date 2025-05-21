
def longest_word(a):
    words = a.split()

    for i in words:
        if len(a[0])<len(i):
            print(i)


longest_word("The fox jumps over the lazy dog")