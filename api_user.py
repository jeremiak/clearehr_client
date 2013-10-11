from base import BaseObject, CreationFailedException

class APIUser(BaseObject):
  def __init__(self, username=None, key=None):
    if username!=None and key!=None:
      self.username = username
      self.key = key
    else:
      raise CreationFailedException
