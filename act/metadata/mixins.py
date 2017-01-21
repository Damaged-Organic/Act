# act_project/act/metadata/mixins.py
class MetadataMixin():
    '''
    Acts as interface marker to make sure that class using mixin
    implements method which returns metadata dictionary
    '''
    def get_metadata(self):
        message = "`{}` should implement `get_metadata()` method".format(
            self.__class__.__name__)

        raise NotImplementedError(message)
