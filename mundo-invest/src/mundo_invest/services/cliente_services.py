from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from mundo_invest.models.models import Cliente
from mundo_invest.schemas.root_schemas import FilterPage


async def read_all_clients_service(session: AsyncSession, filter: FilterPage):
    result = await session.scalars(
        select(Cliente)
        .offset(filter.offset)
        .limit(filter.limit)
    )

    return result.all()