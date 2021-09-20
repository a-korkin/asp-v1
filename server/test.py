import json

class Foo(object):
    def __init__(self):
        self.x = 1
        self.y = 2

    def to_json(self):        
        return json.dumps(self.__dict__)
        