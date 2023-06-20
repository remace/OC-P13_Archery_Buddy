from django import template

register = template.Library()


@register.simple_tag(takes_context=True, name="get_field_colors")
def get_field_colors(context, volley, shot):

    colors = {
        "": "bg-gray-50 text-gray-900",
        "0": "bg-gray-50 text-gray-900",
        "1": "bg-white text-black",
        "2": "bg-white text-black",
        "3": "bg-black text-white",
        "4": "bg-black text-white",
        "5": "bg-blue-400 text-black",
        "6": "bg-blue-400 text-black",
        "7": "bg-red-500 text-white",
        "8": "bg-red-500 text-white",
        "9": "bg-yellow-400 text-black",
        "10": "bg-yellow-400 text-black",
    }

    try:
        score = str(context["practice_records"]
                           [int(volley)]
                           [int(shot) - 1]
                           ["score"])
    except KeyError:
        score = ""
    except IndexError:
        score = ""
    return colors[score]
