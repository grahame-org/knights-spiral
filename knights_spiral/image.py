"""PNG image generation for the knight's spiral."""

from pathlib import Path

from PIL import Image

from knights_spiral.knights import place_knights


def generate_image(iterations: int, output_path: str | Path) -> None:
    """Generate a PNG image of the knight's spiral.

    Args:
        iterations: Number of knights to place.
        output_path: File path for the output PNG.
    """
    occupied = place_knights(iterations)

    if not occupied:
        img = Image.new("RGB", (1, 1), color=(255, 255, 255))
        img.save(str(output_path), format="PNG", compress_level=9)
        return

    min_x = min(x for x, y in occupied)
    max_x = max(x for x, y in occupied)
    min_y = min(y for x, y in occupied)
    max_y = max(y for x, y in occupied)

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    img = Image.new("RGB", (width, height), color=(255, 255, 255))
    pixels = img.load()

    for x, y in occupied:
        px = x - min_x
        py = y - min_y
        pixels[px, py] = (0, 0, 0)

    img.save(str(output_path), format="PNG", compress_level=9)
