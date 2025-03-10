# base
# installed
from django.urls import path, include
# local
from apps.modules.views import (ohis_views,
                                pi_views,
                                pma_views,
                                cpitn_views,
                                cpu_views,
                                teeth_formula_views)


ohis_patterns = [
    path("", ohis_views.OHISListCreateView.as_view(), name="list_create"),
]


pi_patterns = [
    path("", pi_views.PIListCreateView.as_view(), name="list_create"),
]


pma_patterns = [
    path("", pma_views.PMAListCreateView.as_view(), name="list_create"),
]


cpitn_patterns = [
    path("", cpitn_views.CPITNListCreateView.as_view(), name="list_create"),
]


cpu_patterns = [
    path("", cpu_views.CPUListCreateView.as_view(), name="list_create"),
]


teeth_formula_patterns = [
    path("", teeth_formula_views.TeethFormulaListCreateView.as_view(), name="list_create"),
]


urlpatterns = [
    path('patient/<int:patient_id>/ohis/', include((ohis_patterns, 'ohis'))),
    path('patient/<int:patient_id>/pi/', include((pi_patterns, 'pi'))),
    path('patient/<int:patient_id>/pma/', include((pma_patterns, 'pma'))),
    path('patient/<int:patient_id>/cpitn/', include((cpitn_patterns, 'cpitn'))),
    path('patient/<int:patient_id>/cpu/', include((cpu_patterns, 'cpu'))),
    path('patient/<int:patient_id>/teeth-formula/', include((teeth_formula_patterns, 'teeth_formula'))),
]


app_name = 'modules'