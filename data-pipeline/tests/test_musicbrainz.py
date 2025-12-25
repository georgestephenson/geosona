"""Tests for MusicBrainz extractor."""

import pytest
from unittest.mock import patch, MagicMock
from extractors.musicbrainz import MusicBrainzExtractor
from models.artist import Artist


class TestMusicBrainzExtractor:
    """Test MusicBrainzExtractor class."""

    def test_init(self):
        """Test extractor initialization."""
        extractor = MusicBrainzExtractor()
        assert extractor.rate_limit > 0

    @patch("extractors.musicbrainz.mb.search_artists")
    def test_search_artists_success(
        self, mock_search, mock_musicbrainz_response, sample_artist_list
    ):
        """Test successful artist search."""
        mock_search.return_value = mock_musicbrainz_response

        extractor = MusicBrainzExtractor()
        artists = extractor.search_artists("country:GB", limit=2)

        assert len(artists) == 2
        assert all(isinstance(artist, Artist) for artist in artists)
        assert artists[0].name == "Radiohead"
        assert artists[0].country == "GB"
        assert artists[1].name == "The Beatles"

    @patch("extractors.musicbrainz.mb.search_artists")
    def test_search_artists_empty_result(self, mock_search):
        """Test search with no results."""
        mock_search.return_value = {"artist-list": []}

        extractor = MusicBrainzExtractor()
        artists = extractor.search_artists("nonexistent", limit=10)

        assert len(artists) == 0

    @patch("extractors.musicbrainz.mb.search_artists")
    def test_search_artists_api_error(self, mock_search):
        """Test handling of API errors."""
        mock_search.side_effect = Exception("API Error")

        extractor = MusicBrainzExtractor()
        artists = extractor.search_artists("country:GB", limit=10)

        assert len(artists) == 0

    @patch("extractors.musicbrainz.mb.get_artist_by_id")
    def test_get_artist_by_id_success(self, mock_get, sample_artist_data):
        """Test getting artist by ID."""
        mock_get.return_value = {"artist": sample_artist_data}

        extractor = MusicBrainzExtractor()
        artist = extractor.get_artist_by_id("a74b1b7f-71a5-4011-9441-d0b5e4122711")

        assert artist is not None
        assert isinstance(artist, Artist)
        assert artist.name == "Radiohead"
        assert artist.mbid == "a74b1b7f-71a5-4011-9441-d0b5e4122711"

    @patch("extractors.musicbrainz.mb.get_artist_by_id")
    def test_get_artist_by_id_error(self, mock_get):
        """Test error handling when getting artist by ID."""
        mock_get.side_effect = Exception("Not found")

        extractor = MusicBrainzExtractor()
        artist = extractor.get_artist_by_id("invalid-id")

        assert artist is None

    def test_parse_artist(self, sample_artist_data):
        """Test parsing artist data."""
        extractor = MusicBrainzExtractor()
        artist = extractor._parse_artist(sample_artist_data)

        assert artist is not None
        assert artist.name == "Radiohead"
        assert artist.mbid == "a74b1b7f-71a5-4011-9441-d0b5e4122711"
        assert artist.country == "GB"
        assert artist.type == "Group"
        assert artist.begin_area == "Oxford"

    @patch("extractors.musicbrainz.mb.search_artists")
    @patch("extractors.musicbrainz.time.sleep")
    def test_rate_limiting(self, mock_sleep, mock_search, mock_musicbrainz_response):
        """Test that rate limiting is applied."""
        mock_search.return_value = mock_musicbrainz_response

        extractor = MusicBrainzExtractor()
        extractor.search_artists("country:GB", limit=2)

        # Should sleep after the first batch
        mock_sleep.assert_called()

    @patch("extractors.musicbrainz.mb.search_artists")
    def test_pagination(self, mock_search):
        """Test pagination with multiple batches."""
        # First call returns 100 results, second call returns empty
        mock_search.side_effect = [
            {
                "artist-list": [
                    {"id": f"id-{i}", "name": f"Artist {i}"} for i in range(100)
                ]
            },
            {"artist-list": []},
        ]

        extractor = MusicBrainzExtractor()
        artists = extractor.search_artists("country:GB", limit=150)

        # Should get 100 results (stopped when second batch was empty)
        assert len(artists) == 100
        assert mock_search.call_count == 2
