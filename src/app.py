from contextlib import asynccontextmanager
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, Request

from src.schemas import EntradaPredicao, RespostaPredicao

CAMINHO_MODELO = Path(__file__).resolve().parent.parent / "models" / "pipeline_rede_neural.joblib"


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.modelo = joblib.load(CAMINHO_MODELO)
    yield


app = FastAPI(title="API de Previsão de Cancelamento de Clientes", lifespan=lifespan)


@app.get("/diagnostico/modelo")
def diagnostico_modelo() -> dict[str, str]:
    return {
        "status": "operacional_v2",
        "framework": "FastAPI-Production",
        "modelo": "MLPClassifier",
    }


@app.post("/predict", response_model=RespostaPredicao, status_code=200)
def predict(entrada: EntradaPredicao, request: Request) -> RespostaPredicao:
    modelo = request.app.state.modelo
    dados = pd.DataFrame([entrada.model_dump()])
    probabilidades = modelo.predict_proba(dados)[0]
    indice = int(probabilidades.argmax())
    return RespostaPredicao(
        categoria_prevista=str(modelo.classes_[indice]),
        score_confianca=float(probabilidades[indice]),
    )
