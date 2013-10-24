from nose.tools import *

from ..base import CreationFailedException

def test_creation_failed_exception():
  expected = 'Creation of this object failed because not all required values were submitted'
  creation_failed_exception = CreationFailedException()

  assert creation_failed_exception.msg == expected

def test_creation_failed_exception_message():
  creation_failed_exception = CreationFailedException(msg='Message set appropriately')

  assert creation_failed_exception.msg == 'Message set appropriately'
