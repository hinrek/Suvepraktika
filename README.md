# ELU - Mõte

## Eesmärk ja lühikirjeldus

### Elu - Mõte projekt on veebirakendus, mis võimaldab luua üritusi ja neid hallata.

- Üritused
  - Loomine, kustutamine ja muutmine
  - Üritustele kommentaaride lisamine
- Kasutajad
  - Kasutajate lisamine, kustutamine ja muutmine
- Ürituse kategooriad
  - Kategooriate lisamine, muutmine ja kustutamine
- Administratiivne liides /admin
  - Ürituste, ürituse kategooriate ja kasutajate haldus

## Kasutatud tehnoloogiad

- Python3
- Django 1.10.7
- Lisa moodulid [requirements.txt](requirements.txt)

## Projekti panustavad

- Hinrek Saar
- Jan Treiberg
- Kärol-Milaine Jürgenson
- Brigitta Kannel
- Jüri Johannes Derkun

## Litsents

MIT [LICENSE](LICENSE)

## Organisatoorne info

### Kärol on second boss, kes vastutab kui Hinrek tööl!

- Praktika algab kell 09.00 ruumis A406
- Kohustuslik koosolek kell 09.20
- Iga liige täidab `./Blogi/sinu nimi/` kaustas iga päev blogi (mida tegi jne)

## Leht on testimiseks üleval: http://hinrek.pythonanywhere.com

- Lehele pääsemiseks admin : Test1234
- Superuser admin : Test1234

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

## Projekti paigaldamine ja käivitamine

- Veenduge et arvutisse on paigaldatud python3
- Enne käivitamist peab tekitama virtuaalse python3 keskkonna, mida rakendus hakkab kasutama. Käsk mis loob vastava keskkonna Posix `python3 -m venv myvenv` ja windoosa all võiks see midagi sellist välja näha `C:\Python35\python -m venv myvenv` võib ka kasutada virtualenv ehk `pip install virtualenv` ja siis peale seda `virtualenv myvenv`. Sisuliselt ei pea kasutama virtuaalselt keskkonda aga seda vähem pudru pärast arvutis.
- Peale keskkonna loomist peaks selle aktiveerima, et kõik mida paigaldame tehakse myvenv keskkonda. Erinevatel op süsteemidel käsk veits erinev jälle windoosas `myvenv\Scripts\activate` Posix laadses `source myvenv/bin/activate`
- Uuendage pip `pip install --upgrade pip`
- Paigaldame vajalikud moodulid `pip install -r requirements.txt`
- Soovitav kontrollida andmete migreerimine `python manage.py makemigrations`
- Loome andmebaasi migreerimiste alusel `python manage.py migrate`
- Loome admin õigustes kasutaja `python manage.py createsuperuser`

### Eelnevaid samme peab tegema vaid esmasel paigaldusel ja keskkonna uuendamisel

- Käivita projekt `python manage.py runserver`
- Veenduge, et /admin lehel oleks "Event categorys" all olemas mõni kategooria enne uue ürituse loomist
  - Enne projekti käivitamist veenduge et olete aktiveerinud virtuaalse keskkonna (juhul kui kasutate mõnda)