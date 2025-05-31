# base
import json
# installed
from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict
from django_extensions.db.fields.json import JSONDict
# local
from apps.modules import models as modules_models
from apps.patients import models as patients_models
from services import db


def patient_index_last_get(patient_id: int, index_name: str) -> int | None:
    """
    Возвращает последний рассчитанный индекс для пациента.
    Если пациенту еще никогда не рассчитывали индекс - возвращается None
    :param patient_id: id пациента
    :param index_name: название индекса
    :return: значение последнего рассчитанного индекса
    """

    # indexes_names_dict - словарь {название_индекса: модель_индекса}
    # берется значение(модель индекса) по ключу передаваемому в параметре index_name
    # далее с помощью функции get_last_created_object получаем модель последнего рассчитанного индекса для пациента
    indexes_names_dict = db.get_indexes_dict()

    index_model = indexes_names_dict.get(index_name.lower(), None)
    if index_model is None:
        raise ValidationError(f"Неверно передан параметр index_name. "
                              f"Допустимые значения - {list(indexes_names_dict.keys())}")

    index = db.get_last_created_object(index_model, patient_id=patient_id)
    if index is not None:
        return index.value
    return None


def patient_all_info_get(patient_id: int):
    """
    Функция собирает в один словарь значения полей модели пациента и значения последних рассчитанных для него индексов
    :param patient_id: id пациента
    :return: словарь со значениями полей модели пациента + значения последних рассчитанных индексов
    """

    result_dict = dict()

    # получаем объект пациента и преобразуем его данные в dict и добавляем в result_dict
    patient_obj = db.get_object(patients_models.Patient, id=patient_id)
    patient_dict = model_to_dict(patient_obj)
    patient_dict["registration_date"] = patient_obj.registration_date
    result_dict["patient"] = patient_dict

    # indexes_names_dict - словарь {название_индекса: модель_индекса}
    # циклом проходим по именам индексов вызывая функцию patient_index_last_get для каждого индекса
    # добавляем в итоговый словарь ключ-index_name_value: значение-index.value
    indexes_names_dict = db.get_indexes_dict()
    for index_name in indexes_names_dict.keys():
        result_dict[f"{index_name}_value"] = patient_index_last_get(patient_id=patient_id, index_name=index_name)

    return result_dict


def patients_get_list():
    """ Список моделей всех пациентов """
    return db.get_objects_list(patients_models.Patient)


def patient_create(**kwargs):
    """
    Создание пациента
    :param kwargs: сериализованные валидированные данные для создания
    :return: объект модели созданного пациента
    """
    patient = db.create_object(patients_models.Patient, **kwargs)
    return patient
