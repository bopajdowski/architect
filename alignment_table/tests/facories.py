# -*- coding: utf-8 -*-

import factory
# Django
import datetime

from factory.fuzzy import FuzzyDateTime
from pytz import UTC

from ..models import AlignmentTable, AlignmentDateTable, AlignmentStringTable



class AlignmentTableFactory(factory.DjangoModelFactory):

    date_modified = FuzzyDateTime(
        datetime.datetime(2008, 1, 1, tzinfo=UTC),
        datetime.datetime(2019, 12, 31, tzinfo=UTC),
    )
    energy_id = factory.Faker('sentence', nb_words=5)

    class Meta:
        model = AlignmentTable


class AlignmentDateTableFactory(factory.DjangoModelFactory):

    date_modified = FuzzyDateTime(
        datetime.datetime(2008, 1, 1, tzinfo=UTC),
        datetime.datetime(2019, 12, 31, tzinfo=UTC),
    )
    energy_id = factory.Faker('sentence', nb_words=5)

    class Meta:
        model = AlignmentDateTable


class AlignmentStringTableFactory(factory.DjangoModelFactory):

    date_modified = FuzzyDateTime(
        datetime.datetime(2008, 1, 1, tzinfo=UTC),
        datetime.datetime(2019, 12, 31, tzinfo=UTC),
    )
    energy_id = factory.Faker('sentence', nb_words=5)

    class Meta:
        model = AlignmentStringTable
