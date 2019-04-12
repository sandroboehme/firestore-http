import json
import time
import jwt
from jwt.contrib.algorithms.pycrypto import RSAAlgorithm

from definitions import AUTH_FILE_PATH


class JWT(object):

    def get_token(self):
        """
        Returns the jwt token using the configured `/auth.json` file and a default expiration of an hour.
        """
        # The implementation has been guided by this page:
        # https://developers.google.com/identity/protocols/OAuth2ServiceAccount

        try:
            jwt.register_algorithm('RS256', RSAAlgorithm(RSAAlgorithm.SHA256))
        except ValueError:
            # Algorithm already has a handler
            pass

        with open(AUTH_FILE_PATH, 'r') as f:
            auth = json.load(f)
        iat = time.time()
        # exp is set to expire the token maximum of an hour later
        # see https://developers.google.com/identity/protocols/OAuth2ServiceAccount#formingclaimset
        exp = iat + 3600
        payload = {'iss': auth['client_email'],
                   'sub': auth['client_email'],
                   # see https://github.com/googleapis/googleapis/blob/master/google/firestore/firestore_v1.yaml
                   # name: firestore.googleapis.com # Service name
                   # - name: google.firestore.v1.Firestore # API name
                   # 'aud': 'https://SERVICE_NAME/API_NAME'
                   'aud': 'https://firestore.googleapis.com/google.firestore.v1.Firestore',
                   'iat': iat,
                   'exp': exp
                   }
        additional_headers = {'kid': auth['private_key_id']}

        # For jwt docs see: https://pyjwt.readthedocs.io/en/latest/
        return jwt.encode(payload, auth['private_key'], headers=additional_headers, algorithm='RS256')
