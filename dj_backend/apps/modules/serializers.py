# base
# installed
from rest_framework import serializers
# local
from apps.modules import models


# INDEXES
class IndexOutputDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BaseIndexModel
        fields = "__all__"


class IndexInputSerializer(serializers.Serializer):
    teeth = serializers.JSONField()


# TEETH FORMULA
class TeethFormulaOutputDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeethFormulaModel
        fields = "__all__"


class TeethFormulaInputSerializer(serializers.Serializer):
    teeth = serializers.JSONField()


# AppointmentPhoto
class PhotoInputSerializer(serializers.Serializer):
    image = serializers.FileField()


class PhotoOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AppointmentPhoto
        fields = "__all__"