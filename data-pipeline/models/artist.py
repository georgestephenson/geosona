"""Data models for artists."""

from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class Artist(BaseModel):
    """Artist data model."""

    model_config = ConfigDict(frozen=True)

    mbid: str = Field(..., description="MusicBrainz ID")
    name: str = Field(..., description="Artist name")
    sort_name: Optional[str] = Field(default=None, description="Sort name")
    type: Optional[str] = Field(
        default=None, description="Artist type (Person, Group, etc.)"
    )
    country: Optional[str] = Field(default=None, description="Country code")
    begin_area: Optional[str] = Field(default=None, description="Place of origin")
    disambiguation: Optional[str] = Field(default=None, description="Disambiguation")
