"""
Module de base de easy_date_renamer.
"""

import logging
import os
import shutil
from datetime import datetime

from easy_date_renamer.utils import ensure_destination_directory, validate_source_directory

log = logging.getLogger(__name__)

NAME = "easy_date_renamer"


def rename_and_copy_files(src_dir: str, dest_dir: str) -> int:
    """
    Lists files in a directory, renames them using the format dd_MM_yyyy_HH:mm:ss,
    and copies them to an output directory.

    :param src_dir: str - Path to the source directory.
    :param dest_dir: str - Path to the destination directory.
    :return: int - Number of files processed.
    """
    # Validate source directory
    validate_source_directory(src_dir)

    # Ensure destination directory exists
    ensure_destination_directory(dest_dir)

    files = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]
    file_count = len(files)

    if file_count == 0:
        logging.warning("No files found in the source directory '%s'.", src_dir)
        return 0

    for file in files:
        src_path = os.path.join(src_dir, file)
        mod_time = datetime.fromtimestamp(os.path.getmtime(src_path))  # Get file modification time
        new_filename = (
            mod_time.strftime("%d_%m_%Y_%H-%M-%S") + os.path.splitext(file)[-1]
        )  # Keep original extension
        dest_path = os.path.join(dest_dir, new_filename)  # Define destination file path

        shutil.copy2(src_path, dest_path)  # Copy the file while preserving metadata
        logging.info("Copied and renamed: %s -> %s", file, new_filename)

    logging.info("Successfully processed %d files.", file_count)
    return file_count  # Return the total number of files processed
