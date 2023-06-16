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



class ScheduledTransactionSummary(ModelNormal):
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
        ('frequency',): {
            'NEVER': "never",
            'DAILY': "daily",
            'WEEKLY': "weekly",
            'EVERYOTHERWEEK': "everyOtherWeek",
            'TWICEAMONTH': "twiceAMonth",
            'EVERY4WEEKS': "every4Weeks",
            'MONTHLY': "monthly",
            'EVERYOTHERMONTH': "everyOtherMonth",
            'EVERY3MONTHS': "every3Months",
            'EVERY4MONTHS': "every4Months",
            'TWICEAYEAR': "twiceAYear",
            'YEARLY': "yearly",
            'EVERYOTHERYEAR': "everyOtherYear",
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
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
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
        return {
            'id': (str,),  # noqa: E501
            'date_first': (date,),  # noqa: E501
            'date_next': (date,),  # noqa: E501
            'frequency': (str,),  # noqa: E501
            'amount': (int,),  # noqa: E501
            'account_id': (str,),  # noqa: E501
            'deleted': (bool,),  # noqa: E501
            'memo': (str, none_type,),  # noqa: E501
            'flag_color': (str, none_type,),  # noqa: E501
            'payee_id': (str, none_type,),  # noqa: E501
            'category_id': (str, none_type,),  # noqa: E501
            'transfer_account_id': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'date_first': 'date_first',  # noqa: E501
        'date_next': 'date_next',  # noqa: E501
        'frequency': 'frequency',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'account_id': 'account_id',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
        'memo': 'memo',  # noqa: E501
        'flag_color': 'flag_color',  # noqa: E501
        'payee_id': 'payee_id',  # noqa: E501
        'category_id': 'category_id',  # noqa: E501
        'transfer_account_id': 'transfer_account_id',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, date_first, date_next, frequency, amount, account_id, deleted, *args, **kwargs):  # noqa: E501
        """ScheduledTransactionSummary - a model defined in OpenAPI

        Args:
            id (str):
            date_first (date): The first date for which the Scheduled Transaction was scheduled.
            date_next (date): The next date for which the Scheduled Transaction is scheduled.
            frequency (str):
            amount (int): The scheduled transaction amount in milliunits format
            account_id (str):
            deleted (bool): Whether or not the scheduled transaction has been deleted.  Deleted scheduled transactions will only be included in delta requests.

        Keyword Args:
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
            flag_color (str, none_type): The scheduled transaction flag. [optional]  # noqa: E501
            payee_id (str, none_type): [optional]  # noqa: E501
            category_id (str, none_type): [optional]  # noqa: E501
            transfer_account_id (str, none_type): If a transfer, the account_id which the scheduled transaction transfers to. [optional]  # noqa: E501
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

        self.id = id
        self.date_first = date_first
        self.date_next = date_next
        self.frequency = frequency
        self.amount = amount
        self.account_id = account_id
        self.deleted = deleted
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
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
    ])

    @convert_js_args_to_python_args
    def __init__(self, id, date_first, date_next, frequency, amount, account_id, deleted, *args, **kwargs):  # noqa: E501
        """ScheduledTransactionSummary - a model defined in OpenAPI

        Args:
            id (str):
            date_first (date): The first date for which the Scheduled Transaction was scheduled.
            date_next (date): The next date for which the Scheduled Transaction is scheduled.
            frequency (str):
            amount (int): The scheduled transaction amount in milliunits format
            account_id (str):
            deleted (bool): Whether or not the scheduled transaction has been deleted.  Deleted scheduled transactions will only be included in delta requests.

        Keyword Args:
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
            flag_color (str, none_type): The scheduled transaction flag. [optional]  # noqa: E501
            payee_id (str, none_type): [optional]  # noqa: E501
            category_id (str, none_type): [optional]  # noqa: E501
            transfer_account_id (str, none_type): If a transfer, the account_id which the scheduled transaction transfers to. [optional]  # noqa: E501
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

        self.id = id
        self.date_first = date_first
        self.date_next = date_next
        self.frequency = frequency
        self.amount = amount
        self.account_id = account_id
        self.deleted = deleted
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
