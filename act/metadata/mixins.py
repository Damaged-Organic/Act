# act_project/act/metadata/mixins.py
class MetadataMixin():
    def get_metadata(self):
        raise NotImplementedError('Should be implemented to get metadata')
