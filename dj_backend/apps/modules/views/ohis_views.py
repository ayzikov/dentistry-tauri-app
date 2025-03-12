# base
# installed
from django.urls import reverse
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
# local
from apps.modules import serializers
from apps.modules.services import crud
from apps.modules.services.api_doc import IndexAPIDoc


class OHISListCreateView(APIView):
    def get(self, request: Request, patient_id: int):
        """
        Получение списка
        """
        list_indexes = crud.indexes_get_list(patient_id, index_name="ohis")
        data = serializers.IndexOutputDetailSerializer(instance=list_indexes, many=True).data

        return Response(data, status=status.HTTP_200_OK)

    @IndexAPIDoc.create_index
    def post(self, request: Request, patient_id: int):
        """
        Создание
        """
        serializer = serializers.IndexInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        teeth = serializer.validated_data.get("teeth", None)
        crud.ohis_create(teeth, patient_id)

        # делаем редирект на получение списка индексов OHIS
        redirect_url = reverse("modules:ohis:list_create", args=[patient_id])
        return redirect(redirect_url)