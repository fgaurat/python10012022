from collections import deque


l=[]
l.append(12)
l.append(13)
l.append(14)
l.append(15)
l.append(16)
print(l)
i = l.pop(2)
print(i)
print(l)

l.insert(2,65)
print(l)

q = [1,2,3]

q.insert(0,0)
print(q)

d = deque(q,4)
print(d)
d.appendleft(-1)
print(d)
d.append(4)
print(d)
d.append(5)
print(d)

print(50*'-')

l=[]
for i in range(3):
    l.append(i*2) 
print(l)   

# l = list(map(lambda i:i*2,range(3)))
print(l)   

l=[i*2 for i in range(3)]
print(l)   

names = ['  Dupont ','  Durand  ',' Martin   ']

clean_names = []
for n in names:
    clean_names.append(n.strip())

print(clean_names)
clean_names = [n.strip() for n in names]
print(clean_names)

l = [1,2,3,4]
l2 = [i for i in l if i%2 == 0]
print(l2)
# l2 = [2,4]

l1 = ["valeur de a:","valeur de b:","valeur de c:"]
l2 = [2,3,45]
z = list(zip(l1,l2))
print(z)
print(50*"-")
z = list(zip(l1,l2))
print(list(z))
print(list(z))
# for zz in a:
#     print(*zz)

print(l2)
del l2[0]
print(l2)

a = 12
print(a)
del a
print(a)
