"""Fournit des fonctions utiles"""

import io
import logging
import os
from typing import Optional

log = logging.getLogger(__name__)


def read(*paths: str, **kwargs: Optional[str]) -> str:
    """
    Lit le contenu d'un fichier texte.

    Examples:
        >>> read("VERSION")
        '0.0.0'

    Args:
        *paths (str): Un ou plusieurs segments de chemin qui seront joints pour
            localiser le fichier à lire.
        **kwargs (Optional[str]): Paramètres optionnels. Peut inclure "encoding"
            pour spécifier l'encodage du fichier (par défaut "utf8").

    Returns:
        str: Le contenu du fichier texte, sans espaces blancs en début et fin de chaîne.
    """
    content: str = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def validate_source_directory(source_dir: str):
    """
    Validates if the given source directory exists and is a directory.

    :param source_dir: Path to the source directory.
    :raises FileNotFoundError: If the directory does not exist or is not a directory.
    """
    if not os.path.isdir(source_dir):
        error_message = f"The source directory '{source_dir}' does not exist or is not a directory."
        raise FileNotFoundError(error_message)  # Raise an exception instead of exiting


def ensure_destination_directory(dest_dir: str):
    """
    Ensures that the destination directory exists. If not, it creates it.

    :param dest_dir: Path to the destination directory.
    """
    if not os.path.exists(dest_dir):
        logging.info("The destination directory '%s' does not exist. Creating it...", dest_dir)
        os.makedirs(dest_dir)
