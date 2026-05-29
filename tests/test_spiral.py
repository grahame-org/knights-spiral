"""Tests for the spiral coordinate mapping."""

import pytest
from hamcrest import assert_that, equal_to

from knights_spiral.spiral import cell_id_to_xy, build_spiral_lookup


class TestCellIdToXy:
    """Tests for cell_id_to_xy based on example 1 from the spec.

    Example grid (5x5 centered at cell 0):
        12 11 10  9 24
        13  2  1  8 23
        14  3  0  7 22
        15  4  5  6 21
        16 17 18 19 20
    """

    @pytest.mark.parametrize(
        "cell_id, expected_xy",
        [
            (0, (0, 0)),
            (1, (0, -1)),
            (2, (-1, -1)),
            (3, (-1, 0)),
            (4, (-1, 1)),
            (5, (0, 1)),
            (6, (1, 1)),
            (7, (1, 0)),
            (8, (1, -1)),
            (9, (1, -2)),
            (10, (0, -2)),
            (11, (-1, -2)),
            (12, (-2, -2)),
            (13, (-2, -1)),
            (14, (-2, 0)),
            (15, (-2, 1)),
            (16, (-2, 2)),
            (17, (-1, 2)),
            (18, (0, 2)),
            (19, (1, 2)),
            (20, (2, 2)),
            (21, (2, 1)),
            (22, (2, 0)),
            (23, (2, -1)),
            (24, (2, -2)),
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
