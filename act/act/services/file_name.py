# act_project/act/act/services/file_name.py
import os
import uuid

from django.utils.deconstruct import deconstructible


@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")

    def __call__(self, instance, filename):
        _, extension = os.path.splitext(filename)
        return self.path % (uuid.uuid4(), extension)

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            other.path == self.path)
