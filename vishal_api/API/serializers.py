from rest_framework import serializers
from .models import Languages,Developers

class LanguagesSerializer(serializers.ModelSerializer):
    # name = serializers.PrimaryKeyRelatedField(queryset=Developers.objects.all(), many= False)
    class Meta:
        model = Languages
        fields = ('language','id',)


class DevelopersSerializer(serializers.ModelSerializer):

    language = LanguagesSerializer(many=True)
    class Meta:
        model = Developers
        fields = ('name', 'language', 'id',)

