from sqlalchemy.orm import Mapped, mapped_column, registry

from mundo_invest.enums.enums import StatusEnum

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
    prioridade: Mapped[str] = mapped_column(nullable=True, init=False)
    status: Mapped[StatusEnum] = mapped_column(
        nullable=True, default=StatusEnum.AGUARDANDO_ANALISE, init=False
    )
