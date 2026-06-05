import json
from dataclasses import asdict

from paper_fetch.models import Paper


def to_json(papers: list[Paper]) -> str:
    return json.dumps(
        [asdict(paper) for paper in papers],
        indent=2
    )

def to_markdown(papers: list[Paper]) -> str:
    lines = ["# Papers", ""]
    for paper in papers:
        lines.extend(
            [
                f"## {paper.title}",
                f"- Authors: {', '.join(paper.authors)}",
                f"- Category: {paper.category}",
                f"- Published: {paper.published}",
                f"- URL: {paper.url}",
                ""
            ]
        )

    return "\n".join(lines)

def to_table(papers: list[Paper]) -> str:
    if not papers:
        return "No papers found."

    rows = []

    header = (
        f"{'Title':40}"
        f"{'Category':15}"
        f"{'Published':15}"
    )

    rows.append(header)
    rows.append("-" * len(header))

    for paper in papers:
        rows.append(
            f"{paper.title[:38]:40}"
            f"{paper.category:15}"
            f"{paper.published:15}"
        )

    return "\n".join(rows)