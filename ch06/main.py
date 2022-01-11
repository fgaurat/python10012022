# import fibo as fi
from fibo import fib as f,fib2
import sys


def main():
    print(sys.argv)
    value = int(sys.argv[1])
    # def fib(n):
    #     print("bonjour",n)

    # fi.fib(100)
    # a = fi.fib2(100)
    # print(a)

    print("module main",__name__)
    f(value)


if __name__ == "__main__":
    main()

