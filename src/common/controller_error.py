import werkzeug
# class ControllerError(werkzeug.exceptions.ServiceUnavailable):
class ControllerError(Exception):
    code = 503
    description = 'Not enough storage space.'
