"""
Wierd problem = nested if-else

n = int(input())
if not (n%2 == 0):
    print("wierd")
else:
    if n>=2 and n<=5:
        print("not wierd")
    if n>=6 and n<=20:
        print("wierd")
    if n>20:
        print("not wierd")

"""
'''
s1 = t1.split("-")
    hour1= (int(s1[-1])/100)*3600
    min1=  (int(s1[-1]) - ((int(s1[-1])/100)*100))*60
    
    s2 = t2.split("+")
    hour2= (int(s2[-1])/100)*3600
    min2=  (int(s2[-1]) - ((int(s2[-1])/100)*100))*60
    print((hour1+min1) - (hour2+min2))

        hour1= int(t1[-4] + t1[-3])
    min1=  int(t1[-2] + t1[-1])
    hour2= int(t2[-4] + t2[-3])
    min2=  int(t2[-2] + t2[-1])
    print(min1)
    if t1[-5] == "+" and t2[-5]=="+":
        return str((hour1*3600+min1*60) - (hour2*3600+min2*60))
    if t1[-5] == "+" and t2[-5]=="-":
        return str((hour1*3600+min1*60) + (hour2*3600+min2*60))
    if t1[-5] == "-" and t2[-5]=="+":
        return str((hour1*3600+min1*60) + (hour2*3600+min2*60))
    else:
        return str((hour1*3600+min1*60) - (hour2*3600+min2*60))


    # Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
for i in range(N):
    a = input()
    if a[-1]=='.':
        res= False
    else:   
        try :  
            float(a) 
            res = True
        except :  
            res = False
    print(res)
    
'''


a = int(input())
b = int(input())
c = int(input())
n = int(input())
p = [i for i in range(a+1)]
q = [i for i in range(b+1)]
r = [i for i in range(c+1)]
l = [(i,j,k) for (i,j,k) in zip(p,q,r) if i+j+k != n]
print(l)

