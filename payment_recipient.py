from base import BaseObject, CreationFailedException

class PaymentRecipient(BaseObject):
  optional_arguments = ['pay_to_address2', 'pay_to_first']

  def __init__(self, ein_ssn=None,
      ssn=None,
      npi=None,
      pay_to_address1=None,
      pay_to_city=None,
      pay_to_last=None,
      pay_to_state=None,
      pay_to_zip=None, **kwargs):

    if None not in locals().values():
      self.ein_ssn = ein_ssn
      self.ssn = ssn
      self.npi = npi
      self.pay_to_address1 = pay_to_address1
      self.pay_to_city = pay_to_city
      self.pay_to_last = pay_to_last
      self.pay_to_state = pay_to_state
      self.pay_to_zip = pay_to_zip
    else:
      raise CreationFailedException 

    for k,v in kwargs.items():
      if k in self.optional_arguments:
        self.__setattr__(k, v)

  def __str__(self):
    return 'PaymentRecipient: %s from %s' % (self.pay_to_last, self.pay_to_state)
