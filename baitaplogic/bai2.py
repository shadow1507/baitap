
if __name__=='__main__':
    count = 0
    x=int(input("nhap x:"))
    print(x)
    y=int(input("nhap y:"))
    print(y)
    while(x>y):
        print("xin moi nhap lai x:")
        x = int(input())
        print("xin moi nhap la y:")
        y=int(input())

    while(x<y):
         if(y%2==0):
            y=y/2
            count =count+1
            print(y)
         else:
            y=y+1
            count = count + 1
         if x==y+1:
            count = count+1
            break

    print(count)