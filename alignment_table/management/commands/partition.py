"""Gen raport file."""

from django.core.management.base import BaseCommand


from alignment_table.tests.facories import AlignmentTableFactory, AlignmentDateTableFactory, \
    AlignmentStringTableFactory
from tqdm import tqdm
from contextlib import closing
from django.db import connection


def generate_data_in_database(start, stop, table_name):
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """
            INSERT INTO {0} (energy_id, date_modified)
            SELECT
                md5(random()::text),
                '1/1/2008'::date + ('1 month'::interval*floor(random()*144))
            FROM
                generate_series({1}, {2}) AS s(i)
            """.format(table_name, start, stop)
        )


class Command(BaseCommand):
    """Command."""

    help = 'Generate data.'

    def handle(self, *args, **options):
        """Handle command."""

        r_start = 0
        r_stop = 10000000

        step = 100000
        pbar = tqdm(range(r_start, r_stop, step))
        for start in pbar:
            generate_data_in_database(start, start + step - 1, 'alignment_table_alignmenttable')
            pbar.set_description("Processing %s" % start)

        step = 10000
        pbar = tqdm(range(r_start, r_stop, step))
        for start in pbar:
            generate_data_in_database(start, start + step - 1, 'alignment_table_alignmentdatetable')
            pbar.set_description("Processing %s" % start)

        step = 1000
        pbar = tqdm(range(r_start, r_stop, step))
        for start in pbar:
            generate_data_in_database(start, start + step - 1, 'alignment_table_alignmentstringtable')
            pbar.set_description("Processing %s" % start)



