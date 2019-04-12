import unittest

import requests

from firestorehttp.jwt import JWT


class TestFirestoreAccess(unittest.TestCase):

    def test_create_jwt(self):

        jwt = JWT()
        token = 'Bearer ' + jwt.get_token().decode("utf-8")
        base_api_url = 'https://content-firestore.googleapis.com/v1'
        project = 'example5-237118'
        database = '/databases/(default)/'
        endpoint_prefix = base_api_url + '/projects/' + project + database

        # list collections
        endpoint = 'documents:listCollectionIds'
        print(requests.post(endpoint_prefix + endpoint, headers={'Authorization': token}).text)

        # list documents of collection
        endpoint = 'documents/collection1'
        print(requests.get(endpoint_prefix + endpoint, headers={'Authorization': token}).text)

        # add document to collection
        endpoint = 'documents/collection1/'
        params = {
            'documentId': 'documentId2'
        }
        print(requests.post(endpoint_prefix + endpoint, headers={'Authorization': token}, params=params).text)


if __name__ == '__main__':
    unittest.main()
