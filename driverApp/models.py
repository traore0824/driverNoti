from django.db import models
from django.contrib.auth.models import User, AbstractUser
import uuid


#Abstract user
class Utilisateur(AbstractUser):
    choice_role = [
        ("Utilisateur", "Utilisateur"),
        ("Chauffeur", "Chauffeur")
    ]
    role = models.CharField(max_length=100, choices=choice_role)

    def __str__(self) -> str:
        return self.username
    


#table Booking this booking help you to requeste and receive reponse booking
class Booking(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    statut = models.CharField(max_length=100, default="En entente")
    email_driver = models.EmailField(default=True)
    

    def __str__(self) -> str:
        return self.statut
