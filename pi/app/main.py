from fastapi import FastAPI
import uvicorn

from .faces.router import router

app = FastAPI()


@app.get("/healthcheck/")
def healthcheck():
    return 'Health - OK'


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)


