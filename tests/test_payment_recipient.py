from nose.tools import *

from ..base import CreationFailedException
from ..payment_recipient import PaymentRecipient 

@raises(CreationFailedException)
def test_create_payment_recipient_with_no_options():
  payment_recipient = PaymentRecipient()

def test_create_payment_recipient_with_all_options():
  payment_recipient = PaymentRecipient(ein_ssn='REQUIRED',
      ssn='REQUIRED',
      npi='REQUIRED',
      pay_to_address1='REQUIRED',
      pay_to_city='REQUIRED',
      pay_to_last='REQUIRED',
      pay_to_state='REQUIRED',
      pay_to_zip='REQUIRED')

  assert payment_recipient.__class__ == PaymentRecipient 

def test_create_payment_recipient_with_optional_parameter():
  payment_recipient = PaymentRecipient(ein_ssn='REQUIRED',
      ssn='REQUIRED',
      npi='REQUIRED',
      pay_to_address1='REQUIRED',
      pay_to_city='REQUIRED',
      pay_to_last='REQUIRED',
      pay_to_state='REQUIRED',
      pay_to_zip='REQUIRED',
      pay_to_address2='OPTIONAL')

  assert payment_recipient.pay_to_address2 == 'OPTIONAL'

@raises(AttributeError)
def test_create_payment_recipient_with_invalid_optional_parameter():
  payment_recipient = PaymentRecipient(ein_ssn='REQUIRED',
      ssn='REQUIRED',
      npi='REQUIRED',
      pay_to_address1='REQUIRED',
      pay_to_city='REQUIRED',
      pay_to_last='REQUIRED',
      pay_to_state='REQUIRED',
      pay_to_zip='REQUIRED',
      invalid_paramter='INVALID')

  payment_recipient.invalid_parameter
