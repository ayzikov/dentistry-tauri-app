# base
# installed
from django.http import Http404
from django.shortcuts import get_object_or_404, get_list_or_404
# local
from dj_backend.apps.modules import models


def get_object(model_or_qs, **kwargs):
    """ Получение объекта """
    try:
        return get_object_or_404(model_or_qs, **kwargs)
    except Http404:
        return None


def get_objects_list(model_or_qs, **kwargs):
    """ Получение списка объектов """
    try:
        return get_list_or_404(model_or_qs, **kwargs)
    except Http404:
        return []
#=======================================================================================================================

# получение каждого индекса (список с индексами одного типа) для пациента
def ohis_indexes_get_list(patient_id: int, order_by: str = "-datetime", **kwargs) -> list:
    """
    :param patient_id: id пациента
    :param order_by: по умолчанию сортируется начиная с самых новых,
    другие варианты сортировки:
    order_by="value" - сортировка по значению
    """
    return get_objects_list(models.IndexOHIS.objects.order_by(order_by), patient=patient_id)


def pi_indexes_get_list(patient_id: int, order_by: str = "-datetime", **kwargs) -> list:
    """
    :param patient_id: id пациента
    :param order_by: по умолчанию сортируется начиная с самых новых,
    другие варианты сортировки:
    order_by="value" - сортировка по значению
    """
    return get_objects_list(models.IndexPI.objects.order_by(order_by), patient=patient_id)


def pma_indexes_get_list(patient_id: int, order_by: str = "-datetime", **kwargs) -> list:
    """
    :param patient_id: id пациента
    :param order_by: по умолчанию сортируется начиная с самых новых,
    другие варианты сортировки:
    order_by="value" - сортировка по значению
    """
    return get_objects_list(models.IndexPMA.objects.order_by(order_by), patient=patient_id)


def cpitn_indexes_get_list(patient_id: int, order_by: str = "-datetime", **kwargs) -> list:
    """
    :param patient_id: id пациента
    :param order_by: по умолчанию сортируется начиная с самых новых,
    другие варианты сортировки:
    order_by="value" - сортировка по значению
    """
    return get_objects_list(models.IndexCPITN.objects.order_by(order_by), patient=patient_id)


def cpu_indexes_get_list(patient_id: int, order_by: str = "-datetime", **kwargs) -> list:
    """
    :param patient_id: id пациента
    :param order_by: по умолчанию сортируется начиная с самых новых,
    другие варианты сортировки:
    order_by="value" - сортировка по значению
    """
    return get_objects_list(models.IndexCPU.objects.order_by(order_by), patient=patient_id)
#=======================================================================================================================


# получение списка всех индексов для определенного пациента
def list_all_indexes_get_list(patient_id: int, order_by: str = "-datetime", **kwargs) -> dict:
    pass
# получение списка всех челюстей с буквами определенного пациента



