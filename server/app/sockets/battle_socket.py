import socketio
from typing import Dict

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")


# Стандартна подія підключення
@sio.event
async def connect(sid, environ):
    print(f"✅ Socket connected: {sid}")


@sio.event
async def disconnect(sid):
    print(f"❌ Socket disconnected: {sid}")


@sio.event
async def submit_code(sid, data: Dict[str, str]):
    code = data.get("code", "")
    print(f"📥 Received code:\n{code}")

    # Фейковий результат бою для MVP
    result = "👊 Симуляція: атаковано ворога, знято 10 HP з першого юніта!"

    # Надсилаємо назад гравцю
    await sio.emit("battle_result", result, to=sid)
