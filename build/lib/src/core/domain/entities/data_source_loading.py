from abc import ABCMeta, abstractmethod
from pathlib import Path
from typing import Any

from contig_maker.core.domain.dtos.raw_sequence_read import RawSequenceRead


class DataSourceLoading(metaclass=ABCMeta):
    @abstractmethod
    def load(self, file_path: Path) -> RawSequenceRead:
        ...
