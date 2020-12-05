def permute(list, s):
    if list == 1:
        return s
    else:
        return [y + x
                for y in permute(1, s)
                for x in permute(list - 1, s)
                ]

if __name__=='__main__':
    L='123456789'
    a=[]
    for i in L:
        a.append(['+%s' % i, '-%s' % i, '%s' % i])



    b=permute(9, ["0","1","2"])
    for i in range(len(b)):
        list_1=[]
        b_1=b[i]
        for j in range(len(b_1)):
            c= int(b_1[j])
            d=a[j][c]
            list_1.append(d)
        c = ''.join(map(str,list_1))
        if c[0] != '+':
            total= eval(c)
            if total == 100:
                total= ''.join(map(str,list_1))
                print(total)

