from django.db import models
from django.core.exceptions import ValidationError


class RecordSession(models.Model):

    CONDITIONS_CHOICE = [("INT", "Intérieur"), ("EXT", "Extérieur")]

    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    session_datetime = models.DateTimeField(
        "date et heure", auto_now=True, auto_now_add=False
    )
    conditions = models.CharField(
        max_length=3, choices=CONDITIONS_CHOICE, default=CONDITIONS_CHOICE[0]
    )
    distance = models.IntegerField("distance")
    comment = models.CharField("commentaires", max_length=255, null=True)

    class Meta:
        abstract = True


class PracticeRecordSession(RecordSession):

    arrows = models.ManyToManyField("equipment.Arrow", through="PracticeRecord")
    number_of_volleys = models.IntegerField("nombre de volées")

    def get_total_score(self) -> int:
        """gets the total score of a training practice

        Returns:
            int: total score of this training practice
        """
        arrows = self.arrows.through.objects.all()
        score_sum = 0
        for arrow in arrows:
            score_sum += arrow.score
        return score_sum

    def __str__(self):
        datetime_as_string = self.session_datetime.strftime("%d/%m/%Y - %H:%M")
        return (
            f"Entrainement: {datetime_as_string} - {self.conditions} - {self.distance}m"
        )

    class Meta:
        verbose_name = "Session d'entrainement"
        verbose_name_plural = "Sessions d'entrainement"


class PracticeRecord(models.Model):
    arrow = models.ForeignKey("equipment.Arrow", on_delete=models.CASCADE)
    practice_session = models.ForeignKey(
        "records.PracticeRecordSession", on_delete=models.CASCADE
    )
    score = models.IntegerField(
        "score",
    )
    volley = models.IntegerField("volée")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self):
        """validation for volley and score attributes."""
        super().clean()
        max_volley = self.practice_session.number_of_volleys

        # score
        if self.score < 0 or self.score > 10:
            raise ValidationError("score may be an integer value between 0 and 10")

        # volley
        if self.volley > max_volley or self.volley < 1:
            raise ValidationError(
                "volley may be an integer value between 1 and session's volley number"
            )

    def __str__(self):
        return f"arrow {self.arrow.id}@volée {self.volley} --> {self.score}"

    class Meta:
        unique_together = ("arrow", "volley", "practice_session")


class StatsRecordSession(RecordSession):

    arrows = models.ManyToManyField("equipment.Arrow", through="StatsRecord")

    def __str__(self):
        datetime_as_string = self.session_datetime.strftime("%d/%m/%Y - %H:%M")
        return (
            f"statistiques: {datetime_as_string} - {self.conditions} - {self.distance}m"
        )

    class Meta:
        verbose_name = "Session d'enregistrement de statistiques de flèches"
        verbose_name_plural = "Sessions d'enregistrement de statistiques de flèches"


class StatsRecord(models.Model):

    arrow = models.ForeignKey("equipment.Arrow", on_delete=models.CASCADE)
    practice_session = models.ForeignKey(
        "records.StatsRecordSession", on_delete=models.CASCADE
    )
    pos_x = models.FloatField("coordonnée horizontale")
    pos_y = models.FloatField("coordonnée verticale")
