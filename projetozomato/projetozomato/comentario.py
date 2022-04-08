class Comentario():
    def __init__(self, id: int, nome_especialista: str, frase: str):
        self._id = id
        self._autor = nome_especialista
        self._frase = frase
    
    def get_id(self): 
        return self._id
    
    def set_id(self, value):
        self._id = value
    
    def get_autor(self):
        return self._autor
    
    def set_autor(self, value):
        self._autor = value
    
    def get_frase(self):
        return self._frase
    
    def set_frase(self, value):
        self._frase = value