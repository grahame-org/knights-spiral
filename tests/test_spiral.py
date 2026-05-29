"""Tests for the spiral coordinate mapping."""

import pytest
from hamcrest import assert_that, equal_to

from knights_spiral.spiral import cell_id_to_xy, build_spiral_lookup


class TestCellIdToXy:
    """Tests for cell_id_to_xy based on example 1 from the spec.

    Example grid (5x5 centered at cell 0):
        16 15 14 13 12
        17  4  3  2 11
        18  5  0  1 10
        19  6  7  8  9
        20 21 22 23 24
    """

    @pytest.mark.parametrize(
        "cell_id, expected_xy",
        [
            (0, (0, 0)),
            (1, (1, 0)),
            (2, (1, -1)),
            (3, (0, -1)),
            (4, (-1, -1)),
            (5, (-1, 0)),
            (6, (-1, 1)),
            (7, (0, 1)),
            (8, (1, 1)),
            (9, (2, 1)),
            (10, (2, 0)),
            (11, (2, -1)),
            (12, (2, -2)),
            (13, (1, -2)),
            (14, (0, -2)),
            (15, (-1, -2)),
            (16, (-2, -2)),
            (17, (-2, -1)),
            (18, (-2, 0)),
            (19, (-2, 1)),
            (20, (-2, 2)),
            (21, (-1, 2)),
            (22, (0, 2)),
            (23, (1, 2)),
            (24, (2, 2)),
        ],
    )
    def test_cell_id_maps_to_expected_coordinates(self, cell_id, expected_xy):
        assert_that(cell_id_to_xy(cell_id), equal_to(expected_xy))


class TestBuildSpiralLookup:

    def test_lookup_matches_cell_id_to_xy(self):
        lookup = build_spiral_lookup(24)
        for cell_id in range(25):
            assert_that(
                lookup[cell_id],
                equal_to(cell_id_to_xy(cell_id)),
                f"Mismatch at cell_id={cell_id}",
            )
