"""n=int(input("eneter the no of rows:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("#",end=" ")
    print()

n=int(input("eneter the no of rows:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")

    print()"""

n=int(input("eneter the no of rows:"))
count=0
for i in range(1,n+1):
    for j in range(1,i+1):
        count=count+1
        print(count,end=" ")
    print()
