from pathlib import Path, PosixPath
from typing import List

from contig_maker.core.domain.dtos.raw_sequence_read import RawSequenceRead
from contig_maker.core.domain.entities.data_source_loading import (
    DataSourceLoading,
)
from contig_maker.core.use_cases.io.load_single_file import load_single_file


def load_batch(
    folder_path: Path,
    wildcard: str,
    data_source_loading_repo: DataSourceLoading,
) -> List[RawSequenceRead]:
    
    if folder_path.is_dir() is False:
        raise IOError(f"specified path invalid: {folder_path}")

    target_paths: List[PosixPath] = list(folder_path.glob(wildcard))

    if len(target_paths) == 0:
        raise IOError(f"wildcard does not matches files: {wildcard}")

    return [
        load_single_file(
            file_path=path,
            data_source_loading_repo=data_source_loading_repo,
        )
        for path in target_paths
    ]
