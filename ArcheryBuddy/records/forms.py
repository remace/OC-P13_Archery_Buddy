from django import forms

from .models import StatsRecordSession
from equipment.models.arrows import Arrow


class PracticeRecordSessionForm(forms.Form):
    CONDITIONS_CHOICE = [("INT", "Intérieur"), ("EXT", "Extérieur")]
    conditions = forms.ChoiceField(label="conditions", choices=CONDITIONS_CHOICE)
    distance = forms.IntegerField(label="distance")
    comment = forms.CharField(label="commentaires")

    number_of_volleys = forms.IntegerField(label="nombre de volées")
    max_arrows_in_volley = forms.IntegerField(
        label="nombre maximum de flèches par volée"
    )


class StatsRecordSessionForm(forms.Form):
    CONDITIONS_CHOICE = [("INT", "Intérieur"), ("EXT", "Extérieur")]

    def __init__(self, *args, **kwargs):

        self.user = kwargs.pop("user")
        super(StatsRecordSessionForm, self).__init__(*args, **kwargs)

        self.fields["available_arrows"].queryset = Arrow.objects.filter(
            user=self.user, not_broken=True
        )

    class Meta:
        model = StatsRecordSession
        fields = ["conditions", "distance", "comment", "arrows"]

    conditions = forms.ChoiceField(label="conditions", choices=CONDITIONS_CHOICE)
    distance = forms.IntegerField(label="distance")
    comment = forms.CharField(label="commentaires")

    available_arrows = forms.ModelMultipleChoiceField(
        queryset=None, widget=forms.CheckboxSelectMultiple
    )
