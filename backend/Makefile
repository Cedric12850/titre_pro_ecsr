# -------------------------------
# Makefile pour Docker - site_titre_pro_ecsr
# -------------------------------

# Nom des services dans docker-compose
WEB_SERVICE = web
DB_SERVICE = db

# Commande compose
DC = docker compose -f ../docker-compose.yml

# -------------------------------
# Initialisation : build + up en arrière-plan
# -------------------------------
init:
	@echo "🚀 Build et lancement des containers en arrière-plan..."
	$(DC) build
	$(DC) up -d

# -------------------------------
# Lancer le serveur Django (attaché au terminal)
# -------------------------------
run:
	@echo "▶️ Démarrage du serveur Django..."
	$(DC) up

# -------------------------------
# Accéder au shell Django
# -------------------------------
shell:
	@echo "💻 Accès au shell Django..."
	$(DC) exec $(WEB_SERVICE) python manage.py shell

# -------------------------------
# Migrations
# -------------------------------
makemigrations:
	@echo "📝 Création des migrations..."
	$(DC) exec $(WEB_SERVICE) python manage.py makemigrations

migrate:
	@echo "✅ Application des migrations..."
	$(DC) exec $(WEB_SERVICE) python manage.py migrate

# -------------------------------
# Créer un superuser
# -------------------------------
createsuperuser:
	@echo "👤 Création d'un superuser Django..."
	$(DC) exec $(WEB_SERVICE) python manage.py createsuperuser

# -------------------------------
# Nettoyage des __pycache__ dans le container web
# -------------------------------
clean:
	@echo "🧹 Nettoyage des __pycache__..."
	$(DC) exec $(WEB_SERVICE) find . -type d -name '__pycache__' -exec rm -rf {} +

# -------------------------------
# Stopper et supprimer tous les containers (mais conserve les volumes)
# -------------------------------
stop:
	@echo "🛑 Arrêt des containers..."
	$(DC) down

# -------------------------------
# Stopper et supprimer containers + volumes
# -------------------------------
reset:
	@echo "🗑 Suppression des containers et volumes..."
	$(DC) down -v

# -------------------------------
# Commande complète setup : init + migrations + superuser
# -------------------------------
setup: init makemigrations migrate
	@echo "💡 Setup terminé, vous pouvez créer un superuser avec : make createsuperuser"





# # ─────────────────────────────
# # Variables globales
# # ─────────────────────────────
# ifeq ($(OS),Windows_NT)
#     PYTHON = env/Scripts/python.exe
#     ACTIVATE = env\Scripts\activate
#     RM = rmdir /s /q
#     FIND = powershell -Command "Get-ChildItem -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force"
# else
#     PYTHON = env/bin/python
#     ACTIVATE = source env/bin/activate
#     RM = rm -rf
#     FIND = find . -type d -name '__pycache__' -exec rm -r {} +
# endif

# PIP = $(PYTHON) -m pip

# # ─────────────────────────────
# # Initialisation de l'environnement virtuel et installation des dépendances
# # ─────────────────────────────
# init:
# ifeq ($(OS),Windows_NT)
# 	py -3.11 -m venv env
# else
# 	python3.11 -m venv env
# endif
# 	$(PIP) install --upgrade pip setuptools wheel
# 	$(PIP) install -r requirements.txt

# # ─────────────────────────────
# # Vérifier que CKEditor est installé (ou l’installer)
# # ─────────────────────────────
# check-ckeditor:
# 	$(PIP) show django-ckeditor || $(PIP) install django-ckeditor==6.3.1

# # ─────────────────────────────
# # Lancer le serveur Django
# # ─────────────────────────────
# run:
# 	$(PYTHON) manage.py runserver

# # ─────────────────────────────
# # Migrations
# # ─────────────────────────────
# migration:
# 	$(PYTHON) manage.py makemigrations

# migrate:
# 	$(PYTHON) manage.py migrate

# # ─────────────────────────────
# # Créer un super utilisateur
# # ─────────────────────────────
# createsuperuser:
# 	$(PYTHON) manage.py createsuperuser

# # ─────────────────────────────
# # Nettoyage des __pycache__
# # ─────────────────────────────
# clean:
# 	$(FIND)

# # ─────────────────────────────
# # Supprimer l'environnement virtuel
# # ─────────────────────────────
# reset:
# 	$(RM) env

# # ─────────────────────────────
# # Installer toutes les dépendances et CKEditor d'un coup
# # ─────────────────────────────
# setup: init check-ckeditor migrate

# # ─────────────────────────────
# # Créer une nouvelle application Django (compatible Windows & Linux)
# # Utiliser : make app name=nom_app
# # ─────────────────────────────
# app:
# ifeq ($(OS),Windows_NT)
# 	@if ("$(name)"=="") { \
# 		Write-Host "❌ Erreur : vous devez spécifier un nom d'application. Exemple : make app name=conduite"; \
# 	} else { \
# 		Write-Host "📁 Création de l'application Django : $(name)"; \
# 		$(PYTHON) manage.py startapp $(name); \
# 		Write-Host "✅ Application $(name) créée dans backend/$(name)"; \
# 	}
# else
# 	@if [ -z "$(name)" ]; then \
# 		echo "❌ Erreur : vous devez spécifier un nom d'application. Exemple : make app name=conduite"; \
# 	else \
# 		echo "📁 Création de l'application Django : $(name)"; \
# 		$(PYTHON) manage.py startapp $(name); \
# 		echo "✅ Application $(name) créée dans backend/$(name)"; \
# 	fi
# endif
