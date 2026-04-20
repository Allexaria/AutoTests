from pydantic import BaseModel


class AuthResponse(BaseModel):
    responseCode: int
    message: str


class CreateAccountResponse(BaseModel):
    responseCode: int
    message: str


class DeleteAccountResponse(BaseModel):
    responseCode: int
    message: str
