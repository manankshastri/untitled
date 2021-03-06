from django.conf import settings


class LoginRequiredMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        respose = self.get_response(request)
        return respose