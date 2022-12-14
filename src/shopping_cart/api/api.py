from fastapi import APIRouter

from shopping_cart.api.endpoints import login, products, users

api_router = APIRouter()

api_router.include_router(login.router, prefix='/login', tags=['login'])
api_router.include_router(users.router, prefix='/users', tags=['users'])
api_router.include_router(products.router, prefix='/products', tags=['products'])
