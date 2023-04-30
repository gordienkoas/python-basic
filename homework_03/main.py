import uvicorn
from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/ping/")
async def root():
    return JSONResponse(status_code=200, content={"message": "pong"})

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


