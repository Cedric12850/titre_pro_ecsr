# -------------------------------
# Makefile pour Docker - titre_pro_ecsr
# -------------------------------

# Nom des services dans docker-compose
WEB_SERVICE = web
DB_SERVICE = db

# Commande docker compose
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
# Commande complète setup : init + migrations
# -------------------------------
setup: init makemigrations migrate
	@echo "💡 Setup terminé, vous pouvez créer un superuser avec : make createsuperuser"

# -------------------------------
# Créer une nouvelle application Django
# Usage : make app name=nom_app
# -------------------------------
app:
ifeq ($(name),)
	$(error "❌ Vous devez spécifier un nom d'application. Exemple : make app name=trame_pedagogique")
endif
	@echo "📁 Création de l'application Django : $(name)"
	$(DC) exec $(WEB_SERVICE) python manage.py startapp $(name)
	@echo "✅ Application $(name) créée dans backend/$(name)"
