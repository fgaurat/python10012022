

s = {'val 1','val 2','val 3','val 1','val 2'}
s1 = {'val 10','val 2','val 3','val 4','val 5'}

print(s)
l = [1,2,3,1,2,5,6,1,2]
print(l)
l = list(set(l))
print(l)
s2 = s & s1
print(s2)

if 'val 1' in s:
    print("ok")