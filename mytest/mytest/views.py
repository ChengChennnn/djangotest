from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Nginx and django should ready now.")