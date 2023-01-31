from pydantic import BaseModel

#Modelo para los clicks
class ClickBase(BaseModel):
    ip: str | None = None
    browser: str | None = None

class ClickCreate(ClickBase):
    pass

class Click(ClickBase):
    id: int
    owner_id: int
    geo: str  | None = None

    class Config:
        orm_mode = True


# Modelo para los Links

class LinkBase(BaseModel):
    email: str

class LinkCreate(LinkBase):
    url: str

class Link(LinkBase):

    id: int | None
    title: str | None
    url: str | None
    fake_url: str| None
    type: str | None
    description: str | None
    image: str | None
    site_name: str | None
    

    is_active: bool = True
    clicks: list[Click] = []

    class Config:
        orm_mode = True
    