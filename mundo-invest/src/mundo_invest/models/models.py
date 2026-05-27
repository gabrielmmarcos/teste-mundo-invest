from sqlalchemy.orm import Mapped, mapped_column, registry

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
    status: Mapped[str]
    prioridade: Mapped[str]
