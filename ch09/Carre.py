


from Rectangle import Rectangle


class Carre(Rectangle):
    

    def __init__(self, cote) -> None:
        super().__init__(cote, cote)
        print(f"def __init__(self,{cote=})")
        self._cote = cote
    
    def get_cote(self):
        return self._cote

    def set_cote(self,cote):
        self._cote = cote
        self._longueur = cote
        self._largeur = cote


    def __str__(self) -> str:
        return f"Carre {self._cote=}"
    
    # Destructeur
    def __del__(self):
        print("del Carre",self)