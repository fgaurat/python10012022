from Rectangle import Rectangle


def main():
    r = Rectangle(12,5) # Créer un objet r instance de la class Rectangle

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