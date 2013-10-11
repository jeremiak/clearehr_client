from base import BaseObject, CreationFailedException

class Subscriber(BaseObject):
  optional_arguments = ['subscriber_address2', 'subscriber_group', 'secondary_payer_name', 
      'secondary_payer_id', 'secondary_subscriber_id', 'secondary_subscriber_group', 
      'tertiary_payer_name', 'tertiary_payer_id', 'tertiary_subscriber_id', 'tertiary_subscriber_group']

  def __init__(self, subscriber_last=None,
      subscriber_first=None,
      subscriber_dob=None,
      subscriber_gender=None,
      subscriber_address1=None,
      subscriber_city=None,
      subscriber_id=None,
      subscriber_state=None,
      subscriber_zip=None, 
      payer_id=None,
      payer_name=None,
      provider_signature='Y',
      release_signed='Y', **kwargs):

    if None not in locals().values():
      self.subscriber_last = subscriber_last 
      self.subscriber_first = subscriber_first
      self.subscriber_dob = subscriber_dob #YYYYMMDD
      self.subscriber_gender = subscriber_gender
      self.subscriber_address1 = subscriber_address1
      self.subscriber_city = subscriber_city
      self.subscriber_id = subscriber_id
      self.subscriber_state = subscriber_state
      self.subscriber_zip = subscriber_zip
    else:
      raise CreationFailedException 

    for k,v in kwargs.items():
      if k in self.optional_arguments:
        self.__setattr__(k, v)

  def __str__(self):
    return 'Subscriber: %s, %s' % (self.subscriber_last, self.subscriber_first)
