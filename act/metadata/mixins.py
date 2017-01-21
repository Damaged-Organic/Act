# act_project/act/metadata/mixins.py
class MetadataMixin():
    def get_metadata(self):
        message = "`{}` should implement `get_metadata()` method".format(
            self.__class__.__name__)

        raise NotImplementedError(message)
