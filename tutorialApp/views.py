from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from tutorialApp.models import Tutorial
from tutorialApp.serializers import TutorialSerializer


# GET lista de tutoriales (o uno según su título), 
# POST un nuevo tutorial, 
# DELETE todos los tutoriales
@api_view(['GET', 'POST', 'DELETE'])
def listaTutoriales(request):
    if request.method == 'GET': # Queremos ver tutoriales
        tutoriales = Tutorial.objects.all()
        
        titulo = request.GET.get('titulo', None)
        if titulo is not None: # Si el GET viene con ?titulo=titulo -> filtramos
            tutoriales = tutoriales.filter(titulo__icontains=titulo)

        tutorialSerializer = TutorialSerializer(tutoriales, many=True)
        return JsonResponse(tutorialSerializer.data, safe=False) # Pasamos a RespuestaJSON los datos del serializer y enviamos
    
    elif request.method == 'POST':
        nuevoTutorial = JSONParser().parse(request)
        tutorialSerializer = TutorialSerializer(data=nuevoTutorial)
        
        if tutorialSerializer.is_valid(): # formato POST correcto
            tutorialSerializer.save() # Persistimos el nuevo tutorial
            return JsonResponse(tutorialSerializer.data, status=status.HTTP_201_CREATED) 
        
        return JsonResponse(tutorialSerializer.errors, status=status.HTTP_400_BAD_REQUEST) # Formato POST incorrecto
    
    elif request.method == 'DELETE': # Ojo que borramos todo
        nTBorrados = Tutorial.objects.all().delete()
        return JsonResponse(
            {'message': 'Los {} tutoriales se borraron correctamente'.format(nTBorrados[0])}, 
            status=status.HTTP_204_NO_CONTENT)
    

# GET / PUT / DELETE un tutorial    
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial(request, pk):
    # Buscamos tutorial por clave primaria
    try:
        tutorial = Tutorial.objects.get(pk=pk)
    except Tutorial.DoesNotExist:
        return JsonResponse({'message': 'El tutorial no existe'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        tutorialSerializer = TutorialSerializer(tutorial)
        return JsonResponse(tutorialSerializer.data) 
     
    elif request.method == 'PUT':
        tutorialModificado = JSONParser().parse(request)
        tutorialSerializer = TutorialSerializer(tutorial, data=tutorialModificado)
        
        if tutorialSerializer.is_valid():
            tutorialSerializer.save()
            return JsonResponse(tutorialSerializer.data)
    
        # Error
        return JsonResponse(tutorialSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        tutorial.delete()
        return JsonResponse({'message': 'El tutorial ha sido borrado con exito'}, 
                            status=status.HTTP_204_NO_CONTENT)


# GET todos los tutoriales publicados
@api_view(['GET'])
def listaTutorialesPublicados(request):
    if request.method == 'GET':
        tutoriales = Tutorial.objects.filter(publicado=True)
        
        tutorialSerializer = TutorialSerializer(tutoriales, many=True)
        return JsonResponse(tutorialSerializer.data, safe=False)