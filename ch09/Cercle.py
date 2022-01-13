import math


class Cercle:
    
    

    def __init__(self,rayon) -> None:
        self._rayon=rayon
    
    def get_rayon(self):
        return self._rayon

    def set_rayon(self,rayon):
        self._rayon = rayon
    
    def get_surface(self):
        return self._rayon**2*math.pi
    
    def __str__(self) -> str:
        return f"Cercle {self._rayon=}"
