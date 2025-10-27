ifeq ($(OS),Windows_NT)
    PYTHON = env/Scripts/python.exe
    ACTIVATE = env\Scripts\activate
    RM = rmdir /s /q
    FIND = powershell -Command "Get-ChildItem -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force"
else
    PYTHON = env/bin/python
    ACTIVATE = source env/bin/activate
    RM = rm -rf
    FIND = find . -type d -name '__pycache__' -exec rm -r {} +
endif

PIP = $(PYTHON) -m pip

# Initialisation de l'environnement virtuel et installation des dépendances
init:
	python -m venv env
	$(PIP) install --upgrade pip setuptools wheel
	$(PIP) install -r requirements.txt

# Vérifier que CKEditor est installé (ou l’installer)
check-ckeditor:
	$(PIP) show django-ckeditor || $(PIP) install django-ckeditor==6.3.1

# Lancer le serveur
run:
	$(PYTHON) manage.py runserver

# Migration
migration:
	$(PYTHON) manage.py makemigrations
migrate:
	$(PYTHON) manage.py migrate

# Créer un super utilisateur
createsuperuser:
	$(PYTHON) manage.py createsuperuser

# Nettoyage des __pycache__
clean:
	$(FIND)

# Supprimer l'environnement virtuel
reset:
	$(RM) env

# Installer toutes les dépendances et CKEditor d'un coup
setup: init check-ckeditor migrate
