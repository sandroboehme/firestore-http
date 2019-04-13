import unittest

import requests

from firestorehttp.jwt import JWT


class TestFirestoreAccess(unittest.TestCase):
    base_api_url = 'https://content-firestore.googleapis.com/v1'
    project = 'example5-237118'
    database = '/databases/(default)/'

    def test_create_jwt(self):
        jwt = JWT()
        token = 'Bearer ' + jwt.get_token().decode("utf-8")
        endpoint_prefix = self.base_api_url + '/projects/' + self.project + self.database

        # list collections
        endpoint = 'documents:listCollectionIds'
        print(requests.post(endpoint_prefix + endpoint, headers={'Authorization': token}).text)

        # list documents of collection
        endpoint = 'documents/collection1'
        print(requests.get(endpoint_prefix + endpoint, headers={'Authorization': token}).text)

    def test_post_document(self):
        jwt = JWT()
        token = 'Bearer ' + jwt.get_token().decode("utf-8")
        endpoint_prefix = self.base_api_url + '/projects/' + self.project + self.database

        # add document to collection
        endpoint = 'documents/collection3'
        params = {
            'documentId': 'd6'
        }
        field = {
            "fields":
                {
                    "f1":
                        {
                            "mapValue":
                                {
                                    "fields":
                                        {
                                            "mf1":
                                                {
                                                    "booleanValue": True,
                                                },
                                            "mf2":
                                                {
                                                    "stringValue": "xyz",
                                                },
                                            "mf3":
                                                {
                                                    "integerValue": 42,
                                                }
                                        }
                                }
                        },
                    "f2":
                        {
                            "stringValue": "abcde",
                        }
                }
        }

        print(endpoint_prefix + endpoint)
        print(requests.post(endpoint_prefix + endpoint,
                            headers={'Authorization': token},
                            params=params,
                            json=field
                            ).text
              )


if __name__ == '__main__':
    unittest.main()
