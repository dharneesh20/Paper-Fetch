from paper_fetch.models import Paper


def test_paper_creation():

    paper = Paper(
        arxiv_id="1234.5678",
        title="Test Paper",
        authors=["John Doe"],
        category="cs.LG",
        published="2026-06-01",
        url="https://arxiv.org/abs/1234.5678",
        abstract="Test Abstract",
    )

    assert paper.title == "Test Paper"
    assert paper.category == "cs.LG"
    assert len(paper.authors) == 1


def test_paper_url():

    paper = Paper(
        arxiv_id="1234.5678",
        title="Test Paper",
        authors=["John Doe"],
        category="cs.LG",
        published="2026-06-01",
        url="https://arxiv.org/abs/1234.5678",
        abstract="Test Abstract",
    )

    assert "arxiv.org" in paper.url


def test_paper_abstract():

    paper = Paper(
        arxiv_id="1234.5678",
        title="Test Paper",
        authors=["John Doe"],
        category="cs.LG",
        published="2026-06-01",
        url="https://arxiv.org/abs/1234.5678",
        abstract="Test Abstract",
    )

    assert paper.abstract == "Test Abstract"