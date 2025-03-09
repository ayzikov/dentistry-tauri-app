# base
# installed
import factory
from faker import Faker
from factory.django import DjangoModelFactory
# local
from dj_backend.apps.patients import models


fake = Faker()


class PatientFactory(DjangoModelFactory):
    first_name = factory.LazyFunction(lambda: fake.first_name())
    last_name = factory.LazyFunction(lambda: fake.last_name())
    middle_name = factory.LazyFunction(lambda: fake.middle_name())
    birthdate = factory.LazyFunction(lambda: fake.date())
    other_info = factory.LazyFunction(lambda: fake.text(max_nb_chars=200))

    class Meta:
        model = models.patients.Patient