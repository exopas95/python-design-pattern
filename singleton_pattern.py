# 기본 싱글턴 패턴
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

# 게으른 싱글턴 패턴
class LazySingleton:
    __instance = None
    def __init__(self):
        if not LazySingleton.__instance:
            print("__init__ method called..")
        else:
            print("Instance already created: ", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton
        return cls.__instance

s = Singleton()
print("Object created", s)

s1 = Singleton()
print("Object created", s1)
