import copy


class PrototypeMixin:
    def clone(self):
        return copy.deepcopy(self)


class SingletonByName(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = {}

    def __call__(cls, *args, **kwargs):
        if args:
            name = args[0]
        if kwargs:
            name = kwargs['name']
        if name in cls.__instance:
            return cls.__instance[name]
        else:
            cls.__instance[name] = super().__call__(*args, **kwargs)
            return cls.__instance[name]


class Observer:
    def update(self, subject):
        pass


class Subject:
    def __init__(self):
        self.observers = []

    def notify(self):
        for item in self.observers:
            item.update(self)
