from projetozomato.comentario import Comentario

class Restaurante():
    def __init__(self, id: int, nome: str, foto_url: str, endereco: str, funcionamento: str, comentario: list[Comentario] ):
        self._id = id
        self._nome = nome
        self._foto_url = foto_url
        self._endereco = endereco
        self._funcionamento = funcionamento
        self._comentario = comentario

    def get_id(self): 
        return self._id
    
    def set_id(self, value):
        self._id = value
    
    def get_nome(self):
        return self._nome
    
    def set_nome(self, value):
        self._nome = value

    def get_foto_url(self):
        return self._foto_url
    
    def set_foto_url(self, value):
        self._foto_url = value

    def get_endereco(self):
        return self._endereco
    
    def set_endereco(self, value):
        self._endereco = value

    def get_funcionamento(self):
        return self._funcionamento
    
    def set_funcionamento(self, value):
        self._funcionamento = value
    
    def get_comentarios(self):
        return self._comentario
    
    def set_comentarios(self, value):
        self._comentario.append(value)
    