from fastapi import FastAPI

app = FastAPI(title="Dust Mighty")


@app.get("/health")
async def health_check() -> dict:
    return {"status": "ok"}
