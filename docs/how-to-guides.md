
# Comment utiliser easy_date_renamer ?

Le projet easy_date_renamer peut être utilisé comme ci dessous.

    your_project/
    └── your_script.py

À l'intérieur de `your_script.py` vous pouvez par exemple importer la
fonction `read()` depuis le module `utils`:

    # your_script.py
    from utils import read

Après avoir importé la fonction, vous pouvez l'utiliser
pour récupérer le contenu d'un fichier :

    # your_script.py
    from from utils import read

    print(read("VERSION"))  # OUTPUT: x.y.z
