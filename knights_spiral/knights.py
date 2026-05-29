"""Knight placement algorithm for the knight's spiral."""

from knights_spiral.spiral import cell_id_to_xy

# All 8 possible knight move offsets
KNIGHT_MOVES = [
    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
    (1, -2), (1, 2), (2, -1), (2, 1),
]


def get_knight_targets(x: int, y: int) -> list[tuple[int, int]]:
    """Return all squares a knight at (x, y) can move to."""
    return [(x + dx, y + dy) for dx, dy in KNIGHT_MOVES]


def place_knights(iterations: int) -> set[tuple[int, int]]:
    """Place `iterations` knights according to the spiral rules.

    Returns the set of (x, y) coordinates where knights are placed.
    """
    occupied: set[tuple[int, int]] = set()
    attacked: set[tuple[int, int]] = set()
    placed = 0
    cell_id = 0

    while placed < iterations:
        xy = cell_id_to_xy(cell_id)
        if xy not in occupied and xy not in attacked:
            occupied.add(xy)
            for target in get_knight_targets(*xy):
                attacked.add(target)
            placed += 1
        cell_id += 1

    return occupied
