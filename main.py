from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def verify_webhook(request: Request):
    mode = request.query_params.get("hub.mode")
    challenge = request.query_params.get("hub.challenge")
    verify_token = request.query_params.get("hub.verify_token")

    if mode == "subscribe" and verify_token == "2021":
        return challenge
    else:
        return {"message": "Invalid verification request"}

@app.post("/instagram-message/")
async def receive_instagram_message(data: dict):
    print (data)
    return {"status": 200}
