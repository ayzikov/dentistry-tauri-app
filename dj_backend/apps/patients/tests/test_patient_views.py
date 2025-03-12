# base
# installed
from cgi import print_directory

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# local
from apps.patients.models import Patient
from services import factories_tests, db

class PatientViewsTest(APITestCase):
    def setUp(self):
        self.url_list_create = reverse("patients:list_create")
        self.url_detail_update_delete = reverse("patients:detail_update_delete", args=[1])

        self.patient_1 = factories_tests.PatientFactory.build()
        self.patient_2 = factories_tests.PatientFactory.build()

    def test_views(self):
        # проверка эндпоинта создания пациента
        # POST запрос на создание
        create_response_1 = self.client.post(
            path=self.url_list_create,
            data={
                "first_name": self.patient_1.first_name,
                "last_name": self.patient_1.last_name,
                "middle_name": self.patient_1.middle_name,
                "birthdate": self.patient_1.birthdate,
                "other_info": self.patient_1.other_info,
            }
        )

        # проверка редиректа
        self.assertEqual(status.HTTP_302_FOUND, create_response_1.status_code)

        # проверка наличия созданного объекта в БД
        db_patient = db.get_object(Patient, id=1)
        self.assertEqual(db_patient.first_name, self.patient_1.first_name)
        self.assertEqual(db_patient.last_name, self.patient_1.last_name)
        self.assertEqual(db_patient.middle_name, self.patient_1.middle_name)
        self.assertEqual(db_patient.birthdate.strftime("%Y-%m-%d"), self.patient_1.birthdate)
        self.assertEqual(db_patient.other_info, self.patient_1.other_info)

        # создание второго пациента
        patient_2 = factories_tests.PatientFactory()

        # проверка эндпоинта вывода списка пациентов
        get_list_response = self.client.get(
            path=self.url_list_create
        )
        self.assertEqual(len(get_list_response.data), 2)

        # проверка эндпоинта детальной информации о пациенте
        get_detail_response = self.client.get(
            path=self.url_detail_update_delete
        )
        self.assertIn("patient", get_detail_response.data)
        self.assertIn("ohis_value", get_detail_response.data)
        self.assertIn("pi_value", get_detail_response.data)
        self.assertIn("pma_value", get_detail_response.data)
        self.assertIn("cpitn_value", get_detail_response.data)
        self.assertIn("cpu_value", get_detail_response.data)


# python manage.py test apps.patients.tests.test_patient_views.PatientViewsTest