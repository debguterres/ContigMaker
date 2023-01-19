from abc import ABCMeta, abstractmethod
from pathlib import Path
from typing import Any


class DataSourceLoading(metaclass=ABCMeta):

    @abstractmethod
    def load(self, file_path: Path) -> Any:
        ...
