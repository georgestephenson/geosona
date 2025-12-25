"""Pytest fixtures for data-pipeline tests."""

import pytest
from unittest.mock import Mock


@pytest.fixture
def sample_artist_data():
    """Sample MusicBrainz artist data."""
    return {
        "id": "a74b1b7f-71a5-4011-9441-d0b5e4122711",
        "name": "Radiohead",
        "sort-name": "Radiohead",
        "type": "Group",
        "country": "GB",
        "begin-area": {"name": "Oxford"},
        "disambiguation": "English alternative rock band",
    }


@pytest.fixture
def sample_artist_list():
    """Sample list of artist data."""
    return [
        {
            "id": "a74b1b7f-71a5-4011-9441-d0b5e4122711",
            "name": "Radiohead",
            "sort-name": "Radiohead",
            "type": "Group",
            "country": "GB",
            "begin-area": {"name": "Oxford"},
        },
        {
            "id": "b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d",
            "name": "The Beatles",
            "sort-name": "Beatles, The",
            "type": "Group",
            "country": "GB",
            "begin-area": {"name": "Liverpool"},
        },
    ]


@pytest.fixture
def mock_musicbrainz_response(sample_artist_list):
    """Mock MusicBrainz API response."""
    return {"artist-list": sample_artist_list, "artist-count": 2}
