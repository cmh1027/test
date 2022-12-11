# cook your dish here
from collections import Counter
T = int(input())
for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    C = Counter(L)
    _, count = C.most_common(1)[0]
    print(N - count)