# act_project/act/metadata/models.py
from urllib.parse import urljoin

from django.db import models, transaction
from django.core.exceptions import ObjectDoesNotExist

from stdimage.models import StdImageField

# Notice overridden transmeta import!
from act.services.transmeta import TransMeta
from act.services.file_name import RandomFileName
from act.utils import get_default_URL

from .utils import truncate_text


def update_with_metadata_variations(variations):
    if Metadata.variations is not None:
        variations.update(Metadata.variations)

    return variations


class Metadata(models.Model, metaclass=TransMeta):
    IMAGE_PATH = 'metadata/images/'

    variations = {
        'open_graph': {'width': 1200, 'height': 630, 'crop': True},
        'twitter_card': {'width': 1120, 'height': 600, 'crop': True},
    }

    image = StdImageField(
        'Зображення',
        upload_to=RandomFileName(IMAGE_PATH),
        variations=variations)

    url_name = models.CharField('Роутінг', max_length=100)
    title = models.CharField('Назва сторінки', max_length=100)
    description = models.CharField('Опис сторінки', max_length=250)
    robots = models.CharField('Інформація для ботів', max_length=100)

    class Meta:
        verbose_name = 'Метадані'
        verbose_name_plural = 'Метадані'

        translate = ('title', 'description', )

    def __str__(self):
        return str(self.title) or self.__class__.__name__

    @staticmethod
    def build_metadata_from_dict(master_metadata, object_metadata_dict):
        '''
        Builds metadata object from dictionary that has appropriate fields.
        Used for dynamic metadata creation for various objects specified in
        metadata settings. Object metadata is based on `master_metadata` which
        resembles `ancestor` for a given object (e.g. for concrete Post object
        ancestor would be a Metadata for a list of posts), and will fill empty
        fields that could be omitted in `object_metadata_dict`
        '''
        metadata = Metadata(**object_metadata_dict)

        metadata.description_uk = truncate_text(metadata.description_uk, 250)

        if not metadata.image:
            metadata.image = master_metadata.image

        if not metadata.robots:
            metadata.robots = master_metadata.robots

        return metadata

    def image_preview(self):
        return '<img src="%s" width="300" max-width="300">' % (self.image.url)
    image_preview.allow_tags = True
    image_preview.short_description = 'Превʼю зображення'

    def provide_open_graph(self, open_graph_type):
        self.open_graph = OpenGraph(
            metadata=self, type=open_graph_type)

    def provide_twitter_card(self, twitter_card):
        self.twitter_card = TwitterCard(
            metadata=self, card=twitter_card)


class MetadataLinked(models.Model):
    '''
    Adds a `Metadata` instance to subclass so it can build itself on that
    instance attributes. `MetadataLinked` object must accept `metadata`
    kwarg, and will raise exception if that condition is not met
    '''
    metadata = None

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        metadata = kwargs.pop('metadata')

        if not isinstance(metadata, Metadata):
            raise ImproperlyConfigured('Passed kwarg is not Metadata instance')

        self.metadata = metadata
        super(MetadataLinked, self).__init__(*args, **kwargs)

    def get_metadata_attribute(self, attribute):
        '''
        Getting `Metadata` attributes through this method for more control
        '''
        return getattr(self.metadata, attribute)


class OpenGraph(MetadataLinked):
    TYPE_WEBSITE = 'website'
    TYPE_ARTICLE = 'article'

    TYPES = [TYPE_WEBSITE, TYPE_ARTICLE]

    DESCRIPTION_LENGTH = 250

    _type = None

    class Meta:
        ''' Should not be persisted in database, built on top of `Metadata` '''
        managed = False

    def __init__(self, *args, **kwargs):
        open_graph_type = kwargs.pop('type', self.TYPE_WEBSITE)
        if open_graph_type in self.TYPES:
            self._type = open_graph_type

        super(OpenGraph, self).__init__(*args, **kwargs)

    def __str__(self):
        return str(self.__class__.__name__)

    @property
    def type(self):
        return self._type

    @property
    def url(self):
        return self.get_metadata_attribute('url_name')

    @property
    def title(self):
        return self.get_metadata_attribute('title')

    @property
    def description(self):
        return truncate_text(
            self.get_metadata_attribute('description'),
            self.DESCRIPTION_LENGTH)

    @property
    def image(self):
        return self.get_metadata_attribute('image')


class TwitterCard(MetadataLinked):
    CARD_SUMMARY = 'summary'
    CARD_SUMMARY_LARGE_IMAGE = 'summary_large_image'

    CARDS = [CARD_SUMMARY, CARD_SUMMARY_LARGE_IMAGE]

    DESCRIPTION_LENGTH = 140

    _card = None

    class Meta:
        ''' Should not be persisted in database, built on top of `Metadata` '''
        managed = False

    def __init__(self, *args, **kwargs):
        twitter_card = kwargs.pop('card', self.CARD_SUMMARY)
        if twitter_card in self.CARDS:
            self._card = twitter_card

        super(TwitterCard, self).__init__(*args, **kwargs)

    def __str__(self):
        return str(self.__class__.__name__)

    @property
    def card(self):
        return self._card

    @property
    def title(self):
        return self.get_metadata_attribute('title')

    @property
    def description(self):
        return truncate_text(
            self.get_metadata_attribute('description'),
            self.DESCRIPTION_LENGTH)

    @property
    def image(self):
        return self.get_metadata_attribute('image')
