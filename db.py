from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from settings import STR_DATABASE

engine = create_engine(STR_DATABASE)

Session = sessionmaker(bind=engine)

# para trabalhar com tabelas
Base = declarative_base()

# cria, caso não existam, as tabelas de todos os modelos
# que encontrar na aplicação (importados)
def criaTabelas():
    Base.metadata.create_all(engine)


# com o engine realizamos a conexão como banco de dados.
from sqlalchemy import create_engine

engine = create_engine("sqlite:///pastelaria_db.db") 

# permite enviar comandos para o banco, sejam comandos SQL puros ou recursos ORM, como por exemplo criar uma tabela e salvar dados nela.
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

#um objeto do tipo Base. • A documentação do sqlalchemy sugere criar uma classe base para todos os nossos modelos usando a função
#declarative_base() do pacote sqlalchemy.ext conforme o exemplo abaixo.

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() 

#Com a classe Base conseguimos criar nossos modelos, ou classes que representarão nossas tabelas e dados. • O comando abaixo, uma vez montado nossos modelos, 
#será utilizado para gerar toda a estrutura do banco, ou seja, com base nos modelos (classes), serão criadas as tabelas do banco de dados.

Base.metadata.create_all(engine)