# act_project/act/metadata/mixins.py
from .models import Metadata


class MetadataMixin():
    @staticmethod
    def update_with_metadata_variations(variations):
        if Metadata.variations is not None:
            variations.update(Metadata.variations)

        return variations

    def get_metadata(self):
        raise NotImplementedError('Should be implemented to get metadata')
