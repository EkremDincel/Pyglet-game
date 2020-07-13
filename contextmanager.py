def __enter(self):
    self.begin()

def __exit(self, exception_type, exception_value, traceback):
    self.end()

def activatable(cls):
    cls.__enter__ = __enter
    cls.__exit__ = __exit
    return cls
