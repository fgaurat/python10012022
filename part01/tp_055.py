d = {'name':"GAURAT","first_name":"Fred"}

print(d['name'])
d['age']=45
print(d)
d['age']=100
print(d)

for k in d:
    print(k,d[k])

if 'name' in d:
    print("ok")

l = ['name','first_name','age']
l1 = ['GAURAT','Fred',45]

d2 = dict(zip(l,l1))
print(d2)

# {'name':"GAURAT","first_name":"Fred",age:45}

d3 = {l[i]:l1[i] for i in range(len(l))}
print(d3)
# {'name':"GAURAT","first_name":"Fred",age:45}


print (50*'-')

print(d3.keys())
print(d3.values())

for k,v in d3.items():
    print(k,v)


l = list(d3)
print(l)

