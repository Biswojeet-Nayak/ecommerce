from django.http import HttpResponse
from django.views import View


class API(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, world. You're at the home page.")

    def post(self, request, *args, **kwargs):
        return HttpResponse("Hello, world. You're at the home page.")

    def patch(self, request, *args, **kwargs):
        return HttpResponse("Hello, world. You're at the home page.")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("Hello, world. You're at the home page.")
