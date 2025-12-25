"""Integration tests for MusicBrainz extractor (requires network)."""

import pytest
from extractors.musicbrainz import MusicBrainzExtractor


@pytest.mark.integration
class TestMusicBrainzIntegration:
    """Integration tests that make real API calls.

    These tests are skipped by default. Run with: pytest -m integration
    """

    def test_search_real_artist(self):
        """Test searching for a real artist (Radiohead)."""
        extractor = MusicBrainzExtractor()
        artists = extractor.search_artists("artist:Radiohead", limit=3)

        assert len(artists) > 0
        # Check that we got Radiohead
        names = [artist.name for artist in artists]
        assert "Radiohead" in names

    def test_get_radiohead_by_id(self):
        """Test getting Radiohead by their MBID."""
        extractor = MusicBrainzExtractor()
        artist = extractor.get_artist_by_id("a74b1b7f-71a5-4011-9441-d0b5e4122711")

        assert artist is not None
        assert artist.name == "Radiohead"
        assert artist.country == "GB"
        assert artist.type == "Group"

    def test_search_by_country(self):
        """Test searching artists by country."""
        extractor = MusicBrainzExtractor()
        artists = extractor.search_artists("country:GB AND type:group", limit=5)

        assert len(artists) > 0
        # All should be from GB
        for artist in artists:
            if artist.country:  # Some might not have country set
                assert artist.country == "GB"
