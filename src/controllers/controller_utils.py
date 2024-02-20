
from enum import Enum

from src.common.controller_error import ControllerError

class ResponseCodes(Enum):
    STATUS_CODE_REQUEST_SUCCESS = "request_success"
    STATUS_CODE_REQUEST_FAILED = "request_failed"
    STATUS_CODE_SERVER_ERROR = "server_error"


def create_response(content: dict):
    return {
        "status": ResponseCodes.STATUS_CODE_REQUEST_SUCCESS.value,
        "content": content
    }, 200
