from django.urls import path, include
from . import views
from rest_framework import routers  

router=routers.DefaultRouter()
router.register(r'publication', views.PublicationStatuViewSet)
router.register(r'administrative', views.AdministrativeViewSet)
router.register(r'news', views.NewsViewSet)
router.register(r'project', views.ProjectViewSet)
router.register(r'element', views.ElementViewSet)
router.register(r'presenter', views.PresenterViewSet)
router.register(r'editor', views.EditorViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'elementpresenter', views.ElementPresenterViewSet)
router.register(r'elementvideo', views.ElementVideoViewSet)

urlpatterns = [
    path('routes/', include(router.urls)),
    path('dashboard/', views.get_services_enpoints, name='dashboard' ),
]   