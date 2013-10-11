from nose.tools import *

from APIConnector.base import CreationFailedException
from APIConnector.service_line import ServiceLine 

@raises(CreationFailedException)
def test_create_service_line_with_no_options():
  service_line = ServiceLine() 

def test_create_service_line_with_all_options():
  service_line = ServiceLine(hcpcs_code='REQUIRED',
      line_item_amount='REQUIRED',
      code_pointer1='REQUIRED')

  assert service_line.__class__ == ServiceLine

def test_create_service_line_with_optional_parameter():
  service_line = ServiceLine(hcpcs_code='REQUIRED',
      line_item_amount='REQUIRED',
      code_pointer1='REQUIRED',
      modifier1='OPTIONAL')

  assert service_line.modifier1 == 'OPTIONAL'

@raises(AttributeError)
def test_create_service_line_with_invalid_optional_paramter():
  service_line = ServiceLine(hcpcs_code='REQUIRED',
      line_item_amount='REQUIRED',
      code_pointer1='REQUIRED',
      invalid='INVALID')

  service_line.invalid
