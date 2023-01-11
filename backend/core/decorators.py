from exceptions import Unauthorized
from logger import get_logger
from responses import OK, GenericError, UnauthorizedRes

logger = get_logger()


def api_interface(func):
    """
    Decorator for methods which are called directly from the API layer.
    We always want to ensure the application does not throw exceptions and return a proper error to the user
    :param func:
    :return:
    """
    def inner_function(*args, **kwargs):
        try:
            data = func(*args, **kwargs)
            return OK(data=data)
        except Unauthorized as exc:
            msg = f'User is unauthorized: {exc}'
            logger.error(msg)
            return UnauthorizedRes(msg='User is unauthorized')
        except Exception as exc:
            msg = f'Error occurred in {func}: {exc}'
            logger.error(msg)
            return GenericError(msg='Unexpected error occurred! Please contact Yirmiyahu Library support')

    return inner_function