
def mult2(i):
    return i*2

# la = lambda i: i*2
# i = la(2)

l = [1,2,3,4,5]

# l2 = map( mult2, l)
l2 = map( lambda v: v*2, l)
l2 = list(l2)
print(l2)
# l2 = [2,4,6,8,10]

names = ['dupont','duRand','MARTIN']

cap_names = map( lambda v: v.capitalize(), names)
cap_names = list(cap_names)
print(cap_names)

names = ['  Dupont ','  Durand  ',' Martin   ']
print(names)
clean_names = map( lambda v: v.strip(), names)
clean_names = list(clean_names)
print(clean_names)


l = [1,2,3,4,5]
l2 = filter(lambda i:i>3,l)
l2 = list(l2)
print(l2)
# l2 = [4,5]
