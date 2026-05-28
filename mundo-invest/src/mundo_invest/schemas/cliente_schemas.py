from pydantic import BaseModel, EmailStr, Field

from mundo_invest.enums.enums import StatusEnum


class ClientePublic(BaseModel):
    id: int
    cliente_nome: str
    cliente_email: EmailStr
    tipo_solicitacao: str
    valor_patrimonio: float


class ClienteList(BaseModel):
    clientes: list[ClientePublic]


class ClienteResponde(ClientePublic):
    status: StatusEnum = Field(default=StatusEnum.AGUARDANDO_ANALISE)


class ClientePrioridade(ClienteResponde):
    prioridade: str
