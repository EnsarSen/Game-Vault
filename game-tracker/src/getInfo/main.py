from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

client_id = os.getenv("IDGB_CLIENT_ID")
client_secret = os.getenv("IDGB_CLIENT_SECRET")

app = FastAPI()


origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/token")
def get_token():
    token = requests.post(
        f"https://id.twitch.tv/oauth2/token?client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials"
    )

    return token.json()


@app.get("/games")
def get_games():
    pytoken = get_token()

    bearer = pytoken["token_type"]
    headers = {
        "Client-ID": client_id,
        "Authorization": f"{bearer} {pytoken["access_token"]}",
    }

    url = "https://api.igdb.com/v4/games/"

    games = requests.post(url, headers=headers, data='search "Persona"; fields name;')

    return games.json()
