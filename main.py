from fastapi import FastAPI

app = FastAPI()




@app.get("/")
async def home():
    return {"status": 200}


@app.post("/instagram-message/")
async def receive_instagram_message(data: dict):
    print (data)
    return {"status": 200}
