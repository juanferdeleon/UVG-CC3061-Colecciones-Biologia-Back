"""coleccion_biologia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from user_type.views import UserTypeViewSet
from users.views import UserViewSet
from taxonomic_level.views import TaxonomicLevelViewSet
from organism_conservation.views import OrganismConservationViewSet
from departamento.views import DepartamentoViewSet
from municipio.views import MunicipioViewSet

router = DefaultRouter()

router.register(r'user-types', UserTypeViewSet) #localhost:8080//api/user-types
router.register(r'users', UserViewSet) #localhost:8080//api/users
router.register(r'taxonomic-levels', TaxonomicLevelViewSet) #localhost:8080//api/taxonomit-levels
router.register(r'organism-conservation', OrganismConservationViewSet) #localhost:8080//api/
router.register(r'departamentos', DepartamentoViewSet) #localhost:8080//api/
router.register(r'municipios', MunicipioViewSet) #localhost:8080//api/

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/', include(router.urls)),
]
