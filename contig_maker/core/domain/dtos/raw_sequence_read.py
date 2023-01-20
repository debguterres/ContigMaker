from typing import List
from attr import define


@define(kw_only=True)
class RawSequenceRead:
    source_name: str
    dna_sequence: List[str]
    sequence_quality: List[int]
