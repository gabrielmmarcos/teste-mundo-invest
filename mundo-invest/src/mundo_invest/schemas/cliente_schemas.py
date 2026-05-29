from typing import Optional

from pydantic import BaseModel, EmailStr, Field

# # teste
# from src.mundo_invest.enums.enums import StatusEnum
from mundo_invest.enums.enums import PrioridadeEnum, StatusEnum


class ClientePublic(BaseModel):
    # id: int
    cliente_nome: str
    cliente_email: EmailStr
    tipo_solicitacao: str
    valor_patrimonio: float


class ClienteResponse(ClientePublic):
    status: StatusEnum = Field(default=StatusEnum.AGUARDANDO_ANALISE)
    prioridade: Optional[PrioridadeEnum] = None


class ClienteList(BaseModel):
    clientes: list[ClienteResponse]


# para post webhook
class ClientePrioridade(ClienteResponse):
    prioridade: str
