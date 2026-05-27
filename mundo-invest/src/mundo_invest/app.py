from http import HTTPStatus

from fastapi import FastAPI

app = FastAPI(
    title="Mundo Invest - Internal Management API",
    version="1.0.0",
    description="""Sistema interno para gerenciamento de clientes,
              controle de patrimônio investido e mapeamento
              de processos.""",
)


# endpoint root
@app.get("/", status_code=HTTPStatus.OK)
def read_root():
    # menssagem de boas vindas
    return {"message": "Teste técnico Mundo Invest!"}
