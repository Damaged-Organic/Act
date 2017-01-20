# act_project/act/act/serializers.py
from django.db.models.fields.files import ImageFieldFile

from rest_framework import serializers


class StdImageSerializer(serializers.ImageField):
    '''
    Serializer for Django Standardized Image Field package:
    https://github.com/codingjoe/django-stdimage

    Output representation override to include thumbnail `variations`
    fields and present returned value as a complete dictionary
    '''
    _variation = None

    def __init__(self, *args, **kwargs):
        self._variation = kwargs.pop('variation', self._variation)
        super(StdImageSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, value):
        '''
        Can produce single image link of one's choosing as string
        (according to `_variation` kwarg) or dictionary of all images
        with corresponding variation names
        '''
        if not value:
            return None

        images = {
            key: image for key, image in value.__dict__.items()
            if isinstance(image, ImageFieldFile)}

        if self._variation:
            try:
                return super(StdImageSerializer, self).to_representation(
                    images[self._variation])
            except KeyError as e:
                raise KeyError('No such variation in image field') from e

        representation = {
            'original': super(
                StdImageSerializer, self).to_representation(value), }

        for field, image in images.items():
            representation.update({field: super().to_representation(image)})

        return representation
