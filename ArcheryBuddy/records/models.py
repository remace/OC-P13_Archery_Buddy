from django.db import models
from alternativeequipment.models.arrows import Arrow

from datetime import datetime


class RecordSession(models.Model):

    CONDITIONS_CHOICE = [
        ("INT", "Intérieur"),
        ("EXT", "Extérieur")
    ]

    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    datetime = models.DateTimeField("date et heure", auto_now=True, auto_now_add=False)
    conditions = models.CharField(max_length=3,
        choices= CONDITIONS_CHOICE,
        default= CONDITIONS_CHOICE[0]
    )
    distance = models.IntegerField("distance", null=True)
    comment = models.CharField("commentaires", max_length=255)
    
    def __str__(self):
        return f'{self.datetime} - {self.conditions} - {self.distance}'
    

    class Meta:
        abstract = True


class PracticeRecordSession(RecordSession):
    
    arrows = models.ManyToManyField("alternativeequipment.Arrow", through='PracticeRecord')

    def __str__(self):
        datetime_as_string = self.datetime.strftime("%d/%m/%Y - %H:%M")
        return f'entrainement: {datetime_as_string} - {self.conditions} - {self.distance}m'

    class Meta:
        verbose_name = "Session d'entrainement"
        verbose_name_plural = "Sessions d'entrainement"

class PracticeRecord(models.Model):
    arrow = models.ForeignKey("alternativeequipment.Arrow", on_delete=models.CASCADE)
    practice_session = models.ForeignKey("records.PracticeRecordSession", on_delete=models.CASCADE)
    


# class StatsRecordSession(RecordSession):

#     class Meta:
#         verbose_name = "Session de statistiques"
#         verbose_name_plural = "Sessions de statistiques"
