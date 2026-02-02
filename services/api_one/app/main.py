from fastapi import FastAPI

app = FastAPI(title="api_one")


@app.get("/items")
async def get_items():
    """Return a simple list of items."""
    return [{"id": 1, "name": "Item A"}, {"id": 2, "name": "Item B"}]


@app.get("/health")
async def health():
    return {"status": "ok", "service": "api_one"}
