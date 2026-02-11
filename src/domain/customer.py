from dataclasses import dataclass
from datetime import datetime

@dataclass
class Customer:
    id: int
    email: str
    name: str
    is_active: bool
    created_at: datetime
