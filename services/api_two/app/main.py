from fastapi import FastAPI

app = FastAPI(title="api_two")


@app.get("/users")
async def get_users():
    """Return a simple list of users."""
    return [{"id": 1, "username": "alice"}, {"id": 2, "username": "bob"}]


@app.get("/health")
async def health():
    return {"status": "ok", "service": "api_two"}
