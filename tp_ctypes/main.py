from ctypes import CDLL,c_char_p

def main():
    libc = CDLL('hello.o')
    libc.sayHello()

    name = b"toto"
    libc.hello(c_char_p(name))

if __name__ == '__main__':
    main()