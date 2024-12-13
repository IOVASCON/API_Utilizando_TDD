from fastapi import FastAPI
from store.routers import api_router

app = FastAPI(
    title="API de Seguros e Planos de Aposentadoria",
    description="API para gerenciar seguros e planos de aposentadoria.",
    version="1.0.0",
)

# Rota de boas-vindas
@app.get("/", tags=["Welcome"])
async def read_root():
    return {"message": "Bem-vindo à API de Seguros e Planos de Aposentadoria!"}

# Incluindo as rotas configuradas no api_router
app.include_router(api_router)
