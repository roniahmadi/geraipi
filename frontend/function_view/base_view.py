import os

import firebase_admin
from django.views import View
from firebase_admin import credentials

from master.models import ConfigurationWebsite


class FrontPage(View):
    # Create your views here.
    def __init__(self):
        self.configuration = ConfigurationWebsite.get_solo()
        self.pinetwork_type = os.environ.get("PI_TYPE") or "Pi Testnet"
        if not firebase_admin._apps:
            cred = credentials.Certificate(
                "geraipi-firebase-adminsdk-aq8fj-9234eedc80.json"
            )
            firebase_admin.initialize_app(cred)
