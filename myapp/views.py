from django.http import JsonResponse
from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import PublicationStatu
from .models import Administrative
from .models import User
from .models import Editor
from .models import Presenter
from .models import ElementPresenter
from .models import ElementVideo
from .models import Element
from .models import Project
from .models import News
from .models import Fechas
from .serializers import PublicationStatuSerializer
from .serializers import AdministrativeSerializer
from .serializers import UserSerializer
from .serializers import EditorSerializer
from .serializers import PresenterSerializer
from .serializers import ElementPresenterSerializer
from .serializers import ElementVideoSerializer
from .serializers import ElementSerializer
from .serializers import ProjectSerializer
from .serializers import NewsSerializer
from .serializers import FechaSerializer
from django.views.decorators.http import require_http_methods
import json




#------------viewsets---------------------------------------
class PublicationStatuViewSet(viewsets.ModelViewSet):
    queryset= PublicationStatu.objects.all()
    serializer_class=  PublicationStatuSerializer

class AdministrativeViewSet(viewsets.ModelViewSet):
    queryset= Administrative.objects.all()
    serializer_class=  AdministrativeSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class=  UserSerializer

class EditorViewSet(viewsets.ModelViewSet):
    queryset= Editor.objects.all()
    serializer_class=  EditorSerializer

class PresenterViewSet(viewsets.ModelViewSet):
    queryset= Presenter.objects.all()
    serializer_class=  PresenterSerializer

class ElementPresenterViewSet(viewsets.ModelViewSet):
    queryset= ElementPresenter.objects.all()
    serializer_class=  ElementPresenterSerializer

class ElementVideoViewSet(viewsets.ModelViewSet):
    queryset= ElementVideo.objects.all()
    serializer_class=  ElementVideoSerializer

class ElementViewSet(viewsets.ModelViewSet):
    queryset= Element.objects.all()
    serializer_class=  ElementSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset= Project.objects.all()
    serializer_class=  ProjectSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset= News.objects.all()
    serializer_class=  NewsSerializer
#---------------------------------------------------------------------
@require_http_methods(["GET"])
def fechas_views(request):
    # If the request is GET, retrieve and display data
    fechas = Fechas.objects.all()
    serializer = FechaSerializer(fechas, many=True)
    
    # Extracting only the required fields from the serialized data
    fechas_data = [{"fecha_inicio": fecha["fecha_inicio"], "fecha_final": fecha["fecha_final"]} for fecha in serializer.data]

    response_data = {"fechas": fechas_data}
    return JsonResponse(response_data)

@require_http_methods(["POST"])
def fechas_views_post(request):
    # Handle the form submission logic here
    fecha_inicio = request.POST.get('fecha_inicio')
    fecha_final = request.POST.get('fecha_final')

    # Validate and process the form data as needed
    # Example: Save the form data to the database
    Fechas.objects.create(fecha_inicio=fecha_inicio, fecha_final=fecha_final)

    # Return a JsonResponse or redirect to a different page
    return JsonResponse({"message": "Form submitted successfully"})

def dashboard(request):
    # Lógica para obtener los datos del gráfico desde la base de datos o donde sea necesario
    datos_grafico = [...]  

    return render(request, 'dashboard.html', {'datos_grafico': datos_grafico})
# def dashboard_flexmonster(request):
#     # Lógica para obtener los datos del gráfico desde la base de datos o donde sea necesario
#     datos_flexmonster = [...]  

#     return render(request, 'dashboard_flexmonster.html', {'datos_flexmonster': datos_flexmonster})




#----------------Services---------------------------------------------------------------------------------------------

def get_services_enpoints(request):
    # Hacer una solicitud a la API de Laravel para datos de productos próximos a vencer
    url_visitas = 'http://127.0.0.1:8000/myapp/dashboard/publication/'#'http://34.151.236.58:3000/api/show/next-expired-products'
    response_visitas = requests.get(url_visitas)


    # Verificar si las solicitudes fueron exitosas y hay datos
    if (
        response_visitas.status_code == 200 #and
        # response_total_inventory_month.status_code == 200 and
        # response_total_sales_month.status_code == 200 and
        # response_obsolencia_rate_month.status_code == 200 and
        # response_inventory_turnover_month.status_code == 200 and
        # response_tendencia_temporada_month.status_code == 200 and
        # response_analisis_estacionalidad_month.status_code == 200 
        #response_predicciones_month.status_code == 200
        
    ):
        data_response_visitas = response_visitas.json()
        #print(data_response_visitas)

        # Procesar los datos y enviarlos al contexto
        context = {
            'data_response_visitas': data_response_visitas,
            # 'data_total_inventory_month': data_total_inventory_month,
            # 'data_total_sales_month': data_total_sales_month,
            # 'data_obsolencia_rate_month': data_obsolencia_rate_month.get('obsolenceRate'),
            # 'data_inventory_turnover_month': data_inventory_turnover_month,
            # 'data_tendencia_temporada_month': json.dumps(data_tendencia_temporada_month.get('seasonalityAnalysis', [])),
            # 'data_analisis_estacionalidad_month': json.dumps(data_analisis_estacionalidad_month.get('seasonalityAnalysis', [])),
           # 'data_predicciones_month': response_predicciones_month.get('data', {}).get('prediccion', {}).get('demanda', {}).get('data', [])

       
            
        }
        return render(request, 'dashboard.html', context)
    else:
        return render(request, 'error.html', {'message': 'Error al obtener datos de la API'})
# views.py



# def get_services_ia_api_pre(request):
#     if request.method == 'GET':
#         url_predicciones_month = request.GET.get('urlWithParams', '')

#         # Hacer una solicitud a la URL recibida
#         try:
#             response_predicciones_month = requests.get(url_predicciones_month)
#             response_data = response_predicciones_month.json()  # Suponiendo que la respuesta es JSON
#             # Procesar los datos de la respuesta según sea necesario
#             # ...

#             return JsonResponse({'success': True, 'message': 'Solicitud exitosa.', 'data': response_data})
#         except Exception as e:
#             return JsonResponse({'success': False, 'error': f'Error en la solicitud: {e}'})

#     return JsonResponse({'success': False, 'error': 'Método de solicitud no válido.'})