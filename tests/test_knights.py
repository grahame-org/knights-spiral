"""Tests for the knight placement algorithm."""

from hamcrest import assert_that, equal_to, has_key, has_length, is_not

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
        assert_that(occupied, has_key((0, 0)))

    def test_five_knights_match_example_2(self):
        """Verify against example 2 from the spec.

        Expected knights at cell IDs: 0, 1, 2, 3, 20
        Corresponding coords: (0,0), (1,0), (1,-1), (0,-1), (-2,2)
        """
        occupied = place_knights(5)
        assert_that(occupied, has_length(5))
        expected_coords = {(0, 0), (1, 0), (1, -1), (0, -1), (-2, 2)}
        assert_that(set(occupied.keys()), equal_to(expected_coords))

    def test_no_two_knights_attack_each_other(self):
        occupied = place_knights(10)
        occupied_list = list(occupied.keys())
        for i, (x1, y1) in enumerate(occupied_list):
            targets = set(get_knight_targets(x1, y1))
            for j, pos in enumerate(occupied_list):
                if i != j:
                    assert pos not in targets, (
                        f"Knight at {(x1, y1)} attacks knight at {pos}"
                    )


class TestPlaceKnightsMultiColour:

    def test_two_colours_first_at_origin(self):
        occupied = place_knights(1, num_colours=2)
        assert_that(occupied, has_length(1))
        assert_that(occupied[(0, 0)], equal_to(0))

    def test_two_colours_alternates(self):
        occupied = place_knights(4, num_colours=2)
        assert_that(occupied, has_length(4))
        colour_counts = [0, 0]
        for colour in occupied.values():
            colour_counts[colour] += 1
        assert_that(colour_counts[0], equal_to(2))
        assert_that(colour_counts[1], equal_to(2))

    def test_two_colours_no_cross_colour_attacks(self):
        """No knight should be a knight's move from a different colour."""
        occupied = place_knights(10, num_colours=2)
        for (x, y), colour in occupied.items():
            for target in get_knight_targets(x, y):
                if target in occupied:
                    assert_that(
                        occupied[target],
                        equal_to(colour),
                        f"Knight at {(x, y)} (colour {colour}) attacks "
                        f"knight at {target} (colour {occupied[target]})",
                    )

    def test_single_colour_backward_compatible(self):
        """Single colour uses original rules: no two knights attack."""
        occupied = place_knights(5, num_colours=1)
        assert_that(occupied, has_length(5))
        expected_coords = {(0, 0), (1, 0), (1, -1), (0, -1), (-2, 2)}
        assert_that(set(occupied.keys()), equal_to(expected_coords))
        for colour in occupied.values():
            assert_that(colour, equal_to(0))
