# -*- coding: utf-8 -*-
"""Admin site configuration file."""

from django.contrib import admin


# Local
from .models import AlignmentTable, AlignmentStringTable, AlignmentDateTable


@admin.register(AlignmentTable)
class AlignmentTableAdmin(admin.ModelAdmin):
    """Alignment table admin definitions."""

    list_display = [
        'id',
        'energy_id',
        'date_modified',
    ]

    show_full_result_count = False


@admin.register(AlignmentDateTable)
class AlignmentDateTableAdmin(admin.ModelAdmin):
    """Alignment table admin definitions."""

    list_display = [
        'id',
        'energy_id',
        'date_modified',
    ]

    show_full_result_count = False


@admin.register(AlignmentStringTable)
class AlignmentStringTableAdmin(admin.ModelAdmin):
    """Alignment table admin definitions."""

    list_display = [
        'id',
        'energy_id',
        'date_modified',
    ]

    show_full_result_count = False
