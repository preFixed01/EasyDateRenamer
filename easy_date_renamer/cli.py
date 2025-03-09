"""
Command-line interface pour easy_date_renamer

"Ce module fournit une interface en ligne de commande (CLI) pour l'application easy_date_renamer.
Il configure l'analyse des arguments, configure la journalisation avec une sortie colorée
et fournit un point d'entrée pour exécuter l'application CLI."


Usage:
    Exécutez ce module en tant que script pour utiliser l'interface de ligne de commande:

    ```bash
    python3 easy_date_renamer [options]
    ```

    Options:
    - `--version`: Affiche la version de l'application.
    - `-v, --verbose`: Active le mode détaillé, qui augmente le niveau de journalisation à DEBUG.
"""

import argparse
import logging
import sys

from colorama import Fore, Style, init

from easy_date_renamer.base import rename_and_copy_files
from easy_date_renamer.utils import read


class ColoredFormatter(logging.Formatter):
    """Formateur personnalisé pour ajouter des couleurs en
    fonction du niveau de log."""

    LOG_COLORS = {
        logging.DEBUG: Fore.GREEN,
        logging.INFO: Fore.WHITE,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.MAGENTA,
    }

    def format(self, record):
        log_color = self.LOG_COLORS.get(record.levelno, Fore.WHITE)
        record.msg = f"{log_color}{record.msg}{Style.RESET_ALL}"
        return super().format(record)


def main():
    """Poit d'entrée de easy_date_renamer"""
    version = read("", "VERSION")

    init(autoreset=True)

    # Set up argument parser
    parser = argparse.ArgumentParser(description="CLI pour easy_date_renamer")

    # Ajout d'une option pour la version
    parser.add_argument("--version", action="version", version=version)

    # Ajout d'une option pour le mode verbeux
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")

    # Add arguments for source and destination directories with default values
    parser.add_argument(
        "source_dir",
        nargs="?",
        default="./input",
        type=str,
        help="Path to the source directory (default: ./input)",
    )
    parser.add_argument(
        "dest_dir",
        nargs="?",
        default="./output",
        type=str,
        help="Path to the destination directory (default: ./output)",
    )

    # Analyser les arguments de la ligne de commande
    args = parser.parse_args()

    # Configure les logs
    handler = logging.StreamHandler()
    formatter = ColoredFormatter("%(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    logging.getLogger().handlers = [handler]

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    # Main application logic
    logging.info("Welcome to easy_date_renamer %s", version)
    logging.info("Source directory: %s", args.source_dir)
    logging.info("Destination directory: %s", args.dest_dir)

    try:
        rename_and_copy_files(args.source_dir, args.dest_dir)
    except OSError as e:
        logging.error("An error occurred: %s", str(e))
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
