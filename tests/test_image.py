"""Tests for the PNG image generation."""

from hamcrest import assert_that, equal_to, is_
from PIL import Image


from knights_spiral.image import generate_image


class TestGenerateImage:

    def test_generates_png_file(self, tmp_path):
        output = tmp_path / "test.png"
        generate_image(5, output)
        assert_that(output.exists(), is_(True))

    def test_image_has_no_alpha_channel(self, tmp_path):
        output = tmp_path / "test.png"
        generate_image(5, output)
        img = Image.open(output)
        assert_that(img.mode, equal_to("RGB"))

    def test_image_contains_black_pixels_for_knights(self, tmp_path):
        output = tmp_path / "test.png"
        generate_image(1, output)
        img = Image.open(output)
        pixels = img.load()
        assert_that(pixels[0, 0], equal_to((0, 0, 0)))

    def test_image_dimensions_match_bounding_box(self, tmp_path):
        """With 5 knights at (0,0),(1,0),(1,-1),(0,-1),(-2,2),
        bounding box is x:[-2,1], y:[-1,2] -> 4x4 image."""
        output = tmp_path / "test.png"
        generate_image(5, output)
        img = Image.open(output)
        assert_that(img.size, equal_to((4, 4)))

    def test_single_knight_produces_1x1_image(self, tmp_path):
        output = tmp_path / "test.png"
        generate_image(1, output)
        img = Image.open(output)
        assert_that(img.size, equal_to((1, 1)))

    def test_white_pixels_for_empty_cells(self, tmp_path):
        """With 5 knights in a 4x4 image, most pixels should be white."""
        output = tmp_path / "test.png"
        generate_image(5, output)
        img = Image.open(output)
        pixels = img.load()
        white_count = 0
        for x in range(img.width):
            for y in range(img.height):
                if pixels[x, y] == (255, 255, 255):
                    white_count += 1
        assert_that(white_count, equal_to(4 * 4 - 5))


class TestGenerateImageMultiColour:

    def test_multi_colour_image_has_no_alpha(self, tmp_path):
        output = tmp_path / "test.png"
        generate_image(10, output, num_colours=2)
        img = Image.open(output)
        assert_that(img.mode, equal_to("RGB"))

    def test_multi_colour_has_non_white_pixels(self, tmp_path):
        output = tmp_path / "test.png"
        generate_image(10, output, num_colours=2)
        img = Image.open(output)
        pixels = img.load()
        non_white = 0
        for x in range(img.width):
            for y in range(img.height):
                if pixels[x, y] != (255, 255, 255):
                    non_white += 1
        assert_that(non_white, equal_to(10))

    def test_multi_colour_has_distinct_colours(self, tmp_path):
        output = tmp_path / "test.png"
        generate_image(10, output, num_colours=2)
        img = Image.open(output)
        pixels = img.load()
        colours = set()
        for x in range(img.width):
            for y in range(img.height):
                px = pixels[x, y]
                if px != (255, 255, 255):
                    colours.add(px)
        assert_that(len(colours), equal_to(2))
