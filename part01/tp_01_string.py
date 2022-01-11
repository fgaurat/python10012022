

s = '"Il fait beau mais". \nL\'orage gronde'
print(s)

path = r"c:\terminal\newuser"
print(path)

longue_chaine = """
        Ligne 1
        Ligne 2
        Ligne 3
"""
print(longue_chaine)

ligne_1="La ligne 1"
ligne_2="La ligne 2"
lignes = ligne_1+" "+ligne_2
a = 2
b = 3
c = a+b
print(lignes)
print(c)
ligne_a = "Valeur de c = "+str(c)
print(ligne_a)
str_a ="2"
str_b ="3"
c = int(str_a)+int(str_b)
print(c)
print(50*'-')
a = "toto"
b = a*3
print(b)
print(50*"-")

s = "Python"
print(s[1])

print(len(s))

print(s[len(s)-1])
print(s[-1])
print(s[-4])

print(s[:4])
print(s[4:])
print(len(s[42:]))


print(s)
# s[0]='J'
print( hex(id(s)))
s = 'J'+s[1:]
print(s)

s1 = "toto"
s2 = "toto"

print(id(s1))
print(id(s2))

