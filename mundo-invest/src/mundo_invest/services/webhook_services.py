from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from mundo_invest.enums.enums import PrioridadeEnum, StatusEnum
from mundo_invest.models.models import Cliente, Webhook
from mundo_invest.schemas.root_schemas import FilterPage


async def read_all_webhooks_service(session: AsyncSession, filter: FilterPage):
    result = await session.scalars(
        select(Webhook).offset(filter.offset).limit(filter.limit)
    )

    return result.all()


async def create_webhook_service(
    webhook,
    session: AsyncSession,
):
    db_webhook = await session.scalar(
        select(Webhook).where(Webhook.event_id == webhook.event_id)
    )

    if db_webhook:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail="Evento já processado!  Tente criar outro evento.",
        )

    cliente = await session.scalar(
        select(Cliente).where(Cliente.cliente_email == webhook.cliente_email)
    )

    if not cliente:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Cliente não encontrado! Tente digitar outro email",
        )

    VALOR_PRIORIDADE_ALTA = 200000

    if cliente.valor_patrimonio >= VALOR_PRIORIDADE_ALTA:
        cliente.prioridade = PrioridadeEnum.ALTA
    else:
        cliente.prioridade = PrioridadeEnum.NORMAL

    cliente.status = StatusEnum.PROCESSADO

    novo_webhook = Webhook(
        event_id=webhook.event_id,
        card_id=webhook.card_id
    )

    session.add(novo_webhook)

    await session.commit()

    await session.refresh(cliente)

    return cliente
