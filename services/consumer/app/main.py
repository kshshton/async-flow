import asyncio

import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI(title="consumer_app")

API_ONE = "http://api_one:8001"
API_TWO = "http://api_two:8002"


async def fetch(client: httpx.AsyncClient, url: str):
    resp = await client.get(url, timeout=5.0)
    resp.raise_for_status()
    return resp.json()


@app.get("/aggregate")
async def aggregate():
    """Asynchronously fetch data from both APIs and return combined JSON."""
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(
            fetch(client, f"{API_ONE}/items"),
            fetch(client, f"{API_TWO}/users"),
            return_exceptions=True,
        )

    items, users = results
    if isinstance(items, Exception) or isinstance(users, Exception):
        raise HTTPException(status_code=502, detail="Upstream service error")

    return {"items": items, "users": users}
