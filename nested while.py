#pattern
i=1
while i<=4:
   j=1
   while j<=4:
       print("#",end=" ")
       j+=1
   i+=1
   print( )

#example
i=1
while i<=2:
   j=1
   while j<=3:
       print(i,j)
       j+=1
   i+=1


#mutlipication tables
n=int(input())
i=1
while i<=n:
   j=1
   while j<=10:
       print(i,"x",j,"=",i*j)
       j+=1
   i+=1
   print( )

