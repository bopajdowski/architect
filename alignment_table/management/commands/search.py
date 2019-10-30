"""Gen raport file."""

# Django
from time import time

from django.core.management.base import BaseCommand

# Local
from ...models import AlignmentTable
from ...models import AlignmentDateTable
from ...models import AlignmentStringTable


class Command(BaseCommand):
    """Command."""

    help = 'Search selected and measure time.'

    def handle(self, *args, **options):
        """Handle command."""
        print('Wyszukiwanie po tekscie')
        avg = 0
        for x in range(10):
            random_customers = AlignmentTable.objects.only('energy_id').order_by(
                '?').values_list('energy_id', flat=True)[:1000]
            start = time()
            for eci in random_customers:
                y = AlignmentTable.objects.filter(energy_id__istartswith=eci[:5])
            end = time() - start
            print(x + 1, end)
            avg += end
        print(y.explain())
        print('avg', avg/10)

        print('Wyszukiwanie po dacie')
        avg = 0
        for x in range(10):
            random_date = AlignmentTable.objects.only('date_modified').order_by(
                '?').values_list('date_modified', flat=True)[:1000]
            start = time()
            for date in random_date:
                y = AlignmentTable.objects.filter(date_modified=date)
            end = time() - start
            print(x +1, end)
            avg += end
        print(y.explain())
        print('avg', avg / 10)
        wynik1 = avg / 10

        print('Wyszukiwanie po tekscie')
        avg = 0
        for x in range(10):
            random_customers = AlignmentStringTable.objects.only('energy_id').order_by(
                '?').values_list('energy_id', flat=True)[:1000]
            start = time()
            for eci in random_customers:
                y = AlignmentStringTable.objects.filter(energy_id__istartswith=eci[:10])
            end = time() - start
            print(x + 1, end)
            avg += end
        print(y.explain())
        print('avg', avg / 10)

        print('Wyszukiwanie po dacie')
        avg = 0
        for x in range(10):
            random_date = AlignmentDateTable.objects.only('date_modified').order_by(
                '?').values_list('date_modified', flat=True)[:1000]
            start = time()
            for date in random_date:
                y = AlignmentDateTable.objects.filter(date_modified=date)
            end = time() - start
            print(x + 1, end)
            avg += end
        print(y.explain())
        print('avg', avg / 10)
        wynik2 = avg / 10

        print(wynik1/wynik2*100)
