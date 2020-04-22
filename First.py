def get_plural(singular):
    if singular[-2:] == "ch" or singular[-2:] == "ss" or singular[-2:] == "sh" or singular[-2:] == "tz" or singular[-1:] == "x":
        plural = singular + "es"
    elif singular[-1:] == "y" and singular[-2:] not in ["oy", "ay", "ey", "uy"]:
        plural = singular[:-1] + "ies"
    elif singular[-1:] == "f" :
        plural = singular[:-1] + "ves"
    elif singular[-2:] == "fe":
        plural = singular[:-2] + "ves"
    else:
        plural = singular + "s"
    
    return plural

    