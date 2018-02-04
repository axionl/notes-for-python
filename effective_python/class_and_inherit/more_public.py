class MyObject(object):
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field

class MyOtherObject(object):
    def __init__(self):
        self.__private_field = 71

    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field

class MyParentObject(object):
    def __init__(self):
        self.__private_field = 71
    
class MyChildObject(MyParentObject):
    def get_private_field(self):
        return self.__private_field

class MyClass(object):
    def __init__(self, value):
        self.__value = value

class ApiClass(object):
    def __init__(self):
        self.__value = 5

    def get(self):
        return self.__value

class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'

def main():
    foo = MyObject()
    assert foo.public_field == 5
    assert foo.get_private_field() == 10
    # print(foo.__private_field)

    bar = MyOtherObject()
    assert MyOtherObject.get_private_field_of_instance(bar) == 71

    baz = MyChildObject()
    # baz.get_private_field()
    assert baz._MyParentObject__private_field == 71
    print(baz.__dict__)

    a = Child()
    print(a.get(), 'and', a._value, 'are different')
if __name__ == '__main__':
    main()
    