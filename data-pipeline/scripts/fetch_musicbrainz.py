#!/usr/bin/env python3
"""Fetch artist data from MusicBrainz API."""

import argparse
from extractors.musicbrainz import MusicBrainzExtractor
from utils.logger import logger
from config.settings import settings


def main():
    """Main entry point for fetching MusicBrainz data."""
    parser = argparse.ArgumentParser(description="Fetch artists from MusicBrainz")
    parser.add_argument(
        "--query",
        type=str,
        default="country:GB AND type:group",
        help="MusicBrainz search query",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=settings.max_artists,
        help="Maximum number of artists to fetch",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Optional JSON output file",
    )

    args = parser.parse_args()

    logger.info("starting_fetch", query=args.query, limit=args.limit)

    # Extract artists
    extractor = MusicBrainzExtractor()
    artists = extractor.search_artists(query=args.query, limit=args.limit)

    logger.info("fetch_complete", count=len(artists))

    # Optional: Save to file
    if args.output:
        import json

        with open(args.output, "w") as f:
            json.dump(
                [artist.model_dump() for artist in artists], f, indent=2, default=str
            )
        logger.info("saved_to_file", path=args.output)

    # Print sample
    if artists:
        logger.info("sample_artist", artist=artists[0].model_dump())


if __name__ == "__main__":
    main()
