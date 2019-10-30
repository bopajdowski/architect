# -*- coding: utf-8 -*-
"""Model definitions."""

# Django
from django.db import models
import architect


class AlignmentTable(models.Model):
    """Alignment table model interpretation of excel file."""

    energy_id = models.CharField(max_length=255, db_index=True)
    date_modified = models.DateTimeField(db_index=True, blank=True, null=True)

    class Meta:
        """Meta class."""

        verbose_name = 'No partition'
        verbose_name_plural = 'No partition'


@architect.install('partition', type='range', subtype='date', constraint='month',
                   column='date_modified')
class AlignmentDateTable(models.Model):
    """Alignment table model interpretation of excel file."""

    energy_id = models.CharField(max_length=255, db_index=True)
    date_modified = models.DateTimeField(db_index=True, blank=True, null=True)

    class Meta:
        """Meta class."""

        verbose_name = 'Date example'
        verbose_name_plural = 'Date examples'


@architect.install('partition', type='range', subtype='string_firstchars', constraint='2',
                   column='energy_id')
class AlignmentStringTable(models.Model):
    """Alignment table model interpretation of excel file."""

    energy_id = models.CharField(max_length=255, db_index=True)
    date_modified = models.DateTimeField(db_index=True, blank=True, null=True)

    class Meta:
        """Meta class."""

        verbose_name = 'String example'
        verbose_name_plural = 'String examples'
