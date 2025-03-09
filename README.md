
# easy_date_renamer

A simple and efficient script to automatically rename photos and videos based on their date metadata. Easily organize your media files by timestamp for better sorting and accessibility.

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

## Utilisation du package dans un autre projet

```py
from easy_date_renamer import BaseClass
from easy_date_renamer import base_function

BaseClass().base_method()
base_function()
```
