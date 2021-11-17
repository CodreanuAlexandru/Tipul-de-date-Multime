n1=int(input('Introduceti numarul de elmente in multimea A:'))
n2=int(input('Introduceti numarul de elmente in multimea B:'))
A=set()
B=set()
z1,z2=1,1
for z1 in range(n1):
    q1=input('Introduceti elementele multimii A:')
    A.add(q1)
for z2 in range(n2):
    q2=input('Introduceti elementele multimii B:')
    B.add(q2)
C=A
print(C.intersection(B))
D=A
print(D.union(B))
E=A
print(E.difference(B))