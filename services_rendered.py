from base import BaseObject, CreationFailedException

class ServicesRendered(BaseObject):
  optional_arguments = ['diagnosis2', 'diagnosis3', 'diagnosis4', 'diagnosis5',
      'diagnosis6', 'diagnosis7', 'diagnosis8', 'diagnosis9', 'diagnosis10',
      'diagnosis11', 'diagnosis12', 'last_menstrual', 'date_admission']

  def __init__(self, client_total_payments=None,
      diagnosis1=None,
      place_of_service=None,
      service_start_date=None,
      service_end_date=None,
      service_lines=None, **kwargs):

    if None not in locals().values():
      self.client_total_payments = client_total_payments
      self.diagnosis1 = diagnosis1
      self.place_of_service = place_of_service
      self.service_start_date = service_start_date #YYYYMMDD
      self.service_end_date = service_end_date #YYYYMMDD
      
      if type(service_lines) == list:
        self.service_lines = service_lines
        for service_line in service_lines:
          self.total_claim += service_line.line_item_amount
      else:
        raise CreationFailedException('service_lines must be a list')
    else:
      raise CreationFailedException 

    for k,v in kwargs.items():
      if k in self.optional_arguments:
        self.__setattr__(k, v)

  def __str__(self):
    return 'ServicesRendered: %s for %s' % ()

