from nose.tools import *

from APIConnector.base import CreationFailedException
from APIConnector.services_rendered import ServicesRendered 

@raises(CreationFailedException)
def test_create_services_rendered_with_no_options():
  services_rendered = ServicesRendered() 

def test_create_services_rendered_with_all_options():
  services_rendered = ServicesRendered(client_total_payments='REQUIRED',
      diagnosis1='REQUIRED',
      place_of_service='REQUIRED',
      service_start_date='REQUIRED',
      service_end_date='REQUIRED',
      service_lines=[])

  assert services_rendered.__class__ == ServicesRendered 

def test_create_services_rendered_with_optional_parameter():
  services_rendered = ServicesRendered(client_total_payments='REQUIRED',
      diagnosis1='REQUIRED',
      place_of_service='REQUIRED',
      service_start_date='REQUIRED',
      service_end_date='REQUIRED',
      service_lines=[],
      diagnosis2='OPTIONAL') 

  assert services_rendered.diagnosis2 == 'OPTIONAL'

@raises(AttributeError)
def test_create_services_rendered_with_invalid_optional_paramter():
  services_rendered = ServicesRendered(client_total_payments='REQUIRED',
      diagnosis1='REQUIRED',
      place_of_service='REQUIRED',
      service_start_date='REQUIRED',
      service_end_date='REQUIRED',
      service_lines=[],
      invalid_parameter='INVALID')

  services_rendered.invalid

@raises(CreationFailedException)
def test_create_services_rendered_with_service_lines_of_wrong_Type():
  services_rendered = ServicesRendered(client_total_payments='REQUIRED',
      diagnosis1='REQUIRED',
      place_of_service='REQUIRED',
      service_start_date='REQUIRED',
      service_end_date='REQUIRED',
      service_lines='NOTALIST')
