"""PNG image generation for the knight's spiral."""

import colorsys
from pathlib import Path

from PIL import Image

from knights_spiral.knights import place_knights


def _colour_palette(num_colours: int) -> list[tuple[int, int, int]]:
    """Generate a list of visually distinct RGB colours.

    With 1 colour, returns black.  With more, returns evenly spaced hues
    at full saturation and value.
    """
    if num_colours == 1:
        return [(0, 0, 0)]
    colours: list[tuple[int, int, int]] = []
    for i in range(num_colours):
        hue = i / num_colours
        r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        colours.append((int(r * 255), int(g * 255), int(b * 255)))
    return colours


def generate_image(
    iterations: int, output_path: str | Path, num_colours: int = 1
) -> None:
    """Generate a PNG image of the knight's spiral.

    Args:
        iterations: Number of knights to place.
        output_path: File path for the output PNG.
        num_colours: Number of distinct knight colours.
    """
    occupied = place_knights(iterations, num_colours)

    if not occupied:
        img = Image.new("RGB", (1, 1), color=(255, 255, 255))
        img.save(str(output_path), format="PNG", compress_level=9)
        return

    all_coords = occupied.keys()
    min_x = min(x for x, y in all_coords)
    max_x = max(x for x, y in all_coords)
    min_y = min(y for x, y in all_coords)
    max_y = max(y for x, y in all_coords)

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    palette = _colour_palette(num_colours)

    img = Image.new("RGB", (width, height), color=(255, 255, 255))
    pixels = img.load()

    for (x, y), colour_idx in occupied.items():
        px = x - min_x
        py = y - min_y
        pixels[px, py] = palette[colour_idx]

    img.save(str(output_path), format="PNG", compress_level=9)
