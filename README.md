
# easy_date_renamer

[![Latest Release](https://gitlab.com/PolySandbox/python-project-template/-/badges/release.svg)](https://gitlab.com/PolySandbox/python-project-template/-/releases)
[![pipeline status](https://gitlab.com/PolySandbox/python-project-template/badges/main/pipeline.svg)](https://gitlab.com/PolySandbox/python-project-template/-/commits/main)
[![coverage report](https://gitlab.com/PolySandbox/python-project-template/badges/main/coverage.svg)](https://gitlab.com/PolySandbox/python-project-template/-/commits/main)

project_description

## Récupération de l'environnement de dev

```bash
git clone git@gitlab.com:PolySandbox/python-project-template.git
make virtualenv
source .venv/bin/activate
```

## Usage de l'environnement de dev

Vous pouvez appeler l'interface en ligne de commandes du programme:

```bash
easy_date_renamer
```

Appeler un module spécifique du package

```bash
python -m easy_date_renamer.utils
```

## Installation du package depuis les sources

Vous pouvez aussi installer le package dans votre environnement virtuel (mode développement)

```bash
make install
```

Ou tout simplement installer le package:

```bash
pip install .
```

## Installation du package depuis pypi registery

```bash
pip install project-name --index-url https://gitlab.com/api/v4/projects/62863242/packages/pypi/simple
```

## Installation du package depuis docker registery

```bash
TODO
```

## Utilisation du package dans un autre projet

```py
from easy_date_renamer import BaseClass
from easy_date_renamer import base_function

BaseClass().base_method()
base_function()
```
