# Paper Fetch

A command-line tool to search research papers from arXiv.

## Features

- Search papers by keyword
- Filter papers by date
- Filter papers by category
- Limit number of results
- Output as:
  - Table
  - JSON
  - Markdown
- Graceful error handling

---

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd paper-fetch
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -e .
```

---

## Usage

Search papers:

```bash
paper-fetch "machine learning"
```

Limit results:

```bash
paper-fetch "machine learning" --limit 5
```

Filter by category:

```bash
paper-fetch "machine learning" --category cs.LG
```

Filter by date:

```bash
paper-fetch "machine learning" --since 30d
```

JSON output:

```bash
paper-fetch "machine learning" --format json
```

Markdown output:

```bash
paper-fetch "machine learning" --format markdown
```

Help:

```bash
paper-fetch --help
```

---

## Project Structure

```text
paper-fetch/
│
├── src/
│   └── paper_fetch/
│       ├── api.py
│       ├── cli.py
│       ├── dates.py
│       ├── formats.py
│       └── models.py
│
├── testes/
│   ├── test_api.py
│   ├── test_cli.py
│   ├── test_dates.py
│   └── test_formats.py
│
├── README.md
├── pyproject.toml
└── CHANGELOG.md
```

---

## Known Issues

arXiv may temporarily return:

- HTTP 429 (Too Many Requests)
- HTTP 503 (Service Unavailable)

The application handles these errors and displays a user-friendly message.

---

## Version

Current Version:

```text
v0.1.0
```

---

## Author

Dharneesh