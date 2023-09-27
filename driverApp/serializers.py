from rest_framework import serializers
from .models import  Booking, Utilisateur

#Serailizer user
class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ["username", "email", "id", "role"]

#Serailizer booking
class BookingSerializer(serializers.ModelSerializer):
    dravername = serializers.SerializerMethodField(method_name="Mydravername")
    id = serializers.UUIDField(read_only = True)
    class Meta:
        model = Booking
        fields = ["id", "statut", "dravername"]
    #Here we are return the draver name
    def Mydravername(self, book:Booking):
        role_user = book.user.role
        if role_user == "Chauffeur":
            return book.user.username
        

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ["username", "email", "id", "role"]

#Serailizer Reponse driver
class ReponsedriverSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only = True)
    user = UtilisateurSerializer(read_only=True)
    class Meta:
        model = Booking
        fields = ["id", "statut", "user"]
    #Here we are going to overload the update method of the serializers
    def update(self, instance, validated_data):
        instance.statut = validated_data.get("statut")
        instance.user = validated_data.get("user")
        instance.save()
        return instance
        
#Create book serializer
class CreatebokingSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only = True)
    class Meta:
        model = Booking
        fields = ["id", "email_driver"]
    