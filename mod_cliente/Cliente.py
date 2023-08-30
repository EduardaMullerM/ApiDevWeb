from pydantic import BaseModel

class Cliente(BaseModel):
    id_Cliente: int = None
    nome: str
    cpf: str
    telefone: str
    compra_fiado: str
    dia_fiado: str
    senha: str