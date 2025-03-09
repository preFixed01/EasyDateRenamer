"""Configuration de l'environnement de test.

Ce module fournit des fixtures.
L'intérêt d'une fixture est de fournir un environnement de développement fixe
pour configurer un ensemble de tests dans un même contexte ou un même jeu de données

Cela permet d'isoler les tests et empêcher qu'ils n'interfèrent les uns avec les autres.
"""

import sys
from pytest import FixtureRequest, fixture


@fixture(autouse=True)
def go_to_tmpdir(request: FixtureRequest):
    """Une fixture pour changer le répertoire de travail actuel en répertoire temporaire.

    Cete fixture garantit que chaque test s'exécute dans son propre
    répertoire temporaire. Il ajuste dynamiquement le sys.path pour inclure le
    répertoire temporaire, permettant aux packages locaux créés par les tests
    d'être importés.

    Args:
        request (pytest.FixtureRequest): L'objet de requête pytest qui fournit
            accès au contexte de test demandeur.

    Yields:
        None: Cete fixture ne renvoie pas de valeur. Elle change le répertoire
            contexte pendant toute la durée du test.
    """
    tmpdir = request.getfixturevalue("tmpdir")
    # s'assure que les packages créés par les tests locaux peuvent être importés
    sys.path.insert(0, str(tmpdir))
    # Chdir uniquement pendant la durée du test.
    with tmpdir.as_cwd():
        yield
