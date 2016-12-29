# act_project/act/act/validators.py
import os
import magic

from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.deconstruct import deconstructible
from django.template.defaultfilters import filesizeformat


@deconstructible
class FileContentTypeValidator(object):
    messages = {
        'content_type': _(
            "Завантажений файл має недозволений тип '%(content_type)s'. "),
        'max_size': _(
            "Завантажений файл більше максимального розміру %(max_size)s. "),
    }
    codes = {
        'content_type': 'invalid_content_type',
        'max_size': 'exceeded_max_size',
    }

    def __init__(
        self, allowed_content_types=(), max_size=None, message=None, code=None
    ):
        self.allowed_content_types = allowed_content_types
        self.max_size = max_size

        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if self.allowed_content_types:
            content_type = magic.from_buffer(value.read(), mime=True)
            if content_type not in self.allowed_content_types:
                raise ValidationError(
                    self.messages['content_type'],
                    code=self.codes['content_type'],
                    params={'content_type': content_type}
                )

        if self.max_size is not None:
            if value.size > self.max_size:
                raise ValidationError(
                    self.messages['max_size'],
                    code=self.codes['max_size'],
                    params={'max_size': filesizeformat(self.max_size)}
                )

    def __eq__(self, other):
        return isinstance(other, FileContentTypeValidator)
