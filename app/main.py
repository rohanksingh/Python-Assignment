from fastapi import FastAPI
from app.views import addition_view

app = FastAPI()

app.include_router(addition_view.router, prefix="/additions", tags=["additions"])
