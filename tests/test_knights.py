"""Tests for the knight placement algorithm."""

import pytest
from hamcrest import assert_that, equal_to, has_item, has_length, is_not

from knights_spiral.knights import place_knights, get_knight_targets


class TestGetKnightTargets:

    def test_returns_eight_targets(self):
        targets = get_knight_targets(0, 0)
        assert_that(targets, has_length(8))

    def test_targets_from_origin(self):
        targets = set(get_knight_targets(0, 0))
        expected = {
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1),
        }
        assert_that(targets, equal_to(expected))


class TestPlaceKnights:

    def test_one_knight_placed_at_origin(self):
        occupied = place_knights(1)
        assert_that(occupied, has_length(1))
        assert_that(occupied, has_item((0, 0)))

    def test_five_knights_match_example_2(self):
        """Verify against example 2 from the spec.

        Expected knights at cell IDs: 0, 1, 2, 3, 20
        Corresponding coords: (0,0), (1,0), (1,-1), (0,-1), (-2,2)
        """
        occupied = place_knights(5)
        assert_that(occupied, has_length(5))
        expected_coords = {(0, 0), (1, 0), (1, -1), (0, -1), (-2, 2)}
        assert_that(occupied, equal_to(expected_coords))

    def test_no_two_knights_attack_each_other(self):
        occupied = place_knights(10)
        occupied_list = list(occupied)
        for i, (x1, y1) in enumerate(occupied_list):
            targets = set(get_knight_targets(x1, y1))
            for j, pos in enumerate(occupied_list):
                if i != j:
                    assert_that(
                        targets,
                        is_not(has_item(pos)),
                        f"Knight at {(x1, y1)} attacks knight at {pos}",
                    )
