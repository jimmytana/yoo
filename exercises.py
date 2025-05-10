a=[]
n=int(input("how many student you want to find their average :"))
for i in range(n):
    p=int(input("please enter maks to find the aveerage :"))
    a.append(p)
print(a)
avg=sum(a)/len(a)
print("the average of entered marks is :",avg)
