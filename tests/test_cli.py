"""Tests for the CLI entry point."""

import sys
from unittest.mock import patch

import pytest
from hamcrest import assert_that, equal_to

from knights_spiral.cli import main


class TestCli:

    def test_generates_output_file(self, tmp_path):
        output = tmp_path / "out.png"
        with patch.object(sys, "argv", ["knights-spiral", "5", "-o", str(output)]):
            main()
        assert_that(output.exists(), equal_to(True))

    def test_rejects_zero_iterations(self):
        with patch.object(sys, "argv", ["knights-spiral", "0"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert_that(exc_info.value.code, equal_to(1))

    def test_generates_with_colours(self, tmp_path):
        output = tmp_path / "out.png"
        with patch.object(
            sys, "argv",
            ["knights-spiral", "10", "-c", "2", "-o", str(output)],
        ):
            main()
        assert_that(output.exists(), equal_to(True))

    def test_rejects_zero_colours(self):
        with patch.object(sys, "argv", ["knights-spiral", "5", "-c", "0"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert_that(exc_info.value.code, equal_to(1))
