from protocol.JX import JX

class Factory(object):

    @classmethod
    def get_protocol(cls):
        return JX()