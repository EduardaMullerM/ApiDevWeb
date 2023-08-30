from fastapi import APIRouter
from mod_cliente.Cliente import Cliente

router = APIRouter()

# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/cliente/", tags=["cliente"])
def get_cliente():
    return {"msg": "get todos executado"}, 200

@router.get("/cliente/{id}", tags=["cliente"])
def get_cliente(id: int):
    return {"msg": "get um executado"}, 200

@router.post("/cliente/", tags=["cliente"])
def post_cliente(c: Cliente):
    return {"msg": "post executado", "nome": c.nome, "cpf": c.cpf, "telefone": c.telefone, "compra_fiado": c.compra_fiado, "dia_fiado": c.dia_fiado, "senha": c.senha}, 200

@router.put("/cliente/{id}", tags=["cliente"])
def put_cliente(id: int, c: Cliente):
    return {"msg": "put executado", "id": id, "nome": c.nome, "cpf": c.cpf, "telefone": c.telefone, "compra_fiado": c.compra_fiado, "dia_fiado": c.dia_fiado, "senha": c.senha}, 201

@router.delete("/cliente/{id}", tags=["cliente"])
def delete_cliente(id: int):
    return {"msg": "delete executado"}, 201