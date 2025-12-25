"""MusicBrainz API client for extracting artist data."""

import musicbrainzngs as mb
import time
from typing import List, Optional
from models.artist import Artist
from utils.logger import logger
from config.settings import settings

# Read version from package metadata
try:
    from importlib.metadata import version

    __version__ = version("geosona-pipeline")
except Exception:
    __version__ = "0.1.0"  # Fallback


class MusicBrainzExtractor:
    """Extract artist data from MusicBrainz API."""

    def __init__(self):
        """Initialize the MusicBrainz client."""
        mb.set_useragent(
            app="geosona-pipeline",
            version=__version__,
            contact="https://github.com/georgestephenson/geosona",
        )
        self.rate_limit = settings.musicbrainz_rate_limit

    def search_artists(self, query: str, limit: int = 100) -> List[Artist]:
        """
        Search for artists by name or other criteria.

        Args:
            query: Search query (e.g., 'country:GB AND type:group')
            limit: Maximum number of results

        Returns:
            List of Artist objects
        """
        artists = []
        offset = 0
        batch_size = min(100, limit)  # MusicBrainz max is 100 per request

        logger.info("searching_musicbrainz", query=query, limit=limit)

        while len(artists) < limit:
            try:
                result = mb.search_artists(query=query, limit=batch_size, offset=offset)

                if not result.get("artist-list"):
                    break

                for artist_data in result["artist-list"]:
                    artist = self._parse_artist(artist_data)
                    if artist:
                        artists.append(artist)

                    if len(artists) >= limit:
                        break

                offset += batch_size
                time.sleep(self.rate_limit)  # Respect rate limit

            except Exception as e:
                logger.error("musicbrainz_error", error=str(e), offset=offset)
                break

        logger.info("artists_extracted", count=len(artists))
        return artists

    def get_artist_by_id(self, mbid: str) -> Optional[Artist]:
        """
        Get detailed artist information by MusicBrainz ID.

        Args:
            mbid: MusicBrainz ID

        Returns:
            Artist object or None
        """
        try:
            result = mb.get_artist_by_id(mbid, includes=["url-rels", "area-rels"])
            return self._parse_artist(result["artist"])
        except Exception as e:
            logger.error("artist_fetch_error", mbid=mbid, error=str(e))
            return None

    def _parse_artist(self, data: dict) -> Optional[Artist]:
        """Parse raw MusicBrainz artist data into Artist model."""
        try:
            return Artist(
                mbid=data["id"],
                name=data.get("name", ""),
                sort_name=data.get("sort-name"),
                type=data.get("type"),
                country=data.get("country"),
                begin_area=data.get("begin-area", {}).get("name"),
                disambiguation=data.get("disambiguation"),
            )
        except Exception as e:
            logger.warning("parse_error", error=str(e), data=data)
            return None
