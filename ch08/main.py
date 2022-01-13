def main():
    try:
        a=2
        b=int(input("Entrez la valeur de b : "))
        c = a/b
        print(c)
    except ZeroDivisionError as e:
        print("erreur !")
        print(e)
    
    print("Après l'erreur")

if __name__ == '__main__':
    main()