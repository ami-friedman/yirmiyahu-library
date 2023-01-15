from core.exceptions import Unauthorized, Conflict, NotFound, NotAllowed
from logger import get_logger
from responses import OK, GenericError, UnauthorizedRes, ConflictRes, NotFoundRes, NotAllowedRes

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
            res = OK(data=data)
            return res.get_as_json(), res.status_code
        except Unauthorized as exc:
            msg = f'User is unauthorized: {exc}'
            logger.error(msg)
            res = UnauthorizedRes(msg='User is unauthorized')
            return res.get_as_json(), res.status_code
        except Conflict:
            msg = f'The item already exists in DB'
            logger.error(msg)
            res = ConflictRes(msg=msg)
            return res.get_as_json(), res.status_code
        except NotFound:
            msg = f'The item was not found in DB'
            logger.error(msg)
            res = NotFoundRes(msg=msg)
            return res.get_as_json(), res.status_code
        except NotAllowed:
            msg = f'The action requested is not allowed'
            logger.error(msg)
            res = NotAllowedRes(msg=msg)
            return res.get_as_json(), res.status_code
        except Exception as exc:
            msg = f'Error occurred in {func}: {exc}'
            logger.error(msg)
            res = GenericError(msg='Unexpected error occurred! Please contact Yirmiyahu Library support')
            return res.get_as_json(), res.status_code

    return inner_function
