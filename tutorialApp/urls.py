from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers

from tutorialApp import views
from tutorialApp.viewSets import TutorialesViewSet

router = routers.DefaultRouter()
router.register(r'^tutos', TutorialesViewSet)

urlpatterns = [
    url(r'^api/tutoriales$', views.listaTutoriales),
    url(r'^api/tutoriales/(?P<pk>[0-9]+)$', views.tutorial),
    url(r'^api/tutoriales/publicados$', views.listaTutorialesPublicados),
]

# Añadimos las rutas creadas por el Router
urlpatterns.append(
    path('', include(router.urls))
)
