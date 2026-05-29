from enum import Enum


class StatusEnum(str, Enum):
    AGUARDANDO_ANALISE = "Aguardando Análise"
    PROCESSADO = "Processado"


class PrioridadeEnum(str, Enum):
    ALTA = "prioridade_alta"
    NORMAL = "prioridade_normal"
    # NONE = None
