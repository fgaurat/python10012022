# value = input("Please enter an integer: ")
# x = int(value)

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

words = ['cat', 'window', 'defenestrate']

print(words)

for word in words:
    if len(word)>3:
        print(word,len(word))

for i in range(len(words)):
    print(i,words[i])

for i,word in enumerate(words):
    print(i,word)


print( list(range(10)))

a = sum([1,2,3])
a = sum(range(4))
print(a)