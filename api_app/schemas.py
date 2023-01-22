from pydantic import BaseModel

class ClickBase(BaseModel):
    ip: str
    browser: str | None = None

class ClickCreate(ClickBase):
    geo: str 

class Click(ClickBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class LinkBase(BaseModel):
    email: str

class LinkCreate(LinkBase):
    url: str

class Link(LinkBase):
    id: int
    is_active: bool
    clicks: list[Click] = []

    class Config:
        orm_mode = True
    