# base
# installed
from rest_framework import serializers
# local
from apps.patients import models


class PatientOutputDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = "__all__"


class PatientInputCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = "__all__"
