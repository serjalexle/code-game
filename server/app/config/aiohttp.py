from aiohttp import ClientSession
from fastapi import FastAPI


bitrix_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}


def init_aiohttp_session(app: FastAPI):

    app.state.aiohttp_bitrix_session = ClientSession(
        headers=bitrix_headers,
    )


def close_aiohttp_session(app: FastAPI):
    app.state.aiohttp_bitrix_session.close()
