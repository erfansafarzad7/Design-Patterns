"""
    Prototype
    - Prototype is a creational design patterns that lets you cope existing objects
    without making your code dependent on their classes.
"""
import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        cloned_obj = copy.deepcopy(self._objects.get(name))
        cloned_obj.__dict__.update(kwargs)
        return cloned_obj


def client_prototype(name, obj, **kwargs):
    prototype = Prototype()
    prototype.register(name, obj)
    return prototype.clone(name, **kwargs)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('erfan', 30)

p_clone = client_prototype('p1', p, age=23)
print(p_clone.__dict__)
