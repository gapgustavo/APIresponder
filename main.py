from fastapi import FastAPI

app = FastAPI()

@app.post("/instagram-message/")
async def receive_instagram_message(data: dict):
    return {"data": data}