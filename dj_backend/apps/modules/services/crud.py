# base
# installed
from django.db.models import Model
# local
from apps.modules import models
from apps.modules.services import calculations
from apps.modules.services import db


# OHIS
def ohis_indexes_get_list(patient_id: int, **kwargs) -> list:
    """
    :param patient_id: id пациента
    Можно передать в аргументы order_by со строковым значением сортировки.
    Например order_by="-date"
    """
    return db.get_objects_list(models.IndexOHIS, patient=patient_id)


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
def pi_indexes_get_list(patient_id: int, **kwargs) -> list:
    """
    :param patient_id: id пациента
    Можно передать в аргументы order_by со строковым значением сортировки.
    Например order_by="-date"
    """
    return db.get_objects_list(models.IndexPI, patient=patient_id)


def pi_create(teeth: dict, patient_id: int) -> Model:
    """
    Создание индекса PI
    :param teeth: словарь с номерами зубов и выставленными баллами
    :param patient_id: id пациента
    :return: Созданный объект
    """
    index = calculations.pi_calculate(teeth)
    return db.create_object(models.IndexPI, patient=patient_id, value=index)


# PMA
def pma_indexes_get_list(patient_id: int, **kwargs) -> list:
    """
    :param patient_id: id пациента
    Можно передать в аргументы order_by со строковым значением сортировки.
    Например order_by="-date"
    """
    return db.get_objects_list(models.IndexPMA, patient=patient_id)


def pma_create(teeth: dict, patient_id: int) -> Model:
    """
    Создание индекса PMA
    :param teeth: словарь с номерами зубов и выставленными баллами
    :param patient_id: id пациента
    :return: Созданный объект
    """
    index = calculations.pma_calculate(teeth)
    return db.create_object(models.IndexPMA, patient=patient_id, value=index)


# CPITN
def cpitn_indexes_get_list(patient_id: int, **kwargs) -> list:
    """
    :param patient_id: id пациента
    Можно передать в аргументы order_by со строковым значением сортировки.
    Например order_by="-date"
    """
    return db.get_objects_list(models.IndexCPITN, patient=patient_id)


def cpitn_create(teeth: dict, patient_id: int) -> Model:
    """
    Создание индекса CPITN
    :param teeth: словарь с номерами зубов и выставленными баллами
    :param patient_id: id пациента
    :return: Созданный объект
    """
    index = calculations.cpitn_calculate(teeth)
    return db.create_object(models.IndexCPITN, patient=patient_id, value=index)


# CPU
def cpu_indexes_get_list(patient_id: int, **kwargs) -> list:
    """
    :param patient_id: id пациента
    Можно передать в аргументы order_by со строковым значением сортировки.
    Например order_by="-date"
    """
    return db.get_objects_list(models.IndexCPU, patient=patient_id)


def cpu_create(teeth: dict, patient_id: int) -> Model:
    """
    Создание индекса CPU
    :param teeth: словарь с номерами зубов и выставленными баллами
    :param patient_id: id пациента
    :return: Созданный объект
    """
    index = calculations.cpu_calculate(teeth)
    return db.create_object(models.IndexCPU, patient=patient_id, value=index)


# TEETH FORMULA
def teeth_formulas_get_list(patient_id: int, **kwargs) -> list:
    """
    :param patient_id: id пациента
    Можно передать в аргументы order_by со строковым значением сортировки.
    Например order_by="-date"
    """
    return db.get_objects_list(models.TeethFormulaModel, patient=patient_id)


def teeth_formula_create(teeth: dict, patient_id: int) -> Model:
    """
    Создание зубной формулы
    :param teeth: словарь с номерами зубов и выставленными буквами
    :param patient_id: id пациента
    :return: Созданный объект
    """
    return db.create_object(models.TeethFormulaModel, patient=patient_id, teeth=teeth)


# IMAGE
def appointment_photos_get_list(patient_id: int, **kwargs) -> list:
    """
    :param patient_id: id пациента
    Можно передать в аргументы order_by со строковым значением сортировки.
    Например order_by="-date"
    """
    return db.get_objects_list(models.AppointmentPhoto, patient=patient_id)


def appointment_photo_create(image, patient_id: int) -> Model:
    """
    Создание фотографии
    :param image: изображение
    :param patient_id: id пациента
    :return: Созданный объект
    """
    return db.create_object(models.AppointmentPhoto, patient=patient_id, image=image)
