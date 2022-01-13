from Rectangle import Rectangle
from Carre import Carre


def main():
    c = Carre(2)
    print(c.get_cote())
    print(c.get_surface())
    # print(c)
    # print(c.get_surface())

def main_2():
    r = Rectangle(12,5)
    print(Rectangle.get_cpt())
    r1 = Rectangle(12,6)
    print(Rectangle.get_cpt())

    # <Rectangle.Rectangle object at 0x106639100>
    s = str(r)
    print(s)

    # del r
    print(r)
    print(r1)



    # if r.__eq__(r1):
    if r==r1:
        print("ok")
    else:
        print("ko")

def main_1():
    r = Rectangle(12,5) # Créer un objet r instance de la class Rectangle
    print(type(r))
    longueur = r.get_longueur()
    print(longueur) # 12
    
    largeur = r.get_largeur()
    print(largeur) # 5

    r.set_longueur(2)
    r.set_largeur(4)

    print(r.get_longueur())
    print(r.get_largeur())

    print(f"{r.get_surface()=}")


if __name__ == '__main__':
    main()