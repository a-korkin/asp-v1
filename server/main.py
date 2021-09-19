import uvicorn
from auth import routers
from fastapi import FastAPI

app = FastAPI()

app.include_router(routers.router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", port=5000, reload=True)
