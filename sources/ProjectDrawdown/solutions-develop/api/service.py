import json
import glob
import uvicorn
import time

from typing import Optional
from fastapi import Depends, FastAPI, Header, HTTPException, Request
from pydantic import BaseModel
from fastapi_plugins import redis_plugin
from fastapi.middleware.cors import CORSMiddleware

import solution.factory
from api.config import get_settings, RedisSettings
from api import config

settings = get_settings()
origins = ["http://localhost:3000", settings.client_url]

from api.routers.routes import (
    account,
    user,
    workbook,
    resource,
    vma,
    projection
)

with open('./api/docs.html', 'r') as f:
    docs = f.read()

app = FastAPI(
        title="Drawdown API",
        description=docs,
        version="1.0"
        )

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(account.router)
app.include_router(user.router)
app.include_router(workbook.router)
app.include_router(resource.router)
app.include_router(vma.router)
app.include_router(projection.router)

config.app = app

redis_config = RedisSettings()

@app.on_event('startup')
async def on_startup() -> None:
    await redis_plugin.init_app(app, config=redis_config)
    await redis_plugin.init()

@app.on_event('shutdown')
async def on_shutdown() -> None:
    await redis_plugin.terminate()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# For Debugging
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
