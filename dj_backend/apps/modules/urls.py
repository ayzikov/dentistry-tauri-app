# base
# installed
from django.urls import path, include
# local
from apps.modules.views import ohis_views


ohis_patterns = [
    path("", ohis_views.OHISListCreateView.as_view(), name="list_create"),
]


urlpatterns = [
    path('patient/<int:patient_id>/ohis/', include((ohis_patterns, 'ohis'))),
]


app_name = 'modules'