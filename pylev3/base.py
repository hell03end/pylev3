class _Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(
                *args, **kwargs
            )
        else:
            cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(_Singleton("_Singleton", (object,), {})):
    '''
        A metaclass that creates a Singleton base class when called.

        Ensure that only one instance of a class is created and provide
        a global access point to the object.
    '''

    def __init__(self, *args, **kwargs):
        super(Singleton, self).__init__()
