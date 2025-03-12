# base
import datetime
import json
# installed
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# local
from apps.modules import models
from apps.modules.services import calculations
from apps.modules.services import crud
from services import db, factories_tests


class IndexesViewsTest(APITestCase):
    def setUp(self):
        self.ohis_list_create_url = reverse("modules:ohis:list_create", args=[1])
        self.pi_list_create_url = reverse("modules:pi:list_create", args=[1])
        self.pma_list_create_url = reverse("modules:pma:list_create", args=[1])
        self.cpitn_list_create_url = reverse("modules:cpitn:list_create", args=[1])
        self.cpu_list_create_url = reverse("modules:cpu:list_create", args=[1])
        self.teeth_formula_list_create_url = reverse("modules:teeth_formula:list_create", args=[1])

        self.teeth = {"t_11": 1, "t_41": 2, "t_18": 3, "t_32": 1, "t_25": 1}
        self.teeth_json = json.dumps(self.teeth)
        self.patient = factories_tests.PatientFactory()

    def test_ohis_views(self):
        # POST запрос на создание индекса
        create_response = self.client.post(
            path=self.ohis_list_create_url,
            data={"teeth": self.teeth_json},
        )

        # проверка редиректа
        self.assertEqual(create_response.status_code, status.HTTP_302_FOUND)
        # проверка создания индекса, вычисленного значения и даты
        index_obj = db.get_object(models.IndexOHIS, id=1)

        index_value = index_obj.value
        index_date = index_obj.date

        now_date = datetime.date.today()
        value = calculations.ohis_calculate(self.teeth)

        self.assertEqual(value, index_value)
        self.assertEqual(now_date, index_date)

        # проверка эндпоинта получения списка индексов
        get_list_response = self.client.get(
            path=self.ohis_list_create_url
        )

        self.assertEqual(get_list_response.status_code, status.HTTP_200_OK)
        db_list_indexes = crud.ohis_indexes_get_list(patient_id=1)
        self.assertEqual(len(db_list_indexes), len(get_list_response.data))


    def test_pi_views(self):
        # POST запрос на создание индекса
        create_response = self.client.post(
            path=self.pi_list_create_url,
            data={"teeth": self.teeth_json},
        )

        # проверка редиректа
        self.assertEqual(create_response.status_code, status.HTTP_302_FOUND)
        # проверка создания индекса, вычисленного значения и даты
        index_obj = db.get_object(models.IndexPI, id=1)

        index_value = index_obj.value
        index_date = index_obj.date

        now_date = datetime.date.today()
        value = calculations.pi_calculate(self.teeth)

        self.assertEqual(value, index_value)
        self.assertEqual(now_date, index_date)

        # проверка эндпоинта получения списка индексов
        get_list_response = self.client.get(
            path=self.pi_list_create_url
        )

        self.assertEqual(get_list_response.status_code, status.HTTP_200_OK)
        db_list_indexes = crud.pi_indexes_get_list(patient_id=1)
        self.assertEqual(len(db_list_indexes), len(get_list_response.data))


    def test_pma_views(self):
        # POST запрос на создание индекса
        create_response = self.client.post(
            path=self.pma_list_create_url,
            data={"teeth": self.teeth_json},
        )

        # проверка редиректа
        self.assertEqual(create_response.status_code, status.HTTP_302_FOUND)
        # проверка создания индекса, вычисленного значения и даты
        index_obj = db.get_object(models.IndexPMA, id=1)

        index_value = index_obj.value
        index_date = index_obj.date

        now_date = datetime.date.today()
        value = calculations.pma_calculate(self.teeth)

        self.assertEqual(value, index_value)
        self.assertEqual(now_date, index_date)

        # проверка эндпоинта получения списка индексов
        get_list_response = self.client.get(
            path=self.pma_list_create_url
        )

        self.assertEqual(get_list_response.status_code, status.HTTP_200_OK)
        db_list_indexes = crud.pma_indexes_get_list(patient_id=1)
        self.assertEqual(len(db_list_indexes), len(get_list_response.data))


    def test_cpitn_views(self):
        # POST запрос на создание индекса
        create_response = self.client.post(
            path=self.cpitn_list_create_url,
            data={"teeth": self.teeth_json},
        )

        # проверка редиректа
        self.assertEqual(create_response.status_code, status.HTTP_302_FOUND)
        # проверка создания индекса, вычисленного значения и даты
        index_obj = db.get_object(models.IndexCPITN, id=1)

        index_value = index_obj.value
        index_date = index_obj.date

        now_date = datetime.date.today()
        value = calculations.cpitn_calculate(self.teeth)

        self.assertEqual(value, index_value)
        self.assertEqual(now_date, index_date)

        # проверка эндпоинта получения списка индексов
        get_list_response = self.client.get(
            path=self.cpitn_list_create_url
        )

        self.assertEqual(get_list_response.status_code, status.HTTP_200_OK)
        db_list_indexes = crud.cpitn_indexes_get_list(patient_id=1)
        self.assertEqual(len(db_list_indexes), len(get_list_response.data))


    def test_cpu_views(self):
        # POST запрос на создание индекса
        create_response = self.client.post(
            path=self.cpu_list_create_url,
            data={"teeth": self.teeth_json},
        )

        # проверка редиректа
        self.assertEqual(create_response.status_code, status.HTTP_302_FOUND)
        # проверка создания индекса, вычисленного значения и даты
        index_obj = db.get_object(models.IndexCPU, id=1)

        index_value = index_obj.value
        index_date = index_obj.date

        now_date = datetime.date.today()
        value = calculations.cpu_calculate(self.teeth)

        self.assertEqual(value, index_value)
        self.assertEqual(now_date, index_date)

        # проверка эндпоинта получения списка индексов
        get_list_response = self.client.get(
            path=self.cpu_list_create_url
        )

        self.assertEqual(get_list_response.status_code, status.HTTP_200_OK)
        db_list_indexes = crud.cpu_indexes_get_list(patient_id=1)
        self.assertEqual(len(db_list_indexes), len(get_list_response.data))


    def test_teeth_formula_views(self):
        # POST запрос на создание индекса
        create_response = self.client.post(
            path=self.teeth_formula_list_create_url,
            data={"teeth": self.teeth_json},
        )

        # проверка редиректа
        self.assertEqual(create_response.status_code, status.HTTP_302_FOUND)
        # проверка создания и даты
        index_obj = db.get_object(models.TeethFormulaModel, id=1)

        index_date = index_obj.date
        now_date = datetime.date.today()

        self.assertEqual(now_date, index_date)

        # проверка эндпоинта получения списка формул
        get_list_response = self.client.get(
            path=self.teeth_formula_list_create_url
        )

        self.assertEqual(get_list_response.status_code, status.HTTP_200_OK)
        db_list_indexes = crud.teeth_formulas_get_list(patient_id=1)
        self.assertEqual(len(db_list_indexes), len(get_list_response.data))


# python manage.py test apps.modules.tests.test_views.test_indexes.IndexesViewsTest