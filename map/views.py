from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from .forms import CreateMap
from .models import MapInfo
from rest_framework import viewsets
from .serializers import MapInfoSerializer


def mapq(request):
    return render(request, 'map/map_base.html')

@csrf_protect
def create_point(request):
    if request.method == 'POST':
        form = CreateMap(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = CreateMap()

    return render(request, 'map/points.html', {'form': form})


class MapInfoViewSet(viewsets.ModelViewSet):
    queryset = MapInfo.objects.all()
    serializer_class = MapInfoSerializer

