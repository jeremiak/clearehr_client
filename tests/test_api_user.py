from nose.tools import *

from ..base import CreationFailedException
from ..api_user import APIUser 

@raises(CreationFailedException)
def test_create_api_user_with_no_options():
  user = APIUser()

def test_create_api_user_with_all_options():
  user = APIUser(username='kimelmanmd', key='KEYGOESHERE') 

  assert user.__class__ == APIUser 

