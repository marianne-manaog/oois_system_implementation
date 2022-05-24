# This Python file contains utility-type of functions leveraged for raw input validation by the file app.py and used by other Python files.

import logging

utils_log = logging.getLogger(__name__)


def validate_float_input():
    # type: () -> float
    """
    This function validates whether an input value is a float and returns it if so.

    Returns:
        validated_float_input: float
                            the input as a float if validated; otherwise, it throws an exception and logs an error.
    """

    input_value = raw_input("Please type a number, preferably with decimals (float): ")
    try:
        validated_float_input = float(input_value)
        return validated_float_input
    except ValueError:
        utils_log.error("The following input value is not a valid number: {}".format(input_value))


def validate_int_input():
    # type: () -> int
    """
    This function validates whether an input value is an integer and returns it if so.

    Returns:
        validated_int_input: int
                            the input as an integer if validated; otherwise, it throws an exception and logs an error.
    """

    input_value = raw_input("Please type a number: ")
    try:
        validated_int_input = int(input_value)
        return validated_int_input
    except ValueError:
        utils_log.error("The following input value is not a valid number: {}".format(input_value))


def validate_str_input():
    # type: () -> str
    """
    This function validates whether an input value is a string and returns it if so.

    Returns:
        validated_str_input: str
                            the input as a string if validated; otherwise, it throws an exception and logs an error.
    """

    input_value = raw_input("Please type a string: ")
    try:
        if type(input_value) == str:
            validated_str_input = input_value
            return validated_str_input
        else:
            raise TypeError
    except TypeError as type_err:
        utils_log.error("The type error '{}' occurred as the following input value is not a valid number: {}".format(
            type_err, input_value)
        )
