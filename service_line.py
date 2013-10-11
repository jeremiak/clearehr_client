from base import BaseObject, CreationFailedException

class ServiceLine(BaseObject):
  optional_arguments = ['modifier1', 'modifier2', 'modifier3', 'modifier4', 
      'code_pointer2', 'code_pointer3', 'code_pointer4', 'is_dme']

  def __init__(self, hcpcs_code=None,
      line_item_amount=None,
      code_pointer1=None, **kwargs):

    if None not in locals().values():
      self.hcpcs_code = hcpcs_code
      self.line_item_amount = line_item_amount
      self.code_pointer1 = code_pointer1
    else:
      raise CreationFailedException 

    for k,v in kwargs.items():
      if k in self.optional_arguments:
        self.__setattr__(k, v)

  def __str__(self):
    return 'ServiceLine: %s for %s' % (self.hcpcs_code, self.line_item_amount)
