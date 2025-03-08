# base
# installed
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
# local
from dj_backend.apps.modules import serializers
from dj_backend.apps.modules.services import db
from dj_backend.apps.modules.services import selectors


class OHISListCreateView(APIView):
    def get(self, request: Request, patient_id: int):
        """
        Получение списка
        """
        list_indexes = selectors.ohis_indexes_get_list(patient_id)
        data = serializers.IndexOutputDetailSerializer(data=list_indexes, many=True).data

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request: Request, patient_id: int):
        """
        Создание
        """
        serializer = serializers.IndexInputSerializer(request.data)
        serializer.is_valid(raise_exception=True)

        teeth = serializer.validated_data.get("teeth", None)
        db.ohis_create(teeth, patient_id)

        return Response("Успешный успех", status=status.HTTP_201_CREATED)