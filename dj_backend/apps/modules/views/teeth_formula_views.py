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
from apps.modules.services.api_doc import TeethFormulaAPIDoc



class TeethFormulaListCreateView(APIView):
    def get(self, request: Request, patient_id: int):
        """
        Получение списка
        """
        list_teeth_formulas = crud.teeth_formulas_get_list(patient_id)
        data = serializers.TeethFormulaOutputDetailSerializer(instance=list_teeth_formulas, many=True).data

        return Response(data, status=status.HTTP_200_OK)

    @TeethFormulaAPIDoc.create_teeth_formula
    def post(self, request: Request, patient_id: int):
        """
        Создание
        """
        serializer = serializers.TeethFormulaInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        teeth = serializer.validated_data.get("teeth", None)
        crud.teeth_formula_create(teeth, patient_id)

        # делаем редирект на получение списка зубных формул
        redirect_url = reverse("modules:teeth_formula:list_create", args=[patient_id])
        return redirect(redirect_url)