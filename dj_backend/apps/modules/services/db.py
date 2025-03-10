# base
# installed
from django.db.models import Model
from django.http import Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.exceptions import ValidationError
# local


def get_object(model, **kwargs):
    """ Получение объекта """
    try:
        # если был передан параметр сортировки
        if "order_by" in kwargs:
            order = kwargs.get("order_by")
            return get_object_or_404(model.objects.order_by(order), **kwargs)
        return get_object_or_404(model, **kwargs)
    except Http404:
        return None


def get_objects_list(model, **kwargs):
    """ Получение списка объектов """
    try:
        # если был передан параметр сортировки
        if "order_by" in kwargs:
            order = kwargs.get("order_by")
            return get_list_or_404(model.objects.order_by(order), **kwargs)
        return get_list_or_404(model, **kwargs)
    except Http404:
        return []


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
