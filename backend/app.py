from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import save_chat, get_chats
from chatbot import ask_bot

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend working"}

@app.get("/chat")
def chat(msg: str):

    answer = ask_bot(msg)

    save_chat(
        msg,
        answer
    )

    return {
        "response": answer
    }

@app.get("/history")
def history():

    chats = get_chats()

    return {
        "history": chats
    }