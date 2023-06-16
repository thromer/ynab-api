"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ynab_api
from ynab_api.model.save_sub_transaction import SaveSubTransaction
from ynab_api.model.save_transaction_with_id_all_of import SaveTransactionWithIdAllOf
from ynab_api.model.save_transaction_with_optional_fields import SaveTransactionWithOptionalFields
globals()['SaveSubTransaction'] = SaveSubTransaction
globals()['SaveTransactionWithIdAllOf'] = SaveTransactionWithIdAllOf
globals()['SaveTransactionWithOptionalFields'] = SaveTransactionWithOptionalFields
from ynab_api.model.save_transaction_with_id import SaveTransactionWithId


class TestSaveTransactionWithId(unittest.TestCase):
    """SaveTransactionWithId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSaveTransactionWithId(self):
        """Test SaveTransactionWithId"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SaveTransactionWithId()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
