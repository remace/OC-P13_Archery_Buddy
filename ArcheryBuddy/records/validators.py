from django.core.exceptions import ValidationError

def validate_volley_id(id, session):
    if not (1 <= id <= session.number_of_volleys):
        raise ValidationError(
            f"{id} n'est pas un numéro de volée valide",
            params={'value':id, 'session':session}
        )

def validate_arrow_score(value):
    if not value in range(0,11,1):
        raise ValidationError(
            f"{value} n'est pas un score valide",
            params={'value': value}
        )