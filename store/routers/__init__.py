from fastapi import APIRouter
from store.controllers.insurance import router as insurance_router
from store.controllers.retirement import router as retirement_router

api_router = APIRouter()

# Inclui os roteadores dos controladores
api_router.include_router(insurance_router)
api_router.include_router(retirement_router)
