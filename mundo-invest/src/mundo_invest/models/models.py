from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

# # teste
# from src.mundo_invest.enums.enums import StatusEnum, PrioridadeEnum
from mundo_invest.enums.enums import PrioridadeEnum, StatusEnum

table_registry = registry()


# tabela clientes
@table_registry.mapped_as_dataclass
class Cliente:
    # nome da tabela
    __tablename__ = "clientes"
    # colunas da tabela
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    cliente_nome: Mapped[str] = mapped_column(nullable=False)
    cliente_email: Mapped[str] = mapped_column(nullable=False, unique=True)
    tipo_solicitacao: Mapped[str] = mapped_column(nullable=True)
    valor_patrimonio: Mapped[float] = mapped_column(nullable=True)
    prioridade: Mapped[PrioridadeEnum] = mapped_column(
        nullable=True, init=False, default=PrioridadeEnum.NORMAL
    )
    status: Mapped[StatusEnum] = mapped_column(
        nullable=True, default=StatusEnum.AGUARDANDO_ANALISE, init=False
    )


# tabela webhook
@table_registry.mapped_as_dataclass
class Webhook:
    # nome da tabela
    __tablename__ = "webhook"
    # colunas da tabela
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    event_id: Mapped[str] = mapped_column(nullable=False, unique=True)
    card_id: Mapped[str] = mapped_column(nullable=False)
    # cliente_email: Mapped[str] = mapped_column(nullable=False)
    timestamp: Mapped[datetime] = mapped_column(
        init=False, onupdate=func.now(), server_default=func.now()
    )
