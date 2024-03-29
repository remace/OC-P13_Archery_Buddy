from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_score(context, volley, shot):
    try:
        score = str(context["practice_records"]
                           [int(volley)]
                           [int(shot) - 1]
                           ["score"])
    except KeyError:
        score = ""
    except IndexError:
        score = ""
    return score
