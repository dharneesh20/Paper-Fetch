import typer

from paper_fetch.api import search_papers
from paper_fetch.dates import parse_since
from paper_fetch.formats import (
    to_json,
    to_markdown,
    to_table,
)

app = typer.Typer()


@app.command()
def main(
    query: str,
    since: str = typer.Option(
        None,
        help="Filter papers from last N days (e.g. 7d)"
    ),
    category: str = typer.Option(
        None,
        help="Filter by arXiv category"
    ),
    limit: int = typer.Option(
        10,
        help="Maximum number of papers"
    ),
    format: str = typer.Option(
        "table",
        help="Output format: table, json, markdown"
    ),
):
    """
    Search arXiv papers.
    """

    try:

        since_date = None

        if since:
            since_date = parse_since(since)

        papers = search_papers(
            query=query,
            limit=limit,
            category=category,
            since_date=since_date,
        )

        if format == "json":
            typer.echo(to_json(papers))

        elif format == "markdown":
            typer.echo(to_markdown(papers))

        else:
            typer.echo(to_table(papers))

    except Exception as e:
        typer.echo(f"\nError:\n{e}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()