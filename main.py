from fastapi import FastAPI
from api import user_endpoints, task_endpoints
from database.db_setup import engine
from database.models import user_model

user_model.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="API Enxerto-Agro",
    description="API para o teste técnico da empresa Enxerto Agro.",
    version="0.0.1",
    contact={
        "name": "Lucca Haddad",
    },
)


app.include_router(user_endpoints.router)
app.include_router(task_endpoints.router)
