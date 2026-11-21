# Previsão de cancelamento de clientes com MLP e FastAPI

Rede neural multicamadas (MLP) treinada com Scikit-Learn para prever se um cliente de telecomunicações irá cancelar o serviço, exposta por uma API REST em FastAPI.

- **Dataset:** [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) (Kaggle, 7.043 registros)
- **Problema:** classificação binária (`Cancelou` x `Permaneceu`)
- **Modelo:** `Pipeline` com `ColumnTransformer` (`StandardScaler` + `OneHotEncoder`) e `MLPClassifier(hidden_layer_sizes=(128, 64, 32), random_state=77)`

## Estrutura

```
data/dataset.csv                     base original do Kaggle
models/pipeline_rede_neural.joblib   pipeline serializado (gerado pelo notebook)
notebooks/analise_treinamento.ipynb  EDA, treinamento e métricas
src/schemas.py                       contratos Pydantic de entrada e saída
src/app.py                           FastAPI com lifespan e endpoints
requisicoes.http                     testes de integração HTTP
```

## Como reproduzir

Pré-requisito: [uv](https://docs.astral.sh/uv/) instalado.

1. Baixe o dataset no Kaggle e salve o CSV como `data/dataset.csv`.
2. Instale as dependências:
   ```bash
   uv sync
   ```
3. Execute todas as células de `notebooks/analise_treinamento.ipynb` com o kernel do ambiente `.venv`. Isso gera `models/pipeline_rede_neural.joblib`.
4. Inicie a API:
   ```bash
   uv run fastapi dev src/app.py
   ```
5. Acesse a documentação interativa em http://127.0.0.1:8000/docs e execute `requisicoes.http` com a extensão REST Client ou Thunder Client.

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | `/diagnostico/modelo` | Status do serviço e modelo em uso |
| POST | `/predict` | Recebe o perfil do cliente e retorna `categoria_prevista` e `score_confianca` |

Entradas inválidas (tipo incorreto, valor fora dos limites ou categoria inexistente) retornam HTTP 422.
