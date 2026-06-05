from unittest.mock import patch

from typer.testing import CliRunner

from paper_fetch.cli import app
from paper_fetch.models import Paper

runner = CliRunner()


def sample_paper():
    return Paper(
        arxiv_id="1234.5678",
        title="Test Paper",
        authors=["John Doe"],
        category="cs.LG",
        published="2026-06-01",
        url="https://arxiv.org/abs/1234.5678",
        abstract="Test Abstract",
    )


def test_help():

    result = runner.invoke(
        app,
        ["--help"]
    )

    assert result.exit_code == 0


def test_table_output():

    with patch(
        "paper_fetch.cli.search_papers",
        return_value=[sample_paper()],
    ):

        result = runner.invoke(
            app,
            ["llm"]
        )

        assert result.exit_code == 0
        assert "Test Paper" in result.output


def test_json_output():

    with patch(
        "paper_fetch.cli.search_papers",
        return_value=[sample_paper()],
    ):

        result = runner.invoke(
            app,
            [
                "llm",
                "--format",
                "json",
            ]
        )

        assert result.exit_code == 0
        assert "Test Paper" in result.output


def test_markdown_output():

    with patch(
        "paper_fetch.cli.search_papers",
        return_value=[sample_paper()],
    ):

        result = runner.invoke(
            app,
            [
                "llm",
                "--format",
                "markdown",
            ]
        )

        assert result.exit_code == 0
        assert "Test Paper" in result.output