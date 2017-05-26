# SuvePraktika

## Enne mitte torkida kui algusest lõpuni läbitud õpetused:

- [Django Girls Tutorial](https://tutorial.djangogirls.org/en/)
- [Django Girls Tutorial: Extensions](https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/content/)

## Andmebaas

Hetkel arenduse faasis on meil endal hea lihtne kasutada db.sqlite3 baasi, mis sisuliselt on väike fail. Hiljem migreerime postgre peale.

## Mida mitte laadida githubi

- Enda keskkonda (virtualenv)
- Andmebaasi (nt. db.sqlite3)
- IDE seadete faile ja kaustasid (.vscode, .idea jne...)

## Arenduseks soovitan kasutada

- VSCode
  - Lisaks html/css lisadele: Django, Django Snippets, Django Template, python, MagicPython...

### Koodi kontrollimiseks headele tavadele vastavust, kasutada "flake8" ja "pylint" *lintereid*

## Keskkonna paigaldamine ja käivitamine oma arvutis

- Veenduge et arvutisse on paigaldatud python3
- Enne käivitamist peab tekitama virtuaalse python3 keskkonna, mida rakendus hakkab kasutama. Käsk mis loob vastava keskkonna unixis `python3 -m venv myvenv` ja windoosa all võiks see midagi sellist välja näha `C:\Python35\python -m venv myvenv` võib ka kasutada virtualenv ehk `pip install virtualenv` ja siis peale seda `virtualenv myvenv`. Sisuliselt ei pea kasutama virtuaalselt keskkonda aga seda vähem pudru pärast arvutis.
- Peale keskkonna loomist peaks selle aktiveerima, et kõik mida paigaldame tehakse myvenv keskkonda. Erinevatel op süsteemidel käsk veits erinev jälle windoosas `myvenv\Scripts\activate` unix laadses `source myvenv/bin/activate`
- Uuendage pip `pip install --upgrade pip`
- Paigaldage Django `pip install django~=1.10.0`
- Loome andmebaasi `python manage.py migrate`
- Loome admin õigustes kasutaja `python manage.py createsuperuser`

### Eelnevaid samme peab tegema vaid esmasel paigaldusel

- Käivita projekt `python manage.py runserver`
  - Enne projekti käivitamist veenduge et olete aktiveerinud virtuaalse keskkonna (juhul kui kasutate mõnda)