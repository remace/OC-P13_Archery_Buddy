from django import forms


class PracticeRecordSessionForm(forms.Form):
    CONDITIONS_CHOICE = [("INT", "Intérieur"), ("EXT", "Extérieur")]
    conditions = forms.ChoiceField(label="conditions", choices=CONDITIONS_CHOICE)
    distance = forms.IntegerField(label="distance")
    comment = forms.CharField(label="commentaires")

    number_of_volleys = forms.IntegerField(label="nombre de volées")
    max_arrows_in_volley = forms.IntegerField(
        label="nombre maximum de flèches par volée"
    )
