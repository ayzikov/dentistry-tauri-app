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


class AppointmentPhotoListCreateView(APIView):
    def get(self, request: Request, patient_id: int):
        """ Получение всех фотографий пациента """
        list_photos = crud.appointment_photos_get_list(patient_id)
        data = serializers.PhotoOutputSerializer(instance=list_photos, many=True).data

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request: Request, patient_id: int):
        """ Добавление фотографий пациента """

        serializer = serializers.PhotoInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        image = serializer.validated_data.get("image", None)
        crud.appointment_photo_create(image, patient_id)

        redirect_url = reverse("patient:detail_update_delete", args=[patient_id])
        return redirect(redirect_url)