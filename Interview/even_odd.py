import self


def even(self):
    a=[]
    b=[]
    for i in range(0,101):
        if i%2==0:
            a.append(i)
        if i%2!=0:
            b.append(i)
    print(a)
    print(b)



o1=even(self)