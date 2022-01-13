import traceback

from TwelveDivisionError import TwelveDivisionError

def division(a,b):
    if b == 12:
        # err = Exception("division par Douze !")
        err = TwelveDivisionError()
        raise err
    c = a/b
    return c

def call_division(a,b):
    r=0
    try:
        print("call_division")
        r = division(a,b)
    except Exception as e:
        print("erreur call_division",e)
        raise e
    finally:
        print("fin call_division")
    return r

def main():
    try:
        a=2
        b=int(input("Entrez la valeur de b : "))
        # c = a/b
        c = call_division(a,b)
        print(c)
    except ZeroDivisionError as e:
        traceback.print_exc()
        print("erreur !")
        print(e)
    except ValueError as e:
        print("un autre erreur !")
        print(e)
    except TwelveDivisionError as e:
        print("une erreur division!")
        print(e)
    except Exception as e:
        print("une erreur imprévue !")
        print(e)
    
    finally:
        print("finally, après l'erreur")    
    
    print("Après l'erreur")

if __name__ == '__main__':
    main()