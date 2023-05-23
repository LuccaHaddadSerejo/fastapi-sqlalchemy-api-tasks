from fastapi import FastAPI

app = FastAPI(
    title="API Enxerto-Agro",
    description="API para o teste técnico da empresa Enxerto Agro.",
    version="0.0.1",
    contact={
        "name": "Lucca Haddad",
    },
    license_info={
        "name": "MIT",
    },
)

# app.include_router(users.router)
# app.include_router(courses.router)
# app.include_router(sections.router)
