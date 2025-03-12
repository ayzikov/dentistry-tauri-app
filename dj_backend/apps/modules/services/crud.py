# base
# installed
from django.core.exceptions import ValidationError
from django.db.models import Model
# local
from apps.modules import models
from apps.modules.services import calculations
from apps.modules.services import models_functions
from services import db



def indexes_get_list(patient_id: int, index_name: str):
    """
    Возвращает список рассчитанных индексов для пациента.
    :param patient_id: id пациента
    :param index_name: название индекса
    :return: список моделей индексов
    """

    # indexes_names_dict - словарь {название_индекса: модель_индекса}
    # берется значение(модель индекса) по ключу передаваемому в параметре index_name
    indexes_names_dict = db.get_indexes_dict()

    index_model = indexes_names_dict.get(index_name.lower(), None)
    if index_model is None:
        raise ValidationError(f"Неверно передан параметр index_name. "
                              f"Допустимые значения - {list(indexes_names_dict.keys())}")

    return db.get_objects_list(index_model, patient_id=patient_id)

# OHIS
def ohis_create(teeth: dict, patient_id: int) -> Model:
    """
    Создание индекса OHIS
    :param teeth: словарь с номерами зубов и выставленными баллами
    :param patient_id: id пациента
    :return: Созданный объект
    """
    index = calculations.ohis_calculate(teeth)
    return db.create_object(models.IndexOHIS, patient_id=patient_id, value=index)


# PI
def pi_create(teeth: dict, patient_id: int) -> Model:
    """
    Создание индекса PI
    :param teeth: словарь с номерами зубов и выставленными баллами
    :param patient_id: id пациента
    :return: Созданный объект
    """
    index = calculations.pi_calculate(teeth)
    return db.create_object(models.IndexPI, patient_id=patient_id, value=index)


# PMA
def pma_create(teeth: dict, patient_id: int) -> Model:
    """
    Создание индекса PMA
    :param teeth: словарь с номерами зубов и выставленными баллами
    :param patient_id: id пациента
    :return: Созданный объект
    """
    index = calculations.pma_calculate(teeth)
    return db.create_object(models.IndexPMA, patient_id=patient_id, value=index)


# CPITN
def cpitn_create(teeth: dict, patient_id: int) -> Model:
    """
    Создание индекса CPITN
    :param teeth: словарь с номерами зубов и выставленными баллами
    :param patient_id: id пациента
    :return: Созданный объект
    """
    index = calculations.cpitn_calculate(teeth)
    return db.create_object(models.IndexCPITN, patient_id=patient_id, value=index)


# CPU
def cpu_create(teeth: dict, patient_id: int) -> Model:
    """
    Создание индекса CPU
    :param teeth: словарь с номерами зубов и выставленными баллами
    :param patient_id: id пациента
    :return: Созданный объект
    """
    index = calculations.cpu_calculate(teeth)
    return db.create_object(models.IndexCPU, patient_id=patient_id, value=index)


# TEETH FORMULA
def teeth_formulas_get_list(patient_id: int, **kwargs) -> list:
    """
    :param patient_id: id пациента
    Можно передать в аргументы order_by со строковым значением сортировки.
    Например order_by="-date"
    """
    return db.get_objects_list(models.TeethFormulaModel, patient_id=patient_id)


def teeth_formula_create(teeth: dict, patient_id: int) -> Model:
    """
    Создание зубной формулы
    :param teeth: словарь с номерами зубов и выставленными буквами
    :param patient_id: id пациента
    :return: Созданный объект
    """


    # в словарь teeth_dict модели вставляются буквы в значения тех зубов, которые передал клиент
    # остальные значения остаются пустыми
    teeth_dict = models_functions.get_teeth_dict()
    for key, value in teeth.items():
        if key not in teeth_dict.keys():
            raise ValidationError(f"{key} некорректный ключ")
        teeth_dict[key] = value

    return db.create_object(models.TeethFormulaModel, patient_id=patient_id, teeth=teeth_dict)


# IMAGE
def appointment_photos_get_list(patient_id: int, **kwargs) -> list:
    """
    :param patient_id: id пациента
    Можно передать в аргументы order_by со строковым значением сортировки.
    Например order_by="-date"
    """
    return db.get_objects_list(models.AppointmentPhoto, patient_id=patient_id)


def appointment_photo_create(image, patient_id: int) -> Model:
    """
    Создание фотографии
    :param image: изображение
    :param patient_id: id пациента
    :return: Созданный объект
    """
    return db.create_object(models.AppointmentPhoto, patient_id=patient_id, image=image)
