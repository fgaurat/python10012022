
def main():
    pass

def main_1():
    with open(r"lefichier.txt","w") as f:
        # f.write("Toto\n")
        # f.write("Titi\n")
        print("Toto",file=f)
        print("Titi",file=f)
        print("Toto",file=f)
        print("Titi",file=f)
    
    with open(r"lefichier.txt","r") as f:
        # Lit la totalité dans une chaîne
        # data = f.read()
        # print(data)
        data =f.readlines()
        print(data)
        for n,line in enumerate(data):
            s = f"ligne {n+1} {line.strip()}"
            print(s)

        # ligne 1 : Toto
        # ligne 2 : Titi
    


if __name__ == '__main__':
    main()