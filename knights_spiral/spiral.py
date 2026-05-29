"""Spiral coordinate mapping: cell ID <-> (x, y) grid coordinates.

The spiral starts at (0, 0) with cell ID 0 and expands counter-clockwise:
    right, up, left, down
with step counts: 1, 1, 2, 2, 3, 3, 4, 4, ...
"""

from typing import Generator

# Direction vectors: right, up, left, down (counter-clockwise)
_DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

# ---------------------------------------------------------------------------
# Lazy coordinate cache backed by a generator.
#
# _spiral_coords[i] holds the (x, y) for cell ID i.  The generator yields
# successive coordinates starting from cell ID 1; the cache grows on demand
# so every new coordinate is computed in O(1), giving O(N) total cost
# (instead of the O(N²) cost of recomputing from scratch on each call).
# ---------------------------------------------------------------------------


def _spiral_generator() -> Generator[tuple[int, int], None, None]:
    """Yield (x, y) for cell IDs 1, 2, 3, … in spiral order."""
    x, y = 0, 0
    direction_index = 0
    steps = 1
    while True:
        for _ in range(2):
            dx, dy = _DIRECTIONS[direction_index % 4]
            for _ in range(steps):
                x += dx
                y += dy
                yield (x, y)
            direction_index += 1
        steps += 1


_spiral_coords: list[tuple[int, int]] = [(0, 0)]
_spiral_gen = _spiral_generator()


def _extend_spiral(target_id: int) -> None:
    """Grow _spiral_coords until it contains target_id."""
    while len(_spiral_coords) <= target_id:
        _spiral_coords.append(next(_spiral_gen))


def cell_id_to_xy(cell_id: int) -> tuple[int, int]:
    """Convert a spiral cell ID to (x, y) grid coordinates."""
    if cell_id >= len(_spiral_coords):
        _extend_spiral(cell_id)
    return _spiral_coords[cell_id]


def build_spiral_lookup(max_id: int) -> list[tuple[int, int]]:
    """Build a list mapping cell IDs to (x, y) coordinates up to max_id."""
    if max_id >= len(_spiral_coords):
        _extend_spiral(max_id)
    return list(_spiral_coords[: max_id + 1])
