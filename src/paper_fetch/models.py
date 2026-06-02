from dataclasses import dataclass
from typing import List

@dataclass
class Paper:
    arxiv_id: str
    title: str
    authors: List[str]
    category: str
    published: str
    url: str
    abstract: str
    