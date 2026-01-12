# ─────────────────────────────
# Variables globales
# ─────────────────────────────
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

# ─────────────────────────────
# Initialisation de l'environnement virtuel et installation des dépendances
# ─────────────────────────────
init:
ifeq ($(OS),Windows_NT)
	py -3.11 -m venv env
else
	python3.11 -m venv env
endif
	$(PIP) install --upgrade pip setuptools wheel
	$(PIP) install -r requirements.txt

# ─────────────────────────────
# Vérifier que CKEditor est installé (ou l’installer)
# ─────────────────────────────
check-ckeditor:
	$(PIP) show django-ckeditor || $(PIP) install django-ckeditor==6.3.1

# ─────────────────────────────
# Lancer le serveur Django
# ─────────────────────────────
run:
	$(PYTHON) manage.py runserver

# ─────────────────────────────
# Migrations
# ─────────────────────────────
migration:
	$(PYTHON) manage.py makemigrations

migrate:
	$(PYTHON) manage.py migrate

# ─────────────────────────────
# Créer un super utilisateur
# ─────────────────────────────
createsuperuser:
	$(PYTHON) manage.py createsuperuser

# ─────────────────────────────
# Nettoyage des __pycache__
# ─────────────────────────────
clean:
	$(FIND)

# ─────────────────────────────
# Supprimer l'environnement virtuel
# ─────────────────────────────
reset:
	$(RM) env

# ─────────────────────────────
# Installer toutes les dépendances et CKEditor d'un coup
# ─────────────────────────────
setup: init check-ckeditor migrate

# ─────────────────────────────
# Créer une nouvelle application Django (compatible Windows & Linux)
# Utiliser : make app name=nom_app
# ─────────────────────────────
app:
ifeq ($(OS),Windows_NT)
	@if ("$(name)"=="") { \
		Write-Host "❌ Erreur : vous devez spécifier un nom d'application. Exemple : make app name=conduite"; \
	} else { \
		Write-Host "📁 Création de l'application Django : $(name)"; \
		$(PYTHON) manage.py startapp $(name); \
		Write-Host "✅ Application $(name) créée dans backend/$(name)"; \
	}
else
	@if [ -z "$(name)" ]; then \
		echo "❌ Erreur : vous devez spécifier un nom d'application. Exemple : make app name=conduite"; \
	else \
		echo "📁 Création de l'application Django : $(name)"; \
		$(PYTHON) manage.py startapp $(name); \
		echo "✅ Application $(name) créée dans backend/$(name)"; \
	fi
endif
