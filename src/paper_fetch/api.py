from datetime import datetime

import arxiv

from paper_fetch.models import Paper


def search_papers(
    query: str,
    limit: int = 10,
    category: str | None = None,
    since_date: datetime | None = None,
) -> list[Paper]:
    """
    Search papers from arXiv.
    """

    search = arxiv.Search(
        query=query,
        max_results=limit,
        sort_by=arxiv.SortCriterion.SubmittedDate,
    )

    client = arxiv.Client( 
        page_size=5,
        delay_seconds=5.0,
        num_retries=1,
        )

    papers = []

    try:
        for result in client.results(search):

            papers.append(
                Paper(
                    arxiv_id=result.entry_id.split("/")[-1],
                    title=result.title,
                    authors=[
                        author.name
                        for author in result.authors
                    ],
                    category=result.primary_category,
                    published=result.published.strftime(
                        "%Y-%m-%d"
                    ),
                    url=result.entry_id,
                    abstract=result.summary,
                )
            )

    except Exception as e:
        raise RuntimeError(
            f"""
Unable to retrieve papers from arXiv.

Possible reasons:
- arXiv rate limit exceeded (429)
- arXiv service unavailable (503)
- Temporary network issue

Original error:
{e}
"""
        )

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