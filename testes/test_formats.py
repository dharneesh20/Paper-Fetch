from paper_fetch.models import Paper
from paper_fetch.formats import (
    to_json,
    to_markdown,
    to_table,
)


def sample_paper():
    return Paper(
        arxiv_id="1234.5678",
        title="Test Paper",
        authors=["John Doe", "Alice"],
        category="cs.LG",
        published="2026-06-01",
        url="https://arxiv.org/abs/1234.5678",
        abstract="Test abstract",
    )


def test_to_json():
    papers = [sample_paper()]

    result = to_json(papers)

    assert "Test Paper" in result
    assert "cs.LG" in result


def test_to_markdown():
    papers = [sample_paper()]

    result = to_markdown(papers)

    assert "# Papers" in result
    assert "Test Paper" in result
    assert "John Doe" in result


def test_to_table():
    papers = [sample_paper()]

    result = to_table(papers)

    assert "Title" in result
    assert "Test Paper" in result
    assert "cs.LG" in result


def test_to_table_empty():
    result = to_table([])

    assert result == "No papers found."