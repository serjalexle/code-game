from pydantic import BaseModel


class LoginDto(BaseModel):
    login: str
    password: str


class RegisterDto(BaseModel):
    login: str
    password: str

