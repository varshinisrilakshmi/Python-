"""#3 question:
n=int(input())
factorial=1
for i in range(1,n+1):
    factorial*=i
print(factorial)"""


"""#4th question:
for i in range(1,101):
    if  i%3==0 and i%5==0:
        print(i)"""

"""#5 question:
digit=int(input())
n1=digit//100
remain=digit%100
n2=remain//10
n3=remain%10
print(n1+n2+n3)"""


"""name=input()
vowels="aeiou"
count=0
for z in name:
    if z in vowels:
        count+=1
print(count)"""


numbers = [10, 24, 76, 23, 12]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("The largest number is:", largest)






