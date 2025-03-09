"""Python setup.py pour le paquet easy_date_renamer"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """
    Lit le contenu d'un fichier texte.

    Exemple :
        >>> read("easy_date_renamer", "VERSION")
        '0.1.0'
        >>> read("README.md")
        ...

    Args:
        *paths (str): Les segments du chemin du fichier.
        **kwargs: Arguments supplémentaires, comme "encoding".

    Returns:
        str: Le contenu du fichier en tant que chaîne de caractères.
    """
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(filename: str):
    """
    Lit un fichier de dépendances et renvoie une liste de lignes nettoyées.

    Cette fonction lit le fichier `filename` et renvoie une liste de dépendances
    en en excluant les lignes qui commencent par des guillemets, '#', '-', ou 'git+'.

    Args:
        filename (str): Le chemin vers le fichier.

    Returns:
        list: Liste des dépendances nettoyées.
    """
    return [
        line.strip()
        for line in read(filename).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="easy_date_renamer",
    version=read("easy_date_renamer", "VERSION"),
    description="project_description",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="author_name",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    package_data={
        "easy_date_renamer": ["VERSION"],
    },
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["easy_date_renamer = easy_date_renamer.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
