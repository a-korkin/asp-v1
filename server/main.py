import uvicorn
from api import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(app="main:app", port=5000, reload=True)
