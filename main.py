from fastapi import FastAPI
from api.handlers import login_handlers, user_handlers
from api.handlers import task_handlers
from database.db_setup import engine
from models import task_models, user_models

user_models.Base.metadata.create_all(bind=engine)
task_models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="API Enxerto-Agro",
    description="API para o teste técnico da empresa Enxerto Agro.",
    version="0.0.1",
    contact={
        "name": "Lucca Haddad",
    },
)


app.include_router(user_handlers.router)
app.include_router(task_handlers.router)
app.include_router(login_handlers.router)
