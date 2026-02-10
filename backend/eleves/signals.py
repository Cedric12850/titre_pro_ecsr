# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Eleve, ProgressionObjectif
# from trame_pedagogique.models import Objectif as TrameObjectif

# @receiver(post_save, sender=Eleve)
# def create_objectifs_for_new_eleve(sender, instance, created, **kwargs):
#     if not created:
#         return
#     print(f"Signal post_save déclenché pour l'élève {instance}")  # <-- test

#     # Récupère tous les objectifs de la trame pédagogique
#     objectifs = TrameObjectif.objects.all()

#     progression_objs = [
#         ProgressionObjectif(
#             eleve=instance,
#             objectif=obj,
#             statut="pas_aborde"
#         )
#         for obj in objectifs
#     ]

#     ProgressionObjectif.objects.bulk_create(progression_objs)