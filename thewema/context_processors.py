from django.conf import settings


def _validate_school_meta_data(**kwargs):
    school_data = {}
    for k, v in kwargs.items():
        assert isinstance(v, str), 'Each of the school settings must be of type str. You have given {} of {}'.format(v, type(v))
        if v.strip():
            school_data[k] = v
        else:
            school_data[k] = 'SET THE {}'.format(k).upper()
    return school_data


def school(request):
    '''
    Adds a school's cleaned meta data such as name, motto etc to the context of all views..
    '''
    kwargs = {
        'school_name': getattr(settings, 'SCHOOL_NAME', ''),
        'school_motto': getattr(settings, 'SCHOOL_MOTTO', ''),
    }

    clean_data = _validate_school_meta_data(**kwargs)

    return clean_data
