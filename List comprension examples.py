#convert number to string and separate each number and save to list
num = [int(d) for d in str(input("Enter the number:"))] 

#dictionary key for a particular kind of value
l1 = [name for name, number in all_freq.items() if number == m] 

#blank matrix list
K = [[0 for _ in range(W+1)]for _ in range(n+1)] 

#Directly taking list input
list1 = list(map(int, input().rstrip().split()))
