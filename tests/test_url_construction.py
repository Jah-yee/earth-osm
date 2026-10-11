"""Deterministic tests for URL construction in gfk_download.

These tests do NOT require network access and are not marked as integration.
They verify that _build_versioned_url correctly constructs URLs from base + filename.
"""

from earth_osm.gfk_download import _build_versioned_url


def test_build_versioned_url_with_filename():
    """_build_versioned_url appends remote filename to base URL."""
    result = _build_versioned_url(
        "https://download.geofabrik.de/africa/", "nigeria.html"
    )
    assert result == "https://download.geofabrik.de/africa/nigeria.html"


def test_build_versioned_url_with_none_filename():
    """_build_versioned_url returns base URL unchanged when filename is None."""
    result = _build_versioned_url(
        "https://download.geofabrik.de/africa/", None
    )
    assert result == "https://download.geofabrik.de/africa/"


def test_build_versioned_url_strips_trailing_slash():
    """_build_versioned_url handles base URL without trailing slash."""
    result = _build_versioned_url(
        "https://download.geofabrik.de/africa", "nigeria.html"
    )
    assert result == "https://download.geofabrik.de/africa/nigeria.html"
