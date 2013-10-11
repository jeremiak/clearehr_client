from nose.tools import *

from APIConnector.base import CreationFailedException
from APIConnector.subscriber import Subscriber

@raises(CreationFailedException)
def test_create_subscriber_with_no_options():
  subscriber = Subscriber()

def test_create_subscriber_with_all_options():
  subscriber = Subscriber(subscriber_first='Jeremia', 
      subscriber_last='Kimelman', 
      subscriber_group='yo', 
      subscriber_dob='19850301', 
      subscriber_gender='M',
      subscriber_address1='83 Rondel Place', 
      subscriber_city='San Francisco', 
      subscriber_id=123, 
      subscriber_state='CA', 
      subscriber_zip='94103', 
      payer_id=1, 
      payer_name='Insurance Co')

  assert subscriber.__class__ == Subscriber 

def test_create_subscriber_with_optional_parameter():
  subscriber = Subscriber(subscriber_first='Jeremia', 
      subscriber_last='Kimelman', 
      subscriber_group='yo', 
      subscriber_dob='19850301', 
      subscriber_gender='M',
      subscriber_address1='83 Rondel Place', 
      subscriber_city='San Francisco', 
      subscriber_id=123, 
      subscriber_state='CA', 
      subscriber_zip='94103', 
      payer_id=1, 
      payer_name='Insurance Co',
      subscriber_address2='OPTIONAL')

  assert subscriber.subscriber_address2 == 'OPTIONAL'

@raises(AttributeError)
def test_create_subscriber_with_invalid_optional_parameter():
  subscriber = Subscriber(subscriber_first='Jeremia', 
      subscriber_last='Kimelman', 
      subscriber_group='yo', 
      subscriber_dob='19850301', 
      subscriber_gender='M',
      subscriber_address1='83 Rondel Place', 
      subscriber_city='San Francisco', 
      subscriber_id=123, 
      subscriber_state='CA', 
      subscriber_zip='94103', 
      payer_id=1, 
      payer_name='Insurance Co',
      invalid_parameter='INVALID')

  subscriber.invalid_parameter
