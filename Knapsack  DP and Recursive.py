#knapsack Algorithm
'''
#recursive
def knapsack(n,val,weight, w):
    if (n==0 or w ==0):
        return 0
    if weight[n-1]>w:
        return knapsack(n-1,val,weight, w)
    else:
        return max((val[n-1] + knapsack(n-1,val,weight, w-weight[n-1])), knapsack(n-1,val,weight, w))


val = list(map(int, input().rstrip().split()))
weight = list(map(int, input().rstrip().split()))
w = int(input())
n = len(val)
print(knapsack(n,val,weight, w))
'''

#dynamicProgramming

def knapSack(W,wt,val,n):
    K = [[0 for _ in range(W+1)]for _ in range(n+1)]

  #val is value Wt is weight of the respective value
  #W allowable weight (asked)
  #n is length of value

    for i in range(n+1):
        for w in range(W+1):
            if (i==0 or w ==0):
                K[i][w] =  0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] =  K[i-1][w]
    return K[n][W]

val = list(map(int, input().rstrip().split()))
wt = list(map(int, input().rstrip().split()))
W = int(input())
n = len(val)
print(knapSack(W,wt,val,n))
'''
'''
t = int(input())
T = input().rstrip().split()
num = 0
a = ["1","2", "3", "4", "5", "6", "7", "8", "9", "0"]
for element in T:
        if element[0] in a:
            element = int(element)
            if element > num:
                num = element
print(num)

