from pydantic import BaseModel

class Produto(BaseModel):
    id_produto: int = None
    nome: str
    descricao: str
    cpf: str
    foto: str
    valor_unitario: float