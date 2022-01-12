from Rectangle import Rectangle


def main():
    r = Rectangle(12,5) # Créer un objet r instance de la class Rectangle
    
    longueur = r.get_longueur()
    print(longueur) # 12
    
    largeur = r.get_largeur()
    print(largeur) # 5

if __name__ == '__main__':
    main()