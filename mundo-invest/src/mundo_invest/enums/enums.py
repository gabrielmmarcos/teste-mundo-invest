from enum import Enum


class StatusEnum(str, Enum):
    AGUARDANDO_ANALISE = "Aguardando Análise"
    ANALISADO = "Analisado"
