# base
# installed
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# local


class IndexAPIDoc:
    create_index = swagger_auto_schema(
    operation_description="Создание нового индекса",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'teeth': openapi.Schema(type=openapi.TYPE_STRING, description='json с номерами зубов и выставленными баллами\n'
                                                                          '{"t_11": 3, "t_23": 1}'),
        },
        required=['teeth']
    ),
    responses={
        302: openapi.Response('Индекс успешно создан'),
        400: openapi.Response('Некорректные данные'),
    }
)


class TeethFormulaAPIDoc:
    create_teeth_formula = swagger_auto_schema(
    operation_description="Создание новой зубной формулы",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'teeth': openapi.Schema(type=openapi.TYPE_STRING, description='json с номерами зубов и буквами\n'
                                                                          '{"t_11": "О", "t_23": "П"}'),
        },
        required=['teeth']
    ),
    responses={
        302: openapi.Response('Зубная формула успешно создана'),
        400: openapi.Response('Некорректные данные'),
    }
)