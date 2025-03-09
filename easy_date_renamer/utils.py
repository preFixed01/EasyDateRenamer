"""Fournit des fonctions utiles"""

import io
import os
from typing import Optional


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


def fct(a: int, b: int) -> int:
    """_summary_

    _extended_summary_

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        int: _description_
    """
    return a + b if a > b else a - b
