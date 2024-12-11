from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import GeneticTest
from .serializers import GenericTestSerializer, StaticticSerializer
from django.db.models import Avg,Count,Max,Q, Case, When, Value,F, FloatField
from django.db.models.functions import Cast


class GeneticTestView(viewsets.ModelViewSet):
    queryset = GeneticTest.objects.all()
    serializer_class = GenericTestSerializer
    
    def list(self, request, *args, **kwargs):
        species = request.GET.get('species')
        if species:
            self.queryset = GeneticTest.objects.filter(species = species.lower())
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response = {"message": "Данные успешно добавлены",
                    "id": serializer.instance.id}
        return Response(response, status=status.HTTP_201_CREATED)

class StatisticsListView(ListAPIView):
     queryset = GeneticTest.objects.values('species').annotate(total_tests=Count('id'), 
                                            avg_milk_yield=Avg('milk_yield'), 
                                            max_milk_yield=Max('milk_yield'),
                                            good_health_count=Cast(Count('id', filter=Q(health_status='good')), FloatField()),
                                            poor_health_count=Count('id', filter=Q(health_status='poor'))).annotate(good_health_percent=Case(When(poor_health_count=0, then=Value(100)),
                                                                                                                                              default=(F('good_health_count')/(F('poor_health_count') + F('good_health_count')))*100 , 
                                                                                                                                              output_field=FloatField()))
     serializer_class = StaticticSerializer
