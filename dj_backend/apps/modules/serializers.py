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