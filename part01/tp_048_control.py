

i = 12
def f(a=i):
    print(a)
i=100
f()


def add_to_list_2(a,l=[]):
    l.append(a)
    return l

def add_to_list(a,l=None):
    if l == None:
        l = []
    l.append(a)
    return l


def fib2(max_value):  # return Fibonacci series up to max_value
    """Return a list containing the Fibonacci series up to max_value."""
    result = []
    a, b = 0, 1
    while a < max_value:
        result.append(a)    # see below
        a, b = b, a+b
    return result


print(add_to_list(1)) # => [1]
print(add_to_list(2)) # => [2] ou [1,2]
print(add_to_list(3)) # => [3] ou [1,2,3]

fi = fib2(10)

# Positional Arguments
# Keyword Arguments

def hello(name:str,first_name:str):

    print("Hello,","name : ",name,"first_name : ",first_name)


hello(12,24)

# hello('GAURAT','Frédéric')
# hello('Frédéric','GAURAT')
# print(50*'-')
# hello(name='GAURAT',first_name='Frédéric')
# hello(first_name='Frédéric',name='GAURAT')
# # hello(name='GAURAT','Frédéric')
# hello('GAURAT',first_name='Frédéric')

# def mult2(la_liste:list) -> list:
#     la_nouvelle_liste=[]
#     for i in la_liste:
#         la_nouvelle_liste.append(i*2)
    
#     return la_nouvelle_liste

# def mult2_2(*values):
#     la_nouvelle_liste=[]
#     for i in values:
#         la_nouvelle_liste.append(i*2)
    
#     return la_nouvelle_liste
    

# l1 = [2,3,4,5]

# l2 = mult2(l1)
# print(l2)
# # [4,6,8,10]

# l2 = mult2_2(2,3,4,5,6)
# print(l2)
# l2 = mult2_2(2,3,4)
# print(l2)

# # l2 = mult2_2([2,3,4,5])
# # l2 = mult2_2(2,3,4,5)
# l2 = mult2_2(*l1)

# print(50*'-')

# def hello_2(**values):
#     # {'name': 'GAURAT', 'first_name': 'Frédéric', 'age': 45}
#     # JSON => JavaScript Object Notation
#     print(values['name'])
#     print(values['first_name'])
#     print(values['age'])

# # tuple => ()
# # list => []
# # dict => {k:v,k1:v1}

# # hello(name='GAURAT',first_name='Frédéric',age=45)

# print("toto","tutu")

# def hello(name,first_name):
#     print("Hello,","name : ",name,"first_name : ",first_name)


# hello("GAURAT","Fred")
# hello(name="GAURAT",first_name="Fred")
