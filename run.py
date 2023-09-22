import logging, uvicorn
logging.basicConfig(level=logging.INFO)

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/")uto
async def giveResponse():
    return StreamingResponse()

uvicorn.run(app)