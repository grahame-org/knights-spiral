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


def place_knights(
    iterations: int, num_colours: int = 1
) -> dict[tuple[int, int], int]:
    """Place `iterations` knights according to the spiral rules.

    Args:
        iterations: Total number of knights to place.
        num_colours: Number of distinct knight colours (0-indexed internally).
            Must be >= 1.

    Returns a dict mapping (x, y) coordinates to colour index (0-based).
    A cell is blocked for a colour if it is a knight's move away from
    a cell occupied by a *different* colour.  When ``num_colours == 1``
    the original rules apply: a cell is also blocked by a same-colour
    (i.e. any) occupant.
    """
    if num_colours < 1:
        raise ValueError(f"num_colours must be >= 1, got {num_colours}")
    occupied: dict[tuple[int, int], int] = {}
    # attacked_by[colour] = set of cells attacked by that colour
    attacked_by: list[set[tuple[int, int]]] = [set() for _ in range(num_colours)]
    placed = 0
    cell_id = 0

    while placed < iterations:
        colour = placed % num_colours
        xy = cell_id_to_xy(cell_id)
        if xy not in occupied:
            if num_colours == 1:
                # Original rules: no knight may be a knight's move
                # from any other knight.
                blocked = xy in attacked_by[0]
            else:
                # Multi-colour rules: only *different* colours block.
                blocked = any(
                    xy in attacked_by[c]
                    for c in range(num_colours)
                    if c != colour
                )
            if not blocked:
                occupied[xy] = colour
                for target in get_knight_targets(*xy):
                    attacked_by[colour].add(target)
                placed += 1
                cell_id = 0
                continue
        cell_id += 1

    return occupied
