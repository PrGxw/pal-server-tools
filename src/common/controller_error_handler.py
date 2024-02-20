import logging
import traceback
from ..controllers.controller_utils import create_response, ResponseCodes
from .controller_error import ControllerError

def base_exception_handler(e: Exception):
    logging.error({
        "error": repr(e),
        "stack": traceback.format_exc()
    })

    if isinstance(e, ControllerError):
        return {
                "error": "Invalid Request.",
                "error_description": str(e)
        }, 503



    # TODO: return 500 status code.
    return {
        "error": "Server Error.",
        "error_description": "We're having a little issue with our servers.",
        "debug": repr(e)
    }, 500
