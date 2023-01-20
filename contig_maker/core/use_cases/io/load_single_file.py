from pathlib import Path

from contig_maker.core.domain.dtos.raw_sequence_read import RawSequenceRead
from contig_maker.core.domain.entities.data_source_loading import (
    DataSourceLoading,
)


def load_single_file(
    file_path: Path,
    data_source_loading_repo: DataSourceLoading,
) -> RawSequenceRead:
    if file_path.is_file() is False:
        raise IOError(f"invalid path: {file_path}")

    return data_source_loading_repo.load(file_path=file_path)
