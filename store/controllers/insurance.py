from fastapi import APIRouter

router = APIRouter(prefix="/insurance", tags=["Insurance"])

# Dados fictícios
insurance_data = [
    {"id": 1, "name": "Seguro de Vida", "price": 120.50, "description": "Cobertura completa de vida."},
    {"id": 2, "name": "Seguro Residencial", "price": 300.00, "description": "Proteção contra desastres naturais."},
    {"id": 3, "name": "Seguro de Carro", "price": 450.00, "description": "Cobertura contra acidentes e roubo."},
]

@router.get("/")
async def get_insurances():
    return {"insurances": insurance_data}
