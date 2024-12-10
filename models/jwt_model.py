from typing import Optional

from pydantic import BaseModel, Field, field_validator


class JWT(BaseModel):
    access_token: str = Field(strict=True)
    refresh_token: str = Field(strict=True)