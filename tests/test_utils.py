"""Module de test pour le module utilitaires"""

import os

import pytest
from easy_date_renamer.utils import read


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
