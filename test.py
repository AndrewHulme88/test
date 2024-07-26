"""API for Relevant_Concept_Extractor"""

import dataclasses
from typing import Union

@dataclasses.dataclass
class ExtractionResponse:
"""Extraction response.

Attributes:
concepts: List of extracted concepts.
entities: List of extracted entities.
related_terms: List of extracted related terms.
"""

concepts: list[str] | None = None
entities: list[dict] | None = None
related_terms: list[str] | None = None

def extractConceptsAndEntities(
text: str,
) -> ExtractionResponse | dict:
"""Extract relevant concepts and entities from text.

Args:
text: The input text for analysis.
"""
