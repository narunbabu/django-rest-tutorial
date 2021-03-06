from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from dinosaurs.models import Dinosaur
from dinosaurs.serializers import DinosaurSerializer

# class DinosaurViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Dinosaur.objects.all()
#     serializer_class = DinosaurSerializer

@csrf_exempt
def dinosaurs_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    
    if request.method == 'GET':
        dinosaurs = Dinosaur.objects.all()
        serializer = DinosaurSerializer(dinosaurs, many=True)
        # serializer = DinosaurSerializer(dinosaurs, context={'request': request})
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DinosaurSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def dinosaur_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        dinosaur = Dinosaur.objects.get(pk=pk)
    except Dinosaur.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DinosaurSerializer(dinosaur)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DinosaurSerializer(dinosaur, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        dinosaur.delete()
        return HttpResponse(status=204)