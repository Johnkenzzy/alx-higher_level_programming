class LockedClass:
    """limit the creation of new attributes to first_name"""
    __slots__ = ['first_name']

    def __init__(self, first_name=None):
        self.first_name = first_name
