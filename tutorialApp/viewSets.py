from rest_framework import viewsets

from tutorialApp.models import Tutorial
from tutorialApp.serializers import TutorialSerializer

class TutorialesViewSet(viewsets.ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
    
    