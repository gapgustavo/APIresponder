from fastapi import FastAPI, HTTPException, Request

app = FastAPI()


VERIFY_TOKEN = "2021"

@app.get("/")
async def messaging_webhook(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")
    challenge_dict = {"value": challenge}

    if mode and token:
        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("WEBHOOK_VERIFIED")
            return challenge_dict
        else:
            raise HTTPException(status_code=403, detail="Forbidden")
    else:
        raise HTTPException(status_code=400, detail="Bad Request")
    
@app.post("/instagram-message/")
async def receive_instagram_message(data: dict):
    print (data)
    return {"status": 200}
