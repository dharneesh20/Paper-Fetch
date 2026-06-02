import xml.etree.ElementTree as ET
from datetime import datetime
import httpx
from paper_fetch.models import Paper

ARXIV_API_URL = "https://export.arxiv.org/api/query"

def search_papers(
    query: str,
    limit: int = 10,
    category: str | None = None,
    since_date: datetime | None = None,
) -> list[Paper]:

    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": limit,
    }

    try:
        response = httpx.get(
            ARXIV_API_URL,
            params=params,
            timeout=15.0,
        )

        response.raise_for_status()

    except httpx.RequestError:
        raise RuntimeError(
            "Cannot connect to arXiv."
        )

    papers = parse_arxiv_response(response.text)

    if category:
        papers = [
            paper
            for paper in papers
            if paper.category == category
        ]

    if since_date:
        papers = [
            paper
            for paper in papers
            if datetime.fromisoformat(
                paper.published
            ) >= since_date
        ]

    return papers