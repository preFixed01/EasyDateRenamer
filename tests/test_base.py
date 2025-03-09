"""Module de test pour le module de base"""

from easy_date_renamer.base import NAME


def test_base():
    """Assure que le nom du projet est correct"""
    assert NAME == "easy_date_renamer"
