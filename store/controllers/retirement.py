from fastapi import APIRouter

router = APIRouter(prefix="/retirement", tags=["Retirement"])

# Dados fictícios
retirement_data = [
    {"id": 1, "name": "Plano Básico", "contribution": 150.00, "benefits": "Rendimento de 3% ao ano."},
    {"id": 2, "name": "Plano Avançado", "contribution": 300.00, "benefits": "Rendimento de 5% ao ano."},
    {"id": 3, "name": "Plano Premium", "contribution": 500.00, "benefits": "Rendimento de 7% ao ano e cobertura extra."},
]

@router.get("/")
async def get_retirement_plans():
    return {"retirement_plans": retirement_data}
