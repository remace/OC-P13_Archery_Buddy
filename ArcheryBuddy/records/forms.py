from django import forms

from .models import StatsRecordSession
from equipment.models.arrows import Arrow


class PracticeRecordSessionForm(forms.Form):
    CONDITIONS_CHOICE = [("INT", "Intérieur"), ("EXT", "Extérieur")]

    conditions = forms.ChoiceField(
        label="conditions",
        choices=CONDITIONS_CHOICE,
        widget=forms.Select(
            attrs={
                "class": "block w-full bg-gray-50 pl-4 my-4 text-field border border-gray-300 sm:text-sm rounded-lg focus:ring-violet-500 focus:border-violet-500 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
            }
        ),
    )
    distance = forms.IntegerField(
        label="distance",
        widget=forms.NumberInput(
            attrs={
                "class": "my-4 text-field border border-gray-300 sm:text-sm rounded-lg focus:ring-violet-500 focus:border-violet-500 p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
            }
        ),
    )
    comment = forms.CharField(
        label="commentaires",
        widget=forms.TextInput(
            attrs={
                "class": "my-4 text-field border border-gray-300 sm:text-sm rounded-lg focus:ring-violet-500 focus:border-violet-500 p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
            }
        ),
    )

    number_of_volleys = forms.IntegerField(label="nombre de volées")
    max_arrows_in_volley = forms.IntegerField(
        label="nombre de flèches maximum par volée",
    )


class StatsRecordSessionForm(forms.Form):
    CONDITIONS_CHOICE = [("INT", "Intérieur"), ("EXT", "Extérieur")]

    def __init__(self, srs=None, *args, **kwargs):

        self.user = kwargs.pop("user")
        super(StatsRecordSessionForm, self).__init__(*args, **kwargs)

        self.fields["available_arrows"].queryset = Arrow.objects.filter(
            user=self.user, not_broken=True
        )

        if srs:
            self.fields["conditions"].initial = srs.conditions
            self.fields["distance"].widget.attrs["value"] = srs.distance
            self.fields["comment"].widget.attrs["value"] = srs.comment

            arrows = Arrow.objects.filter(user=self.user, not_broken=True)
            arrows2 = srs.available_arrows.values()
            from pprint import pprint

            # pprint(arrows)
            pprint(arrows2)
            # print(self.fields["available_arrows"].widget)
            # print(self.fields["available_arrows"].widget.__dir__())

    class Meta:
        model = StatsRecordSession
        fields = ["conditions", "distance", "comment", "arrows"]

    conditions = forms.ChoiceField(
        label="conditions",
        choices=CONDITIONS_CHOICE,
        widget=forms.Select(
            attrs={
                "class": "block w-full pl-4 my-4 text-field border border-gray-300 sm:text-sm rounded-lg focus:ring-violet-500 focus:border-violet-500 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
            }
        ),
    )
    distance = forms.IntegerField(
        label="distance",
        widget=forms.NumberInput(
            attrs={
                "class": "block w-full my-4 text-field border border-gray-300 sm:text-sm rounded-lg focus:ring-violet-500 focus:border-violet-500 p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
            }
        ),
    )
    comment = forms.CharField(
        label="commentaires",
        widget=forms.TextInput(
            attrs={
                "class": "block w-full my-4 text-field border border-gray-300 sm:text-sm rounded-lg focus:ring-violet-500 focus:border-violet-500 p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
            }
        ),
    )

    available_arrows = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "rounded focus:ring-violet-500 focus:border-violet-500"}
        ),
        label="flèches utilisées",
    )
