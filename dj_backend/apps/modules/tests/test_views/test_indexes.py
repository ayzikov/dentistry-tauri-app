# base
import datetime
import json
# installed
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# local
from apps.modules import models
from apps.modules.services import factories_tests
from apps.modules.services import calculations
from apps.modules.services import db



class ProviderViewsTest(APITestCase):
    def setUp(self):
        self.list_create_url = reverse("modules:ohis:list_create", args=[1])

        self.teeth = {"t_11": 1, "t_41": 2, "t_18": 3, "t_32": 1, "t_25": 1}
        self.teeth_json = json.dumps(self.teeth)
        self.patient = factories_tests.PatientFactory()

    def test_ohis_views(self):
        # POST запрос на создание индекса
        create_response = self.client.post(
            path=self.list_create_url,
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


# python manage.py test apps.modules.tests.test_views.test_indexes.ProviderViewsTest