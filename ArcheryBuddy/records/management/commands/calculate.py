from django.core.management.base import BaseCommand
from django.db.models import Avg

from records.models import StatsRecord, StatsRecordSession
from equipment.models.arrows import Arrow

from records.utils import calculate_barycentre

from pprint import pprint


class Command(BaseCommand):

    help = "calculate things on a set of arrows saved in database"

    def add_argument(self, parser):
        pass

    def handle(self, *args, **options):
        records = self.get_records()

        barycentres = []
        for record in records.values():
            barycentre_coords = calculate_barycentre(record)
            barycentre = {
                "arrow_id": record[0].arrow_id,
                "pos_x": barycentre_coords[0],
                "pos_y": barycentre_coords[1],
            }

            barycentres.append(barycentre)
        pprint(barycentres)

        quiver = calculate_quiver(barycentres)

        return quiver

    def get_records(self):
        bulk_records = StatsRecord.objects.filter(pk__gte=800)
        pk_list = [
            id.get("arrow_id") for id in bulk_records.values("arrow_id").distinct()
        ]
        records = {}
        for id in pk_list:
            records[id] = [rec for rec in bulk_records.filter(arrow_id=id)]
        return records
