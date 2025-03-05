from django.db import models


class BaseModel(models.Model):
    """ Базовый класс для всех модулей """
    patient = models.ForeignKey(to="apps.patients.Patient", on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="дата и время записи")


class BaseIndexModel(BaseModel):
    """ Базовый класс для индексов """
    value = models.IntegerField(verbose_name="результат вычисления индекса")


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


class TeethLettersModel(BaseModel):
    """ Модель зубов с буквами """
    teeth = models.JSONField(default={"t_11": " ", "t_12": " ", "t_13": " ", "t_14": " ", "t_15": " ", "t_16": " ",
                                      "t_17": " ", "t_18": " ", "t_21": " ", "t_22": " ", "t_23": " ", "t_24": " ",
                                      "t_25": " ", "t_26": " ", "t_27": " ", "t_28": " ", "t_31": " ", "t_32": " ",
                                      "t_33": " ", "t_34": " ", "t_35": " ", "t_36": " ", "t_37": " ", "t_38": " ",
                                      "t_41": " ", "t_42": " ", "t_43": " ", "t_44": " ", "t_45": " ", "t_46": " ",
                                      "t_47": " ", "t_48": " ", }, verbose_name="json с буквой каждого зуба")


class AppointmentPhoto(BaseModel):
    """ Фотографии с приема """
    photo = models.ImageField(verbose_name="фотография с приема")