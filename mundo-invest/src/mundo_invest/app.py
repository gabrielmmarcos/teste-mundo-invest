import asyncio
from http import HTTPStatus
from sys import platform

from fastapi import FastAPI

from mundo_invest.routers.cliente_router import router
from mundo_invest.schemas.root_schemas import Message

if platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


app = FastAPI(
    title="Mundo Invest - Internal Management API",
    version="1.0.0",
    description="""Sistema interno para gerenciamento de clientes,
              controle de patrimônio investido e mapeamento
              de processos.""",
)

app.include_router(router)


# endpoint root
@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    # menssagem de boas vindas
    return {"message": "Teste técnico Mundo Invest!"}
