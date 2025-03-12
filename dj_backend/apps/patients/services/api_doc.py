# base
# installed
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# local


class PatientAPIDoc:
    create_patient = swagger_auto_schema(
    operation_description="Создание пациента",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='Имя'),
            'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Фамилия'),
            'middle_name': openapi.Schema(type=openapi.TYPE_STRING, description='Отчество'),
            'birthdate': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, description='Дата рождения'),
            'other_info': openapi.Schema(type=openapi.TYPE_STRING, description='Дополнительная информация'),
        },
        required=['first_name', 'last_name', 'middle_name', 'birthdate', 'other_info']
    ),
    responses={
        302: openapi.Response('Индекс успешно создан'),
        400: openapi.Response('Некорректные данные'),
    }
)

    list_patients_docs = openapi.Schema(
        type=openapi.TYPE_ARRAY,
        items=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID пациента'),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='Имя пациента'),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Фамилия пациента'),
                'middle_name': openapi.Schema(type=openapi.TYPE_STRING, description='Отчество пациента'),
                'birthdate': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE,
                                            description='Дата рождения пациента'),
                'other_info': openapi.Schema(type=openapi.TYPE_STRING,
                                             description='Дополнительная информация о пациенте'),
                'registration_date': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE,
                                                    description='Дата регистрации пациента'),
            }
        )
    )


    get_list_patients = swagger_auto_schema(
        operation_description="Получить список пациентов",
        responses={
            200: openapi.Response('Список пациентов', list_patients_docs),
            404: openapi.Response('Пациенты не найдены'),
        }
    )

    detail_patient_docs = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'patient': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID пациента'),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='Имя пациента'),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Фамилия пациента'),
                'middle_name': openapi.Schema(type=openapi.TYPE_STRING, description='Отчество пациента'),
                'birthdate': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, description='Дата рождения пациента'),
                'other_info': openapi.Schema(type=openapi.TYPE_STRING, description='Дополнительная информация о пациенте'),
            }
        ),
        'ohis_value': openapi.Schema(type=openapi.TYPE_NUMBER, description='Значение индекса OHIS'),
        'pi_value': openapi.Schema(type=openapi.TYPE_NUMBER, description='Значение индекса PI', nullable=True),
        'pma_value': openapi.Schema(type=openapi.TYPE_NUMBER, description='Значение индекса PMA', nullable=True),
        'cpitn_value': openapi.Schema(type=openapi.TYPE_NUMBER, description='Значение индекса CPITN', nullable=True),
        'cpu_value': openapi.Schema(type=openapi.TYPE_NUMBER, description='Значение индекса CPU', nullable=True),
    }
)

    get_detail_patient = swagger_auto_schema(
    operation_description="Получить детальную информацию о пациенте и его индексах",
    responses={
        200: openapi.Response('Детальная информация о пациенте', detail_patient_docs),
        404: openapi.Response('Пациент не найден'),
    }
)

