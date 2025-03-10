# base
# installed
from django.core.exceptions import ValidationError
from django.db.models import Model
# local
from apps.modules import models
from apps.modules.services import calculations


def create_object(model, **kwargs) -> Model:
    """
    Создает объект модели.
    :param model: Модель Django
    :param kwargs: Данные для создания объекта
    :return: Созданный объект
    :raises ValidationError: Если данные невалидны
    """
    try:
        obj = model.objects.create(**kwargs)
        return obj
    except Exception as e:
        raise ValidationError(f"Ошибка при создании объекта: {str(e)}")


def update_object(model, **kwargs) -> Model:
    """
    Обновляет объект модели.
    :param model: Модель Django
    :param kwargs: Данные для обновления объекта
    :return: Созданный объект
    :raises ValidationError: Если данные невалидны
    """
    pass


def delete_object(model, **kwargs) -> bool:
    """
    Удаляет объект модели.
    :param model: Модель Django
    :param kwargs: Данные для удаления объекта
    :return: True
    :raises ValidationError: Если данные невалидны
    """
    pass
#=======================================================================================================================


# CREATE
def ohis_create(teeth: dict, patient_id: int) -> Model:
    """
    Создание индекса OHIS
    :param teeth: словарь с номерами зубов и выставленными баллами
    :param patient_id: id пациента
    :return: Созданный объект
    """
    index = calculations.ohis_calculate(teeth)
    return create_object(models.IndexOHIS, patient_id=patient_id, value=index)


def pi_create(teeth: dict, patient_id: int) -> Model:
    """
    Создание индекса PI
    :param teeth: словарь с номерами зубов и выставленными баллами
    :param patient_id: id пациента
    :return: Созданный объект
    """
    index = calculations.pi_calculate(teeth)
    return create_object(models.IndexPI, patient=patient_id, value=index)


def pma_create(teeth: dict, patient_id: int) -> Model:
    """
    Создание индекса PMA
    :param teeth: словарь с номерами зубов и выставленными баллами
    :param patient_id: id пациента
    :return: Созданный объект
    """
    index = calculations.pma_calculate(teeth)
    return create_object(models.IndexPMA, patient=patient_id, value=index)


def cpitn_create(teeth: dict, patient_id: int) -> Model:
    """
    Создание индекса CPITN
    :param teeth: словарь с номерами зубов и выставленными баллами
    :param patient_id: id пациента
    :return: Созданный объект
    """
    index = calculations.cpitn_calculate(teeth)
    return create_object(models.IndexCPITN, patient=patient_id, value=index)


def cpu_create(teeth: dict, patient_id: int) -> Model:
    """
    Создание индекса CPU
    :param teeth: словарь с номерами зубов и выставленными баллами
    :param patient_id: id пациента
    :return: Созданный объект
    """
    index = calculations.cpu_calculate(teeth)
    return create_object(models.IndexCPU, patient=patient_id, value=index)


def teeth_formula_create(teeth: dict, patient_id: int) -> Model:
    """
    Создание зубной формулы
    :param teeth: словарь с номерами зубов и выставленными буквами
    :param patient_id: id пациента
    :return: Созданный объект
    """
    return create_object(models.TeethFormulaModel, patient=patient_id, teeth=teeth)


def appointment_photo_create(image, patient_id: int) -> Model:
    """
    Создание фотографии
    :param image: изображение
    :param patient_id: id пациента
    :return: Созданный объект
    """
    return create_object(models.AppointmentPhoto, patient=patient_id, image=image)
