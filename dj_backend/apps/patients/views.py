# base
# installed
from django.urls import reverse
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
# local
from apps.patients import serializers
from apps.patients.services import crud


class PatientListCreateView(APIView):
    def get(self, request: Request):
        """ Получение списка """

        list_patients = crud.patients_get_list()
        data = serializers.PatientOutputDetailSerializer(instance=list_patients, many=True).data

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        """ Создание """

        serializer = serializers.PatientInputCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        crud.patient_create(**data)

        # делаем редирект на страницу со списком пациентов
        redirect_url = reverse("patients:list_create")
        return redirect(redirect_url)


class PatientDetailUpdateDeleteView(APIView):
    def get(self, request: Request, patient_id: int):
        """ Детальная информация """

        data = crud.patient_all_info_get(patient_id=patient_id)
        return Response(data, status=status.HTTP_200_OK)

    def patch(self, request: Request, patient_id: int):
        """ Частичное обновление """
        pass

    def delete(self, request: Request, patient_id: int):
        """ Удаление """
        pass