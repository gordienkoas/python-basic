import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return {
        "message": "pong",
    }


@app.get("/")
def index():
    return {
        "message": "Index",
    }


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        reload=True,
    )
