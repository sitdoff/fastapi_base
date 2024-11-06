from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    foo: str
    bar: str


class UserCreate(UserBase):
    pass


class UserOut(UserBase):
    id: int
