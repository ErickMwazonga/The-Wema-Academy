from django import template

register = template.Library()


@register.filter
def grade(value):
    return gradelogic(value)


@register.filter
def mean(value):
    avg = int(value/5)
    return gradelogic(avg)


@register.filter
def score_remarks(value):
    return remarkslogic(value)


@register.filter
def mean_remarks(value):
    avg = int(value/5)
    return remarkslogic(avg)


def gradelogic(value):
    assert isinstance(value, int), (
        'The value to be filtered is a score which must be of int type.'
        ' A value of {} has been given instead.'.format(type(value))
    )
    if value == 0 and value < 30:
        return 'E'
    elif value >= 30 and value < 35:
        return 'D-'
    elif value >= 35 and value < 40:
        return 'D'
    elif value >= 40 and value < 45:
        return 'D+'
    elif value >= 45 and value < 50:
        return 'C-'
    elif value >= 50 and value < 55:
        return 'C'
    elif value >= 55 and value < 60:
        return 'C+'
    elif value >= 60 and value < 65:
        return 'B-'
    elif value >= 65 and value < 70:
        return 'B'
    elif value >= 70 and value < 75:
        return 'B+'
    elif value >= 75 and value < 80:
        return 'A-'
    elif value >= 80 and value < 101:
        return 'A'
    else:
        raise('A malicious mark:{} has been entered'.format(value))


def remarkslogic(value):
    assert isinstance(value, int), (
        'The value to be filtered is a score which must be of int type.'
        ' A value of {} has been given instead.'.format(type(value))
        )

    if value == 0 and value < 30:
        return 'Work Harder'
    elif value >= 30 and value < 35:
        return 'Poor'
    elif value >= 35 and value < 40:
        return 'Poor'
    elif value >= 40 and value < 45:
        return 'Below Average'
    elif value >= 45 and value < 50:
        return 'Below Average'
    elif value >= 50 and value < 55:
        return 'Average'
    elif value >= 55 and value < 60:
        return 'Average'
    elif value >= 60 and value < 65:
        return 'Good'
    elif value >= 65 and value < 70:
        return 'Good'
    elif value >= 70 and value < 75:
        return 'Well Done'
    elif value >= 75 and value < 80:
        return 'Well Done'
    elif value >= 80 and value < 101:
        return 'Excellent'
    else:
        raise('A malicious mark:{} has been entered'.format(value))
