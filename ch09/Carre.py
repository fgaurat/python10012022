


from Rectangle import Rectangle


class Carre(Rectangle):
    

    def __init__(self,cote):
        print(f"def __init__(self,{cote=})")
        self._cote = cote
    
    def get_cote(self):
        return self._cote

    def set_cote(self,cote):
        self._cote = cote
    

    # def __str__(self) -> str:
    #     return f"Carre {self._cote=}"