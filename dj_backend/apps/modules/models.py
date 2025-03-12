# base
# installed
from django.db import models
# local
# from apps.modules.services.models_functions import get_teeth_dict
from apps.modules.services.models_functions import get_teeth_dict

class BaseModel(models.Model):
    """ Базовый класс для всех модулей """
    patient = models.ForeignKey(to="patients.Patient", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, verbose_name="дата записи")
    time = models.TimeField(auto_now_add=True, verbose_name="время записи")

    class Meta:
        get_latest_by = ["date", "time"]
        ordering = ["-date", "-time"]


class BaseIndexModel(BaseModel):
    """ Базовый класс для индексов """
    value = models.FloatField(verbose_name="результат вычисления индекса")


class IndexOHIS(BaseIndexModel):
    """ Индекс OHIS """
    pass


class IndexPI(BaseIndexModel):
    """ Индекс ПИ """
    pass


class IndexPMA(BaseIndexModel):
    """ Индекс PMA """
    pass


class IndexCPITN(BaseIndexModel):
    """ Индекс CPITN """
    pass


class IndexCPU(BaseIndexModel):
    """ Индекс КПУ """
    pass


class TeethFormulaModel(BaseModel):
    """ Модель зубов с буквами """
    teeth = models.JSONField(default=get_teeth_dict, verbose_name="json с буквой каждого зуба")


class AppointmentPhoto(BaseModel):
    """ Фотографии с приема """
    image = models.ImageField(verbose_name="фотография с приема")