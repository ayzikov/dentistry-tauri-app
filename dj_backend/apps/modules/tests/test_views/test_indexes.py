# base
import datetime
# installed
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# local
from dj_backend.apps.modules import models
from dj_backend.apps.modules.services import factories_tests
from dj_backend.apps.modules.services import calculations
from dj_backend.apps.modules.services import selectors



class ProviderViewsTest(APITestCase):
    def setUp(self):
        self.list_create_url = reverse("modules:ohis:list_create", args=[1])

        self.teeth = {"t_11": 1, "t_41": 2, "t_18": 3, "t_32": 1, "t_25": 1}
        self.patient = factories_tests.PatientFactory()

    def test_ohis_views(self):
        # POST запрос на создание индекса
        create_response = self.client.post(
            path=self.list_create_url,
            data={"teeth": self.teeth}
        )

        # проверка редиректа
        self.assertEqual(create_response.status_code, status.HTTP_303_SEE_OTHER)
        # проверка создания индекса, вычисленного значения и даты
        index_obj = selectors.get_object(models.IndexOHIS, id=1)
        index_value = index_obj.value
        index_date = index_obj.date

        now_date = datetime.date.today()
        value = calculations.ohis_calculate(self.teeth)

        self.assertEqual(value, index_value)
        self.assertEqual(now_date, index_date)