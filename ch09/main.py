from Rectangle import Rectangle


def main():
    r = Rectangle(12,5)
    print(Rectangle.get_cpt())
    r1 = Rectangle(2,5)
    print(Rectangle.get_cpt())

    # <Rectangle.Rectangle object at 0x106639100>
    s =str(r)
    print(s)

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