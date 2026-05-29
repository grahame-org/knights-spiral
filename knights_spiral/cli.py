"""Command-line interface for the knight's spiral generator."""

import argparse
import sys

from knights_spiral.image import generate_image


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a knight's spiral PNG image."
    )
    parser.add_argument(
        "iterations",
        type=int,
        help="Number of knights to place.",
    )
    parser.add_argument(
        "-o", "--output",
        default="knights_spiral.png",
        help="Output PNG file path (default: knights_spiral.png).",
    )

    args = parser.parse_args()

    if args.iterations < 1:
        print("Error: iterations must be at least 1.", file=sys.stderr)
        sys.exit(1)

    generate_image(args.iterations, args.output)


if __name__ == "__main__":
    main()
