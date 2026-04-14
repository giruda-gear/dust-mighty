from fastapi import FastAPI

from app.routers import auth, activity, category


app = FastAPI(title="Dust Mighty")

app.include_router(auth.router)
app.include_router(activity.router)
app.include_router(category.router)


@app.get("/health")
async def health_check() -> dict:
    return {"status": "ok"}
