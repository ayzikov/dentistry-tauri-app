from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=500, verbose_name="имя")
    last_name = models.CharField(max_length=500, verbose_name="фамилия")
    middle_name = models.CharField(max_length=500, verbose_name="отчество")
    birthdate = models.DateField(verbose_name="дата рождения")
    other_info = models.TextField(verbose_name="общая информация")
    registration_date = models.DateField(auto_now_add=True, verbose_name="дата регистрации")
