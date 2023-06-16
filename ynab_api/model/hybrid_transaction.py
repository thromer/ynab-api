"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ynab_api.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from ynab_api.exceptions import ApiAttributeError


def lazy_import():
    from ynab_api.model.hybrid_transaction_all_of import HybridTransactionAllOf
    from ynab_api.model.transaction_summary import TransactionSummary
    globals()['HybridTransactionAllOf'] = HybridTransactionAllOf
    globals()['TransactionSummary'] = TransactionSummary


class HybridTransaction(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('cleared',): {
            'CLEARED': "cleared",
            'UNCLEARED': "uncleared",
            'RECONCILED': "reconciled",
        },
        ('type',): {
            'TRANSACTION': "transaction",
            'SUBTRANSACTION': "subtransaction",
        },
        ('flag_color',): {
            'None': None,
            'RED': "red",
            'ORANGE': "orange",
            'YELLOW': "yellow",
            'GREEN': "green",
            'BLUE': "blue",
            'PURPLE': "purple",
        },
        ('debt_transaction_type',): {
            'None': None,
            'PAYMENT': "payment",
            'REFUND': "refund",
            'FEE': "fee",
            'INTEREST': "interest",
            'ESCROW': "escrow",
            'BALANCEDADJUSTMENT': "balancedAdjustment",
            'CREDIT': "credit",
            'CHARGE': "charge",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'date': (date,),  # noqa: E501
            'amount': (int,),  # noqa: E501
            'cleared': (str,),  # noqa: E501
            'approved': (bool,),  # noqa: E501
            'account_id': (str,),  # noqa: E501
            'deleted': (bool,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'account_name': (str,),  # noqa: E501
            'memo': (str, none_type,),  # noqa: E501
            'flag_color': (str, none_type,),  # noqa: E501
            'payee_id': (str, none_type,),  # noqa: E501
            'category_id': (str, none_type,),  # noqa: E501
            'transfer_account_id': (str, none_type,),  # noqa: E501
            'transfer_transaction_id': (str, none_type,),  # noqa: E501
            'matched_transaction_id': (str, none_type,),  # noqa: E501
            'import_id': (str, none_type,),  # noqa: E501
            'import_payee_name': (str, none_type,),  # noqa: E501
            'import_payee_name_original': (str, none_type,),  # noqa: E501
            'debt_transaction_type': (str, none_type,),  # noqa: E501
            'parent_transaction_id': (str,),  # noqa: E501
            'payee_name': (str,),  # noqa: E501
            'category_name': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'date': 'date',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'cleared': 'cleared',  # noqa: E501
        'approved': 'approved',  # noqa: E501
        'account_id': 'account_id',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
        'type': 'type',  # noqa: E501
        'account_name': 'account_name',  # noqa: E501
        'memo': 'memo',  # noqa: E501
        'flag_color': 'flag_color',  # noqa: E501
        'payee_id': 'payee_id',  # noqa: E501
        'category_id': 'category_id',  # noqa: E501
        'transfer_account_id': 'transfer_account_id',  # noqa: E501
        'transfer_transaction_id': 'transfer_transaction_id',  # noqa: E501
        'matched_transaction_id': 'matched_transaction_id',  # noqa: E501
        'import_id': 'import_id',  # noqa: E501
        'import_payee_name': 'import_payee_name',  # noqa: E501
        'import_payee_name_original': 'import_payee_name_original',  # noqa: E501
        'debt_transaction_type': 'debt_transaction_type',  # noqa: E501
        'parent_transaction_id': 'parent_transaction_id',  # noqa: E501
        'payee_name': 'payee_name',  # noqa: E501
        'category_name': 'category_name',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """HybridTransaction - a model defined in OpenAPI

        Keyword Args:
            id (str):
            date (date): The transaction date in ISO format (e.g. 2016-12-01)
            amount (int): The transaction amount in milliunits format
            cleared (str): The cleared status of the transaction
            approved (bool): Whether or not the transaction is approved
            account_id (str):
            deleted (bool): Whether or not the transaction has been deleted.  Deleted transactions will only be included in delta requests.
            type (str): Whether the hybrid transaction represents a regular transaction or a subtransaction
            account_name (str):
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            memo (str, none_type): [optional]  # noqa: E501
            flag_color (str, none_type): The transaction flag. [optional]  # noqa: E501
            payee_id (str, none_type): [optional]  # noqa: E501
            category_id (str, none_type): [optional]  # noqa: E501
            transfer_account_id (str, none_type): If a transfer transaction, the account to which it transfers. [optional]  # noqa: E501
            transfer_transaction_id (str, none_type): If a transfer transaction, the id of transaction on the other side of the transfer. [optional]  # noqa: E501
            matched_transaction_id (str, none_type): If transaction is matched, the id of the matched transaction. [optional]  # noqa: E501
            import_id (str, none_type): If the transaction was imported, this field is a unique (by account) import identifier.  If this transaction was imported through File Based Import or Direct Import and not through the API, the import_id will have the format: 'YNAB:[milliunit_amount]:[iso_date]:[occurrence]'.  For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of 'YNAB:-294230:2015-12-30:1'.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be 'YNAB:-294230:2015-12-30:2'.. [optional]  # noqa: E501
            import_payee_name (str, none_type): If the transaction was imported, the payee name that was used when importing and before applying any payee rename rules. [optional]  # noqa: E501
            import_payee_name_original (str, none_type): If the transaction was imported, the original payee name as it appeared on the statement. [optional]  # noqa: E501
            debt_transaction_type (str, none_type): If the transaction is a debt/loan account transaction, the type of transaction. [optional]  # noqa: E501
            parent_transaction_id (str): For subtransaction types, this is the id of the parent transaction.  For transaction types, this id will be always be null.. [optional]  # noqa: E501
            payee_name (str): [optional]  # noqa: E501
            category_name (str): The name of the category.  If a split transaction, this will be 'Split'.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """HybridTransaction - a model defined in OpenAPI

        Keyword Args:
            id (str):
            date (date): The transaction date in ISO format (e.g. 2016-12-01)
            amount (int): The transaction amount in milliunits format
            cleared (str): The cleared status of the transaction
            approved (bool): Whether or not the transaction is approved
            account_id (str):
            deleted (bool): Whether or not the transaction has been deleted.  Deleted transactions will only be included in delta requests.
            type (str): Whether the hybrid transaction represents a regular transaction or a subtransaction
            account_name (str):
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            memo (str, none_type): [optional]  # noqa: E501
            flag_color (str, none_type): The transaction flag. [optional]  # noqa: E501
            payee_id (str, none_type): [optional]  # noqa: E501
            category_id (str, none_type): [optional]  # noqa: E501
            transfer_account_id (str, none_type): If a transfer transaction, the account to which it transfers. [optional]  # noqa: E501
            transfer_transaction_id (str, none_type): If a transfer transaction, the id of transaction on the other side of the transfer. [optional]  # noqa: E501
            matched_transaction_id (str, none_type): If transaction is matched, the id of the matched transaction. [optional]  # noqa: E501
            import_id (str, none_type): If the transaction was imported, this field is a unique (by account) import identifier.  If this transaction was imported through File Based Import or Direct Import and not through the API, the import_id will have the format: 'YNAB:[milliunit_amount]:[iso_date]:[occurrence]'.  For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of 'YNAB:-294230:2015-12-30:1'.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be 'YNAB:-294230:2015-12-30:2'.. [optional]  # noqa: E501
            import_payee_name (str, none_type): If the transaction was imported, the payee name that was used when importing and before applying any payee rename rules. [optional]  # noqa: E501
            import_payee_name_original (str, none_type): If the transaction was imported, the original payee name as it appeared on the statement. [optional]  # noqa: E501
            debt_transaction_type (str, none_type): If the transaction is a debt/loan account transaction, the type of transaction. [optional]  # noqa: E501
            parent_transaction_id (str): For subtransaction types, this is the id of the parent transaction.  For transaction types, this id will be always be null.. [optional]  # noqa: E501
            payee_name (str): [optional]  # noqa: E501
            category_name (str): The name of the category.  If a split transaction, this will be 'Split'.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              HybridTransactionAllOf,
              TransactionSummary,
          ],
          'oneOf': [
          ],
        }
