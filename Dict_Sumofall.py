


a={1:10,2:20,3:30}


def sum1(dict):
    l1=[]
    for i in dict:
        l1.append(dict[i])

    final=sum(l1)
    print(final)

sum1(a)
