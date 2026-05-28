from datetime import datetime

from pydantic import BaseModel, EmailStr


class WebhookResponse(BaseModel):
    event_id: str
    card_id: str
    timestamp: datetime
    
class WebhookPublic(WebhookResponse):
    cliente_email: EmailStr



class WebhookList(BaseModel):
    webhooks: list[WebhookResponse]
