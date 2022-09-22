import statistics
n=int(input())
l=list(map(int,input().split()))
print(statistics.mode(l))