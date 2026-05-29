"""Spiral coordinate mapping: cell ID <-> (x, y) grid coordinates.

The spiral starts at (0, 0) with cell ID 0 and expands counter-clockwise:
    right, up, left, down
with step counts: 1, 1, 2, 2, 3, 3, 4, 4, ...
"""

# Direction vectors: right, up, left, down (counter-clockwise)
_DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def cell_id_to_xy(cell_id: int) -> tuple[int, int]:
    """Convert a spiral cell ID to (x, y) grid coordinates."""
    x, y = 0, 0
    current_id = 0
    direction_index = 0
    steps = 1

    while current_id < cell_id:
        for _ in range(2):
            dx, dy = _DIRECTIONS[direction_index % 4]
            for _ in range(steps):
                if current_id == cell_id:
                    return (x, y)
                x += dx
                y += dy
                current_id += 1
            direction_index += 1
        steps += 1

    return (x, y)


def build_spiral_lookup(max_id: int) -> list[tuple[int, int]]:
    """Build a list mapping cell IDs to (x, y) coordinates up to max_id."""
    coords = [(0, 0)] * (max_id + 1)
    x, y = 0, 0
    current_id = 0
    coords[0] = (0, 0)
    direction_index = 0
    steps = 1

    while current_id < max_id:
        for _ in range(2):
            dx, dy = _DIRECTIONS[direction_index % 4]
            for _ in range(steps):
                if current_id >= max_id:
                    return coords
                x += dx
                y += dy
                current_id += 1
                coords[current_id] = (x, y)
            direction_index += 1
        steps += 1

    return coords
