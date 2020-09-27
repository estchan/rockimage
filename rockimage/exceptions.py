from flask import jsonify


class BaseHTTPException(Exception):
    def __init__(self, message=None, status_code=None):
        self.message = message
        self.status_code = status_code


class NotFound(BaseHTTPException):
    def __init__(self, message="Not Found"):
        super().__init__(message, status_code=404)
