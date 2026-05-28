from enum import Enum


class StatusEnum(str, Enum):
    AGUARDANDO_ANALISE = "Aguardando Análise"
    APROVADO = "Aprovado"
    RECUSADO = "Recusado"
