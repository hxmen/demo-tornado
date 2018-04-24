class Borg(object):    
    _state = {}    
    def __new__(cls, *args, **kw):    
        ob = super(Borg, cls).__new__(cls, *args, **kw)    
        #ob.__dict__ = cls._state
        print(id(ob))
        return ob    
    
class MyClass(Borg):    
    print('myclass')
    a = 1    
    
