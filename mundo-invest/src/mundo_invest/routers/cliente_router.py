from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from mundo_invest.database import get_session
from mundo_invest.schemas.cliente_schemas import (
    ClienteList,
)
from mundo_invest.schemas.root_schemas import FilterPage
from mundo_invest.services.cliente_services import read_all_clients_service

router = APIRouter(prefix="/clientes", tags=["clientes"])

T_Session = Annotated[AsyncSession, Depends(get_session)]


@router.get("/all", response_model=ClienteList)
async def read_all_clients(
    session: T_Session, filter: Annotated[FilterPage, Query()]
):
    return {"clientes": await read_all_clients_service(session, filter)}
