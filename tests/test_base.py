"""Module de test pour le module de base"""

from datetime import datetime
import os
import logging

import pytest
from easy_date_renamer.base import NAME, rename_and_copy_files

log = logging.getLogger(__name__)


def test_base():
    """Assure que le nom du projet est correct"""
    assert NAME == "easy_date_renamer"


def test_rename_and_copy_files_valid(tmpdir, caplog):
    """
    Test that rename_and_copy_files correctly renames and copies files to the destination directory.
    """
    src_dir = tmpdir.mkdir("source")
    dest_dir = tmpdir.mkdir("destination")

    # Create test files in source directory
    test_file1 = src_dir.join("file1.txt")
    test_file1.write("Test content 1")

    test_file2 = src_dir.join("file2.log")
    test_file2.write("Test content 2")

    # Set a specific modification time for consistency
    mod_time1 = datetime(2024, 3, 1, 14, 30, 15).timestamp()
    mod_time2 = datetime(2024, 3, 2, 16, 45, 10).timestamp()

    os.utime(str(test_file1), (mod_time1, mod_time1))
    os.utime(str(test_file2), (mod_time2, mod_time2))

    with caplog.at_level(logging.INFO):  # Capture logs
        processed_files = rename_and_copy_files(str(src_dir), str(dest_dir))

    # Verify the correct number of files were processed
    assert processed_files == 2

    # Verify that files exist in the destination directory
    dest_files = os.listdir(dest_dir)
    assert len(dest_files) == 2

    # Check that filenames are correctly formatted based on modification time
    expected_filename1 = "01_03_2024_14-30-15.txt"
    expected_filename2 = "02_03_2024_16-45-10.log"

    assert expected_filename1 in dest_files, f"Expected {expected_filename1}, but got {dest_files}"
    assert expected_filename2 in dest_files, f"Expected {expected_filename2}, but got {dest_files}"

    # Ensure log messages were recorded
    assert "Copied and renamed" in caplog.text
    assert "Successfully processed 2 files." in caplog.text


def test_rename_and_copy_files_no_files(tmpdir, caplog):
    """
    Test that rename_and_copy_files correctly handles an empty source directory.
    """
    src_dir = tmpdir.mkdir("empty_source")
    dest_dir = tmpdir.mkdir("destination")

    with caplog.at_level(logging.WARNING):
        processed_files = rename_and_copy_files(str(src_dir), str(dest_dir))

    assert processed_files == 0  # No files should be processed
    assert "No files found in the source directory" in caplog.text


def test_rename_and_copy_files_invalid_source(tmpdir):
    """
    Test that rename_and_copy_files raises FileNotFoundError if the source directory does not exist.
    """
    src_dir = tmpdir.join("non_existent_source")  # Directory is not created
    dest_dir = tmpdir.mkdir("destination")

    with pytest.raises(FileNotFoundError):
        rename_and_copy_files(str(src_dir), str(dest_dir))


def test_rename_and_copy_files_creates_dest_dir(tmpdir):
    """
    Test that rename_and_copy_files creates the destination directory if it does not exist.
    """
    src_dir = tmpdir.mkdir("source")
    dest_dir = tmpdir.join("new_destination")  # Directory is not created yet

    test_file = src_dir.join("test.txt")
    test_file.write("Content")

    rename_and_copy_files(str(src_dir), str(dest_dir))

    assert os.path.isdir(dest_dir)  # Ensure destination directory is created
    assert len(os.listdir(dest_dir)) == 1  # File should be copied successfully


def test_rename_and_copy_files_preserves_metadata(tmpdir):
    """
    Test that rename_and_copy_files copies files while preserving metadata.
    """
    src_dir = tmpdir.mkdir("source")
    dest_dir = tmpdir.mkdir("destination")

    test_file = src_dir.join("testfile.txt")
    test_file.write("Sample content")

    # Set a specific modification time
    mod_time = datetime(2024, 3, 1, 12, 30, 15).timestamp()
    os.utime(str(test_file), (mod_time, mod_time))

    rename_and_copy_files(str(src_dir), str(dest_dir))

    # Ensure file exists in destination
    copied_file = os.listdir(dest_dir)[0]
    copied_file_path = os.path.join(dest_dir, copied_file)

    # Check if modification time is preserved
    copied_mod_time = os.path.getmtime(copied_file_path)
    assert int(copied_mod_time) == int(mod_time)  # Ensure timestamps match
