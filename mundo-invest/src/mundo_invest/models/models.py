from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class Cliente:
    __tablename__ = "clientes"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    nome: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    tipo_solicitacao: Mapped[str] = mapped_column(nullable=True)
    valor_patrimonio: Mapped[float] = mapped_column(nullable=True)

    status: Mapped[str]
    prioridade: Mapped[str]
