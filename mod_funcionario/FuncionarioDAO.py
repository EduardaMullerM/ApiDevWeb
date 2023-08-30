from fastapi import APIRouter
from mod_funcionario.Funcionario import Funcionario

router = APIRouter()

# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/funcionario/", tags=["funcionario"])
def get_funcionario():
    return {"msg": "get todos executado"}, 200

@router.get("/funcionario/{id}", tags=["funcionario"])
def get_funcionario(id: int):
    return {"msg": "get um executado"}, 200

@router.post("/funcionario/", tags=["funcionario"])
def post_funcionario(f: Funcionario):
    return {"msg": "post executado", "nome": f.nome, "matrícula": f.matricula, "cpf": f.cpf, "telefone": f.telefone, "grupo": f.grupo, "senha": f.senha}, 200

@router.put("/funcionario/{id}", tags=["funcionario"])
def put_funcionario(id: int, f: Funcionario):
    return {"msg": "put executado", "id": id, "nome": f.nome, "matrícula": f.matricula, "cpf": f.cpf, "telefone": f.telefone, "grupo": f.grupo, "senha": f.senha}, 201

@router.delete("/funcionario/{id}", tags=["funcionario"])
def delete_funcionario(id: int):
    return {"msg": "delete executado"}, 201