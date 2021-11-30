import threading

GLOBAL_REQUEST = threading.local()

class GlobalRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        GLOBAL_REQUEST.request = request
        try:
            return self.get_response(request)
        finally:
            del GLOBAL_REQUEST.request

    @staticmethod
    def get_request():
        try:
            return GLOBAL_REQUEST.request
        except AttributeError:
            return None