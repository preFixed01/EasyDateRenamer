"""Module de test pour le module utilitaires"""

import os
import logging
import pytest

from easy_date_renamer.utils import read, validate_source_directory, ensure_destination_directory

log = logging.getLogger(__name__)


def test_read(tmpdir):
    """Teste la fonction de lecture avec des fichiers temporaires."""

    # Crée un fichier READ_TEST1 temporaire avec du contenu
    read_test_1 = tmpdir.join("READ_TEST1")
    read_test_1.write("read test")

    # Crée un fichier READ_TEST2 temporaire avec du contenu
    read_test_2 = tmpdir.join("READ_TEST2")
    read_test_2.write("")

    # Crée un fichier DIFFÉRENT temporaire avec du contenu
    different_file = tmpdir.join("DIFFERENT")
    different_file.write("Different content")

    # Test de lecture du fichier READ_TEST1
    version_content = read(os.path.dirname(str(read_test_1)), "READ_TEST1")
    assert version_content == "read test"

    # Test de lecture du fichier READ_TEST2
    version_content = read(os.path.dirname(str(read_test_1)), "READ_TEST2")
    assert version_content == ""

    # Lit le fichier DIFFERENT et vérifie la non-égalité
    different_content = read(os.path.dirname(str(different_file)), "DIFFERENT")
    assert different_content != "Expected content"

    # Teste le cas où le fichier demandé n'existe pas
    with pytest.raises(FileNotFoundError):
        read(os.path.dirname(str(tmpdir)), "NON_EXISTENT_FILE")


def test_validate_source_directory_valid(tmpdir):
    """
    Test that validate_source_directory does not raise an error for
    a valid directory.
    """
    valid_dir = tmpdir.mkdir("valid_directory")  # Create a valid directory inside the tmpdir
    validate_source_directory(str(valid_dir))  # Should not raise an exception


def test_validate_source_directory_invalid(tmpdir):
    """
    Test that validate_source_directory raises FileNotFoundError for a
    non-existent directory.
    """
    invalid_dir = tmpdir.join("non_existent_directory")  # Path that does not exist
    with pytest.raises(
        FileNotFoundError,
        match=f"The source directory '{invalid_dir}' does not exist or is not a directory.",
    ):
        validate_source_directory(str(invalid_dir))


def test_validate_source_directory_not_a_directory(tmpdir):
    """
    Test that validate_source_directory raises FileNotFoundError if the path
    is a file, not a directory.
    """
    file_path = tmpdir.join("some_file.txt")
    file_path.write("This is a file, not a directory.")  # Create a file instead of a directory

    with pytest.raises(
        FileNotFoundError,
        match=f"The source directory '{file_path}' does not exist or is not a directory.",
    ):
        validate_source_directory(str(file_path))


def test_ensure_destination_directory_exists(tmpdir):
    """
    Test that ensure_destination_directory does nothing if the directory
    already exists.
    """
    existing_dir = tmpdir.mkdir("existing_directory")  # Create the directory beforehand
    ensure_destination_directory(str(existing_dir))  # Should not modify anything
    assert os.path.isdir(existing_dir)  # Ensure it still exists


def test_ensure_destination_directory_created(tmpdir, caplog):
    """
    Test that ensure_destination_directory creates the directory
    if it doesn't exist.
    """
    new_dir = tmpdir.join("new_directory")  # Define the path (not created yet)

    with caplog.at_level(logging.INFO):  # Capture logs
        ensure_destination_directory(str(new_dir))

    assert os.path.isdir(new_dir)  # Ensure the directory was created
    assert (
        f"The destination directory '{new_dir}' does not exist. Creating it..." in caplog.text
    )  # Check log output
