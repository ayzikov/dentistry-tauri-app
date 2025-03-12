# base
# installed
from django.urls import path
# local
from apps.patients import views


urlpatterns = [
    path("", views.PatientListCreateView.as_view(), name="list_create"),
    path("<int:patient_id>/", views.PatientDetailUpdateDeleteView.as_view(), name="detail_update_delete"),
]


app_name = 'patient'