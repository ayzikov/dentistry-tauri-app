from django.urls import path, include


urlpatterns = [
    path('module/', include("apps.modules.urls", namespace="modules")),
    # path('patient/', include("apps.patients.urls", namespace="patients")),
]
