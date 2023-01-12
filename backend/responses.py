from typing import Any
import requests


class BaseResponse:
    def __init__(self, msg: str = None, data: Any = None,  status_code: int = requests.codes.ok):
        self.msg = msg
        self.data = data
        self.status_code = status_code

    def get_as_json(self):
        return self.msg if self.msg else self.data


class OK(BaseResponse):
    def __init__(self, msg: str = None, data: Any = None):
        super().__init__(msg=msg, data=data, status_code=requests.codes.ok)


class BadRequest(BaseResponse):
    def __init__(self, msg: str = None):
        super().__init__(msg=msg, status_code=requests.codes.bad_request)


class GenericError(BaseResponse):
    def __init__(self, msg: str = None):
        super().__init__(msg=msg, status_code=requests.codes.internal_server_error)


class UnauthorizedRes(BaseResponse):
    def __init__(self, msg: str = None):
        super().__init__(msg=msg, status_code=requests.codes.unauthorized)


class ConflictRes(BaseResponse):
    def __init__(self, msg: str = None):
        super().__init__(msg=msg, status_code=requests.codes.conflict)
