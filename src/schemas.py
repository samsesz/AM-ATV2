from typing import Literal

from pydantic import BaseModel, Field


class EntradaPredicao(BaseModel):
    meses_contrato: int = Field(
        ge=0,
        le=120,
        description="Tempo de permanência do cliente, em meses",
        examples=[12],
    )
    cobranca_mensal: float = Field(
        ge=0.0,
        le=200.0,
        description="Valor cobrado mensalmente, em dólares",
        examples=[70.35],
    )
    cobranca_total: float = Field(
        ge=0.0,
        le=15000.0,
        description="Valor total já cobrado do cliente, em dólares",
        examples=[844.2],
    )
    tipo_contrato: Literal["Month-to-month", "One year", "Two year"] = Field(
        description="Modalidade do contrato", examples=["Month-to-month"]
    )
    servico_internet: Literal["DSL", "Fiber optic", "No"] = Field(
        description="Tipo de serviço de internet contratado", examples=["Fiber optic"]
    )
    forma_pagamento: Literal[
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)",
    ] = Field(description="Forma de pagamento", examples=["Electronic check"])
    fatura_digital: Literal["Yes", "No"] = Field(
        description="Se o cliente aderiu à fatura digital", examples=["Yes"]
    )
    suporte_tecnico: Literal["Yes", "No", "No internet service"] = Field(
        description="Se o cliente possui suporte técnico", examples=["No"]
    )
    seguranca_online: Literal["Yes", "No", "No internet service"] = Field(
        description="Se o cliente possui segurança online", examples=["No"]
    )


class RespostaPredicao(BaseModel):
    categoria_prevista: str = Field(
        description="Classe prevista pelo modelo: Cancelou ou Permaneceu"
    )
    score_confianca: float = Field(
        ge=0.0,
        le=1.0,
        description="Probabilidade da classe prevista, calculada por predict_proba",
    )
