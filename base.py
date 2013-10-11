
class BaseObject(object):
  def __init__(self):
    pass


class BaseException(Exception):
  def __init__(self):
    pass

class CreationFailedException(BaseException):
  def __init__(self):
    self.msg = 'Creation of this object failed because not all required values were submitted'
