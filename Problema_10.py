import itertools
def findsubsets(s, n):
    return list(itertools.combinations(s, n))
s = {1,2,3,4}
for n in range(1,len(s)+1):
    print(findsubsets(s, n))