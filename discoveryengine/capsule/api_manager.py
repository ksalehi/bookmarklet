from __future__ import unicode_literals

import requests

from discoveryengine.settings import CAPSULE_ID, CAPSULE_API_KEY

from .models import *

class APIManager(object):

    BASE_URL = "https://%s.capsulecrm.com/api/"

    def add_person(Person):
        pass