from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

# teste
from src.mundo_invest.models.models import Cliente
from src.mundo_invest.schemas.cliente_schemas import ClientePublic
from src.mundo_invest.schemas.root_schemas import FilterPage

# from mundo_invest.models.models import Cliente
# from mundo_invest.schemas.cliente_schemas import ClientePublic
# from mundo_invest.schemas.root_schemas import FilterPage


async def read_all_clients_service(session: AsyncSession, filter: FilterPage):
    result = await session.scalars(
        select(Cliente).offset(filter.offset).limit(filter.limit)
    )

    return result.all()


async def create_client_service(
    client: ClientePublic, session: AsyncSession, is_batch=False
):
    db_product = await session.scalar(
        select(Cliente).where(
            and_(Cliente.cliente_email == client.cliente_email)
        )
    )

    if db_product:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail="Cliente Já Existe! Tente Cadastrar outro email.",
        )

    db_product = Cliente(
        cliente_nome=client.cliente_nome,
        cliente_email=client.cliente_email,
        tipo_solicitacao=client.tipo_solicitacao,
        valor_patrimonio=client.valor_patrimonio,
    )

    session.add(db_product)

    await session.commit()
    await session.refresh(db_product)

    return db_product
