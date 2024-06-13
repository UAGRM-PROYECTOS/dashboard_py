from django.http import JsonResponse
from datetime import datetime, timedelta
from django.shortcuts import render
import requests
from datetime import datetime
from collections import defaultdict
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
# #---------------------------------------------------------------------
# @require_http_methods(["GET"])
# def fechas_views(request):
#     # If the request is GET, retrieve and display data
#     fechas = Fechas.objects.all()
#     serializer = FechaSerializer(fechas, many=True)
    
#     # Extracting only the required fields from the serialized data
#     fechas_data = [{"fecha_inicio": fecha["fecha_inicio"], "fecha_final": fecha["fecha_final"]} for fecha in serializer.data]

#     response_data = {"fechas": fechas_data}
#     return JsonResponse(response_data)

# @require_http_methods(["POST"])
# def fechas_views_post(request):
#     # Handle the form submission logic here
#     fecha_inicio = request.POST.get('fecha_inicio')
#     fecha_final = request.POST.get('fecha_final')

#     # Validate and process the form data as needed
#     # Example: Save the form data to the database
#     Fechas.objects.create(fecha_inicio=fecha_inicio, fecha_final=fecha_final)

#     # Return a JsonResponse or redirect to a different page
#     return JsonResponse({"message": "Form submitted successfully"})

# def dashboard(request):
#     # Lógica para obtener los datos del gráfico desde la base de datos o donde sea necesario
#     datos_grafico = [...]  

#     return render(request, 'dashboard.html', {'datos_grafico': datos_grafico})
# # def dashboard_flexmonster(request):
# #     # Lógica para obtener los datos del gráfico desde la base de datos o donde sea necesario
# #     datos_flexmonster = [...]  

# #     return render(request, 'dashboard_flexmonster.html', {'datos_flexmonster': datos_flexmonster})




#----------------Services---------------------------------------------------------------------------------------------

def get_services_enpoints(request):
    # Hacer una solicitud a la API de Laravel para datos de productos próximos a vencer
    #Visitas
    url_visitas = 'http://127.0.0.1:8000/myapp/dashboard/publication/'#'http://34.151.236.58:3000/api/show/next-expired-products'
    response_visitas = requests.get(url_visitas)
    #News
    url_news = 'http://127.0.0.1:8000/myapp/dashboard/news/'#'http://34.151.236.58:3000/api/show/next-expired-products'
    response_news = requests.get(url_news)
    #Projects
    url_projects = 'http://127.0.0.1:8000/myapp/dashboard/project/'#'http://34.151.236.58:3000/api/show/next-expired-products'
    response_projects = requests.get(url_projects)
    #Presenter
    url_presenter = 'http://127.0.0.1:8000/myapp/dashboard/presenter/'#'http://34.151.236.58:3000/api/show/next-expired-products'
    response_presenter = requests.get(url_presenter)



    # Verificar si las solicitudes fueron exitosas y hay datos
    if (
        response_visitas.status_code == 200 and
        response_news.status_code == 200 and
        response_projects.status_code == 200 and
        response_presenter.status_code == 200 #and
        
    ):
        data_response_visitas = response_visitas.json()
        data_response_news = response_news.json()
        data_response_projects =  response_projects.json()
        data_response_presenter =  response_presenter.json()
        #print(data_response_visitas)

        #--------------Calculos----------------------------------------------------------------------
         # Calculate total views per category
        category_views = {}
        total_visitas = 0
        for entry in data_response_visitas:
            category = entry['description']
            views = entry['views']
            total_visitas += views
            if category in category_views:
                category_views[category] += views
            else:
                category_views[category] = views
        
        # Convert the category_views dictionary to a list of dictionaries for easy rendering
        category_views_list = [{'description': k, 'views': v} for k, v in category_views.items()]
        #----------------------------------------------------------------------------------
        # Get the current date
        current_date = datetime.now()
        # Calculate the date one month ago
        one_month_ago = current_date - timedelta(days=30)
        # Filter news articles to include only those from the last month
        recent_news = [article for article in data_response_news if datetime.strptime(article["publication_date"], "%Y-%m-%d") > one_month_ago]

        for article in recent_news:
            for status in data_response_visitas:
                if article["publicationStatu_id"] == status["id"]:
                    article["views"] = status["views"]
                    break

        sorted_news = sorted(recent_news, key=lambda x: x.get("views", 0), reverse=True)
        top_three_news = sorted_news[:3]

        total_views_top_three = sum(article.get('views', 0) for article in top_three_news)

        for article in top_three_news:
            if total_views_top_three > 0:
                article['percentage'] = (article.get('views', 0) / total_views_top_three) * 100
            else:
                article['percentage'] = 0

        #--------------------Calculando top 5 presentadores con mas vistas---------------------------------------------------------------------------------------------
        # Crear un diccionario para almacenar las vistas por presentador
        presenter_views = {presenter["id"]: 0 for presenter in data_response_presenter}
        # Calcular las vistas por presentador
        for news_item in data_response_news:
        # Obtener el proyecto asociado a esta noticia
            project = next((p for p in data_response_projects if p["id"] == news_item["project_id"]), None)
            if project:
        # Asegúrate de que news_item tiene el atributo 'views'
                if "views" in news_item:
                    presenter_views[project["presenter_id"]] += news_item["views"]

        # Ordenar los presentadores por vistas en orden descendente y tomar los 5 primeros
        top_presenters = sorted(presenter_views.items(), key=lambda x: x[1], reverse=True)[:5]

        # Obtener los nombres de los presentadores y sus vistas
        top_presenters_data = [
            {"id": presenter_id, "full_name": next(presenter["full_name"] for presenter in data_response_presenter if presenter["id"] == presenter_id), "views": views}
        for presenter_id, views in top_presenters
        ]

        #------------------Calculo analissi de estacionalidad de las noticias---------------------------------------------------------------------------------------
        # Crear un diccionario para contar los temas por mes
        topics_by_month = defaultdict(list)

        # Procesar cada noticia
        for news in data_response_news:
            try:
                # Convertir la fecha de publicación a objeto datetime
                pub_date = datetime.strptime(news['publication_date'], '%Y-%m-%d')
        
                # Agrupar por mes
                month_key = pub_date.strftime('%Y-%m')
        
                # Agregar el título a la lista de ese mes
                topics_by_month[month_key].append(news['titulo'])
        
            except ValueError:
                print(f"Error en formato de fecha para la noticia con ID {news['id']}.")
            continue

        # Imprimir resultados (puedes hacer más análisis aquí)
        for month, topics in topics_by_month.items():
            print(f"Mes: {month}, Cantidad de noticias: {len(topics)}")
            print(f"Temas: {topics}")

        #----------------------------------------------------------------------------------------------------------------------
        # Procesar los datos y enviarlos al contexto
        context = {
            'data_response_visitas': data_response_visitas,
            'data_category_views_list': category_views_list,
            'data_total_visitas': total_visitas,
            'data_top_three_news': top_three_news,
            'data_top_most_viewed_presenter': json.dumps(top_presenters_data),
            'data_topics_by_month': json.dumps(topics_by_month),
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