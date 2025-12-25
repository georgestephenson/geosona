"""Tests for data models."""

import pytest
from pydantic import ValidationError
from models.artist import Artist


class TestArtistModel:
    """Test Artist model."""

    def test_artist_creation_minimal(self):
        """Test creating artist with minimal required fields."""
        artist = Artist(mbid="test-id", name="Test Artist")

        assert artist.mbid == "test-id"
        assert artist.name == "Test Artist"
        assert artist.sort_name is None
        assert artist.type is None
        assert artist.country is None

    def test_artist_creation_full(self):
        """Test creating artist with all fields."""
        artist = Artist(
            mbid="a74b1b7f-71a5-4011-9441-d0b5e4122711",
            name="Radiohead",
            sort_name="Radiohead",
            type="Group",
            country="GB",
            begin_area="Oxford",
            disambiguation="English alternative rock band",
        )

        assert artist.mbid == "a74b1b7f-71a5-4011-9441-d0b5e4122711"
        assert artist.name == "Radiohead"
        assert artist.country == "GB"
        assert artist.type == "Group"

    def test_artist_missing_required_fields(self):
        """Test that missing required fields raise validation error."""
        with pytest.raises(ValidationError):
            Artist(name="Test")  # type: ignore[call-arg]  # Missing mbid - intentional for test

        with pytest.raises(ValidationError):
            Artist(mbid="test-id")  # type: ignore[call-arg]  # Missing name - intentional for test

    def test_artist_immutability(self):
        """Test that artist instances are immutable (frozen)."""
        artist = Artist(mbid="test-id", name="Test Artist")

        with pytest.raises(ValidationError):
            artist.name = "New Name"

    def test_artist_serialization(self):
        """Test artist model serialization."""
        artist = Artist(
            mbid="test-id",
            name="Test Artist",
            country="US",
        )

        data = artist.model_dump()
        assert data["mbid"] == "test-id"
        assert data["name"] == "Test Artist"
        assert data["country"] == "US"
        assert "sort_name" in data
