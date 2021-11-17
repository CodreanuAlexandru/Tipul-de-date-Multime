import itertools
def findsubsets(s, n):
    return list(itertools.combinations(s, n))
s = {'A','B','C','D'}
for n in range(1,len(s)+1):
    print(findsubsets(s, n))