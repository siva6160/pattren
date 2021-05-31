n=int(input())
for i in range(1,n+1):
        if i%2:
            for j in range(i):
                print(i,end="")
        else:
            for j in range(i):
                print(j+1,end="")
        print()
