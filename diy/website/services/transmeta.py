# diy_project/diy/website/services/transmeta.py
from django.conf import settings
from django.utils.translation import get_language

import transmeta

'''
This whole bunch of shit is neue-transmeta package, based on transmeta,
with bugfix in `get_real_fieldname()`. Damn thing still won't adhere to
merge request proposed a few years ago.
'''


def fallback_language():
    """ returns fallback language """
    return getattr(settings, 'TRANSMETA_DEFAULT_LANGUAGE',
                   settings.LANGUAGE_CODE)


def get_real_fieldname(field, lang=None):
    if lang is None:
        '''
        This is the added line which handles exception of calling `split()`
        on `None` object. Uses `fallback_language()` if `get_language()`
        returns `None`
        '''
        lang = get_language() or fallback_language()
        lang = lang.split('-')[0]  # both 'en-US' and 'en' -> 'en'
    return str('%s_%s' % (field, lang))

transmeta.get_real_fieldname = get_real_fieldname
transmeta.fallback_language = fallback_language

# Main class
TransMeta = transmeta.TransMeta

# For admin module
canonical_fieldname = transmeta.canonical_fieldname
