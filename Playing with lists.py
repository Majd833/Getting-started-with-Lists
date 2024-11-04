l=[9,5,6,7,3,98,1]
count=0
for i in l:
    count+=i
    avg=count/len(l)
print(count)
print(avg)
l.sort()
print("The Smallest value in l is:",l[0])
print("THe largest value in l is:",l[-1])