from rest_framework import serializers
from tutorialApp.models import Tutorial

class TutorialSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tutorial
        fields = ('id',
                  'titulo',
                  'descripcion',
                  'publicado',)