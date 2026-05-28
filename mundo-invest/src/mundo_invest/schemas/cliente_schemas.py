from pydantic import BaseModel, EmailStr, Field

# # teste
# from src.mundo_invest.enums.enums import StatusEnum

from mundo_invest.enums.enums import StatusEnum


class ClientePublic(BaseModel):
    # id: int
    cliente_nome: str
    cliente_email: EmailStr
    tipo_solicitacao: str
    valor_patrimonio: float


class ClienteResponse(ClientePublic):
    status: StatusEnum = Field(default=StatusEnum.AGUARDANDO_ANALISE)


class ClienteList(BaseModel):
    clientes: list[ClienteResponse]


class ClientePrioridade(ClienteResponse):
    prioridade: str
